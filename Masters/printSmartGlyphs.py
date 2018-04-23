#MenuTitle: Print glyphs with smart components
import GlyphsApp

font = Glyphs.font
Glyphs.clearLog()
Glyphs.showMacroWindow()

for glyph in font.glyphs:
  if  len(glyph.smartComponentAxes)>0:

    # print glyph.smartComponentAxes
    for x in xrange(0,len(glyph.smartComponentAxes)):
      print glyph.smartComponentAxes[x]
      del(glyph.smartComponentAxes[x])
    
      
    






  
