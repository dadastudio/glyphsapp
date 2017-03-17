#MenuTitle: Sync SmallCaps
# -*- coding: utf-8 -*-
__doc__="""

Syncs metrics and kerning groups of SmallCaps, and creates missing sc glyphs

"""
import GlyphsApp
import math
Font = Glyphs.font
Glyphs.clearLog()
Glyphs.showMacroWindow()

newones=[]


def getSmallCapName(glyphName):
	
	suffixOffset = abs(glyphName.find("."))
	returnName = glyphName[:suffixOffset].lower() + glyphName[suffixOffset:]
	
	return returnName+".sc"

def setSidebearings(baseName,scGlyph):
	values={"Light":".8","Regular":".8","Bold":".8"} #Clavo
	# values={"Light":".79","Regular":".84","Bold":".89"} #Macho
	# values={"Light":".82","Regular":".82","Bold":".82"} #servus

	for thisMaster in Font.masters:
		layer=scGlyph.layers[thisMaster.id]
		
		mn=thisMaster.name.split()
		

		layer.setLeftMetricsKey_(baseName+"*"+values[mn[0]]) 
		layer.setRightMetricsKey_(baseName+"*"+values[mn[0]]) 

		layer.syncMetrics()

def setKerningGroups(baseGlyph,scGlyph):
	g=Font.glyphs[baseGlyph]
	LeftKey = g.leftKerningGroupId()
	if LeftKey:

		scLeftKey = LeftKey[:7] + getSmallCapName( LeftKey[7:] )
		scGlyph.setLeftKerningGroupId_(scLeftKey)
	
	RightKey = g.rightKerningGroupId()
	if RightKey:

		scRightKey = RightKey[:7] + getSmallCapName( RightKey[7:] )
		scGlyph.setRightKerningGroupId_(scRightKey)


for g in Font.glyphs:
	if g.subCategory=="Uppercase" and g.name.endswith(".subs")==False:

		scName=getSmallCapName(g.name)

		if Font.glyphs[scName]:

			scGlyph=Font.glyphs[scName]

			setKerningGroups(g.name,scGlyph)
			setSidebearings(g.name,scGlyph)

		else:
			if g.script=="latin" or g.script=="cyrillic":
				
				newones.append({g.name:scName} )
				
		
if len(newones) > 0:		
	for ng in newones:
		baseName=ng.keys()[0]
		scName=ng.values()[0]

		g=GSGlyph( scName )
		Font.glyphs.append( g )

		setKerningGroups(baseName,g)
		setSidebearings(baseName,g)






