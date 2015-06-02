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

import GlyphsApp
Glyphs.clearLog()
Glyphs.showMacroWindow()

Font = Glyphs.font

selectedLayers = Font.selectedLayers

# SMALL CAPS

# offset=0
# suffix=".sc"
# sideBearingFactor=0
# scaleFactors=[.78,.82,.88]
# makeLowercase=True
# baseName=False
# removeAnchors=False

# JUST COPY SMALL CAPS
offset=0
suffix=".sc"
sideBearingFactor=0
scaleFactors=[1,1,1]
makeLowercase=True
removeAnchors=False
baseName=False

# SUPERSCRIPT

# offset=250
# suffix=".sups"
# sideBearingFactor=.9
# scaleFactors=[.6,.6,.6]
# makeLowercase=False
# removeAnchors=True
# baseName=False

# DENOMINATORS (FIGURES)

# offset=0
# suffix=".dnom"
# sideBearingFactor=.9
# scaleFactors=[.6,.6,.6]
# makeLowercase=False
# removeAnchors=True
# baseName=True


# SUBSCRIPT

# offset=-150
# suffix=".subs"
# sideBearingFactor=.9
# scaleFactors=[.6,.6,.6]
# makeLowercase=False
# removeAnchors=True
# baseName=True

def transformNodes( thisLayer , sf ):
	
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

			
Font.disableUpdateInterface() 

for thisLayer in selectedLayers:
	
	sourceGlyphName=thisLayer.parent.name  
	sourceGlyph=Font.glyphs[sourceGlyphName]

	newGlyphName=""
	pf=sourceGlyphName.split(".")

	if baseName==True and makeLowercase == True  :
		print "baseName==True and makeLowercase == True "
		newGlyphName=pf[0].lower() + suffix

	elif baseName==False and makeLowercase == True:
		print "baseName==False and makeLowercase == True"
		
		pf[0]= pf[0].lower()		
		
		for x in pf:
			newGlyphName=newGlyphName + "." + x	

		newGlyphName = newGlyphName[1:len(newGlyphName)] + suffix

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

		if removeAnchors == True:
			layer.setAnchors_( None )
		
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


Font.enableUpdateInterface() 


