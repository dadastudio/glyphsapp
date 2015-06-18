#MenuTitle: Makes copies with suffix
# -*- coding: utf-8 -*-
__doc__="""
Goes through all selected glyphs, makes copy and adds suffix

VARIABLES:
offset – move path up or down (-)
suffix – add suffix like ".sc"
sideBearingFactor – set sidebearing linking: 1 – source glyph name, 0 – values of scaleFactors, any other number
scaleFactors – list of numbers that indicate how each master should be scaled
makeLowercase – make new glyph name lowercase True/Flase
removeAnchors – remove all anchors from new glyph True/Flase
baseName – new glyph name consists form a base name of source glyph and a suffix True/Flase 


"""
import sys
import GlyphsApp
import vanilla

Glyphs.clearLog()
Glyphs.showMacroWindow()

Font = Glyphs.font

leftMargin=15
lineHeight=30

selectedLayers = Font.selectedLayers
masterScaleList=[]

def setLineHeight(i=0):
		return lineHeight*i+leftMargin


def transformNodes( thisLayer , sf ):
	offset=int(w.offset_text.get())
	for thisPath in thisLayer.paths:
		for thisNode in thisPath.nodes:

			pos = thisNode.position
			pos.x = pos.x * sf
			pos.y = pos.y * sf
			thisNode.position = pos

			thisNode.y += offset

	for thisAnchor in thisLayer.anchors:
		apos=thisAnchor.position
		apos.x=apos.x * sf
		apos.y=apos.y * sf + offset
		thisAnchor.position=apos

			

def scale(sender) :
	scaleFactors=[]
	Font.disableUpdateInterface() 

	suffixList=GetSuffixNames()
	suffix=suffixList[w.suffix_combo.get()]

	for msl in masterScaleList:
		scaleFactors.append(float(msl.get())/100)
		
	
	for thisLayer in selectedLayers:
		
		sourceGlyphName=thisLayer.parent.name  
		sourceGlyph=Font.glyphs[sourceGlyphName]

		newGlyphName=""
		pf=sourceGlyphName.split(".")
		
		baseName=w.baseName_checkbox
		makeLowercase=w.lowerCase_checkbox

		if baseName==True and makeLowercase == True  :
			print "baseName==True and makeLowercase == True "
			newGlyphName=pf[0].lower() + suffix

		elif baseName==False and makeLowercase == True:
			print "baseName==False and makeLowercase == True"
			
			pf[0]= pf[0].lower()		
			
			for x in pf:
				newGlyphName=newGlyphName + "." + x	

			newGlyphName = newGlyphName[1:len(newGlyphName)] + suffix
			print newGlyphName

		elif baseName==True and makeLowercase == False:
			print "baseName==True and makeLowercase == False"
			newGlyphName=pf[0] + suffix
		else:
			print "baseName==False and makeLowercase == False"
			newGlyphName=sourceGlyphName + suffix
		
		if Font.glyphs[newGlyphName]:								# if a glyph exists

			targetGlyph=Font.glyphs[newGlyphName]
		else:		
			targetGlyph = GSGlyph( newGlyphName )
			Font.glyphs.append( targetGlyph )


		i=0	
		for thisMaster in Font.masters:		

			sourceLayer=sourceGlyph.layers[thisMaster.id]		
			
			# ALTERNATIVE WAY OF COPYING LAYER
			# sourceComponent = GSComponent( sourceGlyphName )
			# layer=targetGlyph.layers[thisMaster.id]
			# layer.components.append(sourceComponent)		
			# layer.decomposeComponents()

			targetGlyph.layers[thisMaster.id]=sourceLayer.copyDecomposedLayer()
			layer=targetGlyph.layers[thisMaster.id]

			transformNodes( layer, scaleFactors[i] )
			removeAnchors= w.removeAnchors_checkbox.get()
			
			if removeAnchors == True:
				layer.setAnchors_( None )

			sideBearingFactor=w.sbFactors_combo.get()
			
			if sideBearingFactor == 1 :
				layer.setLeftMetricsKey_(sourceGlyph.name) 
				layer.setRightMetricsKey_(sourceGlyph.name) 
			elif sideBearingFactor == 0 :
				layer.setLeftMetricsKey_(sourceGlyph.name+"*"+str(scaleFactors[i])) 
				layer.setRightMetricsKey_(sourceGlyph.name+"*"+str(scaleFactors[i])) 

			else :
				layer.setLeftMetricsKey_(sourceGlyph.name+"*"+str(sideBearingFactor)) 
				layer.setRightMetricsKey_(sourceGlyph.name+"*"+str(sideBearingFactor)) 
				
			layer.syncMetrics()
			i=i+1
			""""""
		
	Font.enableUpdateInterface()
	
