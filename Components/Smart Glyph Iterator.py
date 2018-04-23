#MenuTitle: Smart Iterator 1.14
# -*- coding: utf-8 -*-
__doc__="""
Creates iterations for one glyph by stepping through a range of its Smart Component settings.
"""

import vanilla, GlyphsApp, traceback

class SmartGlyphIterator( object ):
	def __init__( self ):
		defaultNumber = 4
		self.currentFont = Glyphs.font # frontmost font
		thisLayer = self.currentFont.selectedLayers[0] # first of active layers of selected glyphs
		self.currentGlyph = thisLayer.parent
		self.currentComponents = thisLayer.components
		self.currentMasterID = self.currentFont.selectedFontMaster.id
		if self.currentComponents:
			numberOfSettings = 0
			self.settingDict = {}
			numberOfComponents = len(self.currentComponents)
			for i in range(numberOfComponents):
				thisComponent = self.currentComponents[i]
				thesePieceSettings = thisComponent.component.partsSettings()
				if thesePieceSettings:
					componentIndicator = "%i:%s" % ( i, thisComponent.componentName )
					for thisSetting in thesePieceSettings:
						self.settingDict["%s:%s" % (componentIndicator,thisSetting.name)] = defaultNumber
					numberOfSettings += thesePieceSettings.count()
			
			# Window 'self.w':
			windowWidth  = 400
			windowHeight = numberOfSettings * 24 + 70
			windowWidthResize  = 500 # user can resize width by this value
			windowHeightResize = 0   # user can resize height by this value
			self.w = vanilla.FloatingWindow(
				( windowWidth, windowHeight ), # default window size
				"Smart Iterator", # window title
				minSize = ( windowWidth, windowHeight ), # minimum size (for resizing)
				maxSize = ( windowWidth + windowWidthResize, windowHeight + windowHeightResize ), # maximum size (for resizing)
				autosaveName = "com.mekkablue.SmartGlyphIterator.mainwindow" # stores last window position and size
			)
		
			# UI elements:
			self.keys = sorted( self.settingDict.keys() )
			for i in range( len(self.keys) ):
				key = self.keys[i]
				value = str( self.settingDict[key] )
				yPos = 12+24*i
				exec( "self.w.text_" + str(i) + " = vanilla.TextBox(  ( 15, " + str(yPos)   + ", -70, 18), 'No. of iterations for " + key + "', sizeStyle='small')" )
				exec( "self.w.edit_" + str(i) + " = vanilla.EditText( (-90, " + str(yPos-3) + ", -15, 19), value, sizeStyle='small', placeholder='" + key + "', callback=self.changeSettingsForKey)" )
					
			# Run Button:
			self.w.runButton = vanilla.Button((-120, -20-15, -15, -15), "Iterate", sizeStyle='regular', callback=self.SmartGlyphIteratorMain )
			self.w.setDefaultButton( self.w.runButton )
		
			# Load Settings:
			# if not self.LoadPreferences():
			# 	print "Note: 'Smart Iterator' could not load preferences. Will resort to defaults"
		
			# Open window and focus on it:
			self.w.open()
			self.w.makeKey()
		else:
			print traceback.format_exc()

	
	def createGlyphCopy( self, newSuffix ):
		thisGlyph = self.currentGlyph
		thisFont = self.currentFont
		
		# prepare glyph:
		newGlyph = thisGlyph.copy()
		newGlyphName = newGlyph.name + ".%s" % newSuffix
		newGlyph.name = newGlyphName
		newGlyph.unicode = None
		
		# remove previously generated glyph with the same name:
		oldGlyph = thisFont.glyphs[newGlyphName]
		if oldGlyph:
			thisFont.removeGlyph_( oldGlyph )
		
		return newGlyph
	
	def changeSettingsForKey( self, sender ):
		key = sender.getPlaceholder()
		if key:
			value = sender.get()
			if value:
				self.settingDict[key] = value
				print "Set %s to '%s'." % (key, value)
		#print sender.getTitle()

	def multiplyAllListValues(self, listOfNumbers):
		product = 1
		for thisNumber in listOfNumbers:
			product *= thisNumber
		return product

	def SmartGlyphIteratorMain( self, sender ):
		try:
			thisGlyph = self.currentGlyph
			thisFont = self.currentFont
			thisLayer = thisGlyph.layers[self.currentMasterID]
			settings = self.settingDict
			allKeys = sorted( settings.keys() )
			componentIndexes = [ int(x.split(":")[0]) for x in allKeys ]
			pieceSettings = [ x.split(":")[2] for x in allKeys ]
			
			print "\nAnalyzing glyph '%s':" % thisGlyph.name
			minima = []
			maxima = []
			for i in range(len(allKeys)):
				original = thisLayer.components[componentIndexes[i]].component
				propertyName = pieceSettings[i]
				print "   Property %i: %s" % (i+1, propertyName)
				partsSettings = original.partsSettings()
				minimum = None
				maximum = None
				
				key = allKeys[i]
				value = str(settings[key])
				print key, value
				
				values = value.split(",")
				if len(values) == 3:
					minimum = float(values[1])
					maximum = float(values[2])
				else:
					for j in range(len(partsSettings)):
						if partsSettings[j].name == propertyName:
							minimum = partsSettings[j].bottomValue
							maximum = partsSettings[j].topValue
							
				minima.append(minimum)
				maxima.append(maximum)
			
			numberOfIterations = [ int(str(settings[k]).split(",")[0]) for k in allKeys ]
			print "\nCreating %i iterations of %s..." % ( self.multiplyAllListValues(numberOfIterations), thisGlyph.name )
	
			listOfSettingLists = []
			for i in range(len(allKeys)):
				currentMinimum = minima[i]
				currentMaximum = maxima[i]
				currentNumberOfIterations = numberOfIterations[i]
				diff = currentMaximum - currentMinimum
				if currentNumberOfIterations < 2:
					currentNumberOfIterations = 2
				step = diff / ( currentNumberOfIterations - 1.0 )
				settingList = [ currentMinimum + i * step for i in range(currentNumberOfIterations) ]
		
				if listOfSettingLists == []:
					listOfSettingLists = [ [x] for x in settingList ]
				else:
					newListOfSettingLists = []
			
					for newSetting in settingList:
						for oldSettingList in listOfSettingLists:
							oldList = list(oldSettingList)
							oldList.append(newSetting)
							newListOfSettingLists.append( oldList )
			
					listOfSettingLists = newListOfSettingLists
			
			for thisSettingList in listOfSettingLists:
				thisStringSettingList = []
				for i in thisSettingList:
					thisStringSettingList.append(str(int(i)))
				glyphSuffix = ".".join( thisStringSettingList )
				print "   ... with suffix: %s" % glyphSuffix
				newGlyph = self.createGlyphCopy( glyphSuffix )
				newLayer = newGlyph.layers[self.currentMasterID]
				
				infos = []
				for i in range(len( thisSettingList )):
					currentComponentIndex = componentIndexes[i]
					currentComponent = newLayer.components[currentComponentIndex]
					currentKey = allKeys[i]
					currentPieceSetting = pieceSettings[i]
					currentComponent.pieceSettings()[currentPieceSetting] = thisSettingList[i]
					infos.append( 
						"%i:%s:%.1f" % (
							currentComponentIndex,
							currentPieceSetting,
							thisSettingList[i]
						) )
				
				newGlyph.note = "; ".join(infos).replace(".0","")
				self.currentFont.glyphs.append(newGlyph)
				
		except Exception, e:
			# brings macro window to front and reports error:
			Glyphs.showMacroWindow()
			print "Smart Iterator Error: %s" % e
			print traceback.format_exc()

SmartGlyphIterator()