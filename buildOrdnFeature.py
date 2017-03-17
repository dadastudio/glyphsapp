#MenuTitle: Build ordn Feature
# -*- coding: utf-8 -*-
__doc__="""
Builds ordn feature based on glyphs with .ordn suffix
"""

import GlyphsApp
import vanilla

Font = Glyphs.font

Glyphs.clearLog()
Glyphs.showMacroWindow()
codesig="ORDINALS"
beginSig = "# BEGIN " + codesig + "\n"
endSig   = "# END "   + codesig + "\n"

def updated_code( oldcode, beginsig, endsig, newcode ):
	begin_offset = oldcode.find( beginsig )
	end_offset   = oldcode.find( endsig ) + len( endsig )
	newcode = oldcode[:begin_offset] + beginsig + newcode + "\n" + endsig + oldcode[end_offset:]
	return newcode


feature=Font.features["ordn"]
feature.automatic=False
featurecode=""
for glyph in Font.glyphs:
	
	if glyph.name.endswith(".ordn"):
		glyphBase=glyph.name[:-5]
		featurecode+="sub "+glyphBase+" by "+glyph.name+"\n"
		

if beginSig in feature.code:
	feature.code = updated_code( feature.code, beginSig, endSig, featurecode )	
else :	
	feature.code += "\n" + beginSig + featurecode + "\n" + endSig









