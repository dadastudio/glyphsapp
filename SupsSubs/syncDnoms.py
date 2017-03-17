#MenuTitle: Sync Denominators
# -*- coding: utf-8 -*-
__doc__="""

Syncs metrics and kerning groups of Denominators, and creates missing .dnoms glyphs

"""
import GlyphsApp
import math
Font = Glyphs.font
# Glyphs.clearLog()
# Glyphs.showMacroWindow()
kernName=""
def transformNodes( thisLayer , sf ):
	offset=0#Font.selectedFontMaster.capHeight
	
	xHeight= Font.selectedFontMaster.xHeight * sf
	# offset-=xHeight/2

	for thisPath in thisLayer.paths:
		for thisNode in thisPath.nodes:
			thisNode.connection=GSSHARP
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


def setSidebearings(baseName,supG):
	values={"Light":".6","Regular":".6","Bold":".6"} #Macho
	# values={"Light":".82","Regular":".82","Bold":".82"} #servus
	
	supGlyph=Font.glyphs[supG]
	for thisMaster in Font.masters:
		layer=supGlyph.layers[thisMaster.id]
		
		mn=thisMaster.name.split()
		

		layer.setLeftMetricsKey_(baseName+"*"+values[mn[0]]) 
		layer.setRightMetricsKey_(baseName+"*"+values[mn[0]]) 

		layer.syncMetrics()

def setKerningGroups(baseGlyph,supG):

	g=Font.glyphs[baseGlyph]
	supGlyph=Font.glyphs[supG]
	LeftKey = g.leftKerningGroupId()

	if LeftKey:

		scLeftKey = LeftKey[:7] + LeftKey[7:]+kernName #baseGlyph#getSuperscriptName( LeftKey[7:] )
		# scLeftKey = LeftKey[:7] + getSuperscriptName( LeftKey[7:] )
		supGlyph.setLeftKerningGroupId_(scLeftKey)
	
	RightKey = g.rightKerningGroupId()
	if RightKey:

		scRightKey = RightKey[:7] + RightKey[7:]+kernName #baseGlyph#getSuperscriptName( RightKey[7:] )
		supGlyph.setRightKerningGroupId_(scRightKey)

def scale(sGlyphName, tGlyphName):
	
	sourceGlyph=Font.glyphs[sGlyphName]
	targetGlyph=Font.glyphs[tGlyphName]

	for thisMaster in Font.masters:
	
		sourceLayer=sourceGlyph.layers[thisMaster.id]		

		targetGlyph.layers[thisMaster.id]=sourceLayer.copyDecomposedLayer()
		layer=targetGlyph.layers[thisMaster.id]
		
		transformNodes( layer, .6 )
		layer.setAnchors_( None )

def generate(sourceGlyphName,targetGlyphName):
	if Font.glyphs[targetGlyphName]==None:
		Font.glyphs.append( GSGlyph( targetGlyphName ) )

	scale(sourceGlyphName,targetGlyphName)	
	setKerningGroups(sourceGlyphName,targetGlyphName)
	setSidebearings(sourceGlyphName,targetGlyphName)

def syncSelected():
	global kernName
	Font.disableUpdateInterface()

	selectedLayers = Font.selectedLayers

	for thisLayer in selectedLayers:

		sourceGlyphName=thisLayer.parent.name  

		if thisLayer.parent.category=="Number": # if selected glyph is a number

			suffixOffset = sourceGlyphName.find(".") # checks if has suffix eg .lf
			
			if suffixOffset>0:
				supName = sourceGlyphName[:suffixOffset]+".dnom"
			else:
				supName =sourceGlyphName+".dnom"
			kernName=".dnom"
			generate(sourceGlyphName,supName)
				

	Font.enableUpdateInterface()


syncSelected()

