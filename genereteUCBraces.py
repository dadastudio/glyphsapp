#MenuTitle: Generate .case braces
# -*- coding: utf-8 -*-
__doc__="""
Generate .case braces
"""
import GlyphsApp


Glyphs.clearLog()
Glyphs.showMacroWindow()


Font = Glyphs.font


braces=["parenleft","parenright","braceleft","braceright","bracketleft","bracketright"]

for b in braces:
  sourceGlyph=Font.glyphs[b]

  if Font.glyphs[b+".case"]==None:    
    Font.glyphs.append(GSGlyph(b+".case"))

  targetGlyph=Font.glyphs[b+".case"]
  targetGlyph.leftMetricsKey=b
  targetGlyph.rightMetricsKey=b
  targetGlyph.leftKerningGroup=b+".case"
  targetGlyph.rightKerningGroup=b+".case"

  for master in Font.masters:
    
    associatedMasterId=master.id
    targetGlyph.layers[associatedMasterId].components=[]
    component=GSComponent(sourceGlyph)

    offset=master.capHeight/2-master.xHeight/2

    print offset
    component.position=NSPoint(0,offset)
    targetGlyph.layers[associatedMasterId].components.append(component)
    
    targetGlyph.layers[associatedMasterId].syncMetrics()
  