scOffset=90
def GetSuffixNames():
	return [".sc",".sups",".subs",".dnom"]
def GetPresets():
	return ["Choose...","Supscript","Subscript","Denominators"]

def getLabel(text,lH=0):
	return vanilla.TextBox((leftMargin, setLineHeight(lH), 80, 14), text, sizeStyle='small' )

def getPopUpButton(data,lH=0,callback=None):
	return vanilla.PopUpButton((leftMargin+scOffset, setLineHeight(lH)-3, -leftMargin, 20), data,callback=callback ,sizeStyle='small' )

def getCheckbox(text,lH=0,selected=True):
	return vanilla.CheckBox((leftMargin+scOffset, setLineHeight(lH), -leftMargin, 20), text, sizeStyle='small')

def getEditText(lH=0):
	return vanilla.EditText((leftMargin+scOffset, setLineHeight(lH), -leftMargin, 20), sizeStyle='small')

def onPresetsChange(sender):

	item=sender.get()

	if item == 0: #Reset
		w.suffix_combo.set(0)
		w.offset_text.set(0)
		w.baseName_checkbox.set(False)
		w.lowerCase_checkbox.set(False)
		w.removeAnchors_checkbox.set(False)
		w.sbFactors_combo.set(0)
		for m in masterScaleList:
			m.set("")

	elif item == 1:#superscirpt

		masterScaleList
		w.suffix_combo.set(1)
		w.offset_text.set(250)
		w.sbFactors_combo.set(.9)
		w.baseName_checkbox.set(False)
		w.lowerCase_checkbox.set(False)
		w.removeAnchors_checkbox.set(True)
		for m in masterScaleList:
			m.set("60")

	elif item == 2:#subscript

		w.suffix_combo.set(2)
		w.offset_text.set(-150)
		w.sbFactors_combo.set(.9)
		w.baseName_checkbox.set(False)
		w.lowerCase_checkbox.set(False)
		w.removeAnchors_checkbox.set(True)
		for m in masterScaleList:
			m.set("60")
	elif item == 3: #denominators

		w.suffix_combo.set(3)
		w.offset_text.set(0)
		w.sbFactors_combo.set(.9)
		w.baseName_checkbox.set(False)
		w.lowerCase_checkbox.set(False)
		w.removeAnchors_checkbox.set(True)
		for m in masterScaleList:
			m.set("60")

w = vanilla.FloatingWindow( (370, 300), "Copy and Scale")

w.suffix_label = getLabel("Suffix: ",0)
w.suffix_combo = getPopUpButton(GetSuffixNames(),0)

w.offset_label = getLabel("Offset: ",1)
w.offset_text = getEditText(1)

w.factors_label = getLabel("Scale %: ",2)
xOff=0


for m in Font.masters:
	
	mname=m.name.split()[0]

	exec("w.master_"+mname+"_label=vanilla.TextBox((leftMargin+scOffset+"+str(xOff)+", setLineHeight(2), 65, 20),'"+mname+"', sizeStyle='small')")
	
	eti=vanilla.EditText((leftMargin+scOffset+xOff, setLineHeight(2.7), 65, 20), sizeStyle='small')

	masterScaleList.append(eti)

	exec("w.master_"+mname+"_input=eti")
	
	xOff=xOff+70
	

sbf=getLabel("SB Factor:",3.7)
w.sidebearing_label=sbf

w.sbFactors_combo = vanilla.ComboBox((leftMargin+scOffset, setLineHeight(3.7), -leftMargin, 20),["0", "1"], sizeStyle='small')
w.options_label = getLabel("Options: ",4.7)

w.baseName_checkbox=getCheckbox("Only Base Name",3+1.7)

w.lowerCase_checkbox=getCheckbox("Make lowercase",3.7+1.7)
w.removeAnchors_checkbox=getCheckbox("Delete Anchors",4.4+1.7)

w.presetsBtnLabel=getLabel("Presets: ",7)
# w.presetsBtn=getPopUpButton(GetPresets(),7,onPresetsChange)
w.presetsBtn=vanilla.PopUpButton((leftMargin+scOffset, setLineHeight(7)-3, -leftMargin, 20), GetPresets(),callback=onPresetsChange ,sizeStyle='small' )

w.mainButton = vanilla.Button((-leftMargin-150, -40, 150, -leftMargin), "Copy and Scale", sizeStyle='regular', callback=scale )
w.setDefaultButton( w.mainButton )
		

w.open()
w.center()
