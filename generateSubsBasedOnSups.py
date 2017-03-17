#MenuTitle: Generate Subs Based On Sups
# -*- coding: utf-8 -*-
__doc__="""

Generate Subs Based On Sups

"""
import GlyphsApp

Font = Glyphs.font

subGlyphs=[]

glyphs2Add=[]
inferiors=["zeroinferior",
"oneinferior",
"twoinferior",
"threeinferior",
"fourinferior",
"fiveinferior",
"sixinferior",
"seveninferior",
"eightinferior",
"nineinferior",
"parenleftinferior",
"parenrightinferior",
"equalinferior",
"minusinferior",
"plusinferior"
]


Font.disableUpdateInterface()


for glyph in Font.glyphs:

	if glyph.name.endswith(".sups"):

		baseName=glyph.name[:-5]
		
		subGlyphName=baseName+".subs"

		if Font.glyphs[subGlyphName]==None:
			glyphs2Add.append(subGlyphName)

		subGlyphs.append(subGlyphName)	

for g2A in glyphs2Add:
	Font.glyphs.append(GSGlyph(g2A))


def makeit(g,nr=-5,suffix=".sups"):

	subGlyph=Font.glyphs[g]
	subGlyphName= subGlyph.name
	baseName=subGlyphName[:nr]
	glyphName=subGlyphName[:nr]+suffix

	baseGlyph=Font.glyphs[glyphName]

	for master in Font.masters:
		layer = subGlyph.layers[master.id]
		layer.beginChanges()
		layer.components=[]
		layer.paths=[]
		comp=GSComponent(glyphName)
		comp.disableAlignment=True
		comp.position=NSPoint(0,-700)
		layer.components.append(comp)

		layer.setLeftMetricsKey_(glyphName) 
		layer.setRightMetricsKey_(glyphName) 

		# print baseGlyph
		# print subGlyph
		subGlyph.setLeftKerningGroupId_(baseGlyph.leftKerningGroupId())
		subGlyph.setRightKerningGroupId_(baseGlyph.rightKerningGroupId())
		layer.syncMetrics()
		layer.endChanges()

for inf in inferiors:
	makeit(inf,-8,"superior")

for subGlyphName in subGlyphs:
	makeit(subGlyphName)

Font.enableUpdateInterface()



# for inf in inferiors:
# 	subGlyph=Font.glyphs[inf]
# 	for master in Font.masters:
# 		layer = subGlyph.layers[master.id]
# 		layer.syncMetrics()


# for subGlyphName in subGlyphs:
# 	subGlyph=Font.glyphs[subGlyphName]

# 	for master in Font.masters:
# 		layer = subGlyph.layers[master.id]
# 		layer.syncMetrics()









