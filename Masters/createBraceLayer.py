#MenuTitle: Create brace layer and interpolate
import GlyphsApp

font = Glyphs.font
# Glyphs.clearLog()
# Glyphs.showMacroWindow()
selectedLayer= Font.selectedLayers

for thisLayer in selectedLayer:

  sourceGlyphName=thisLayer.parent.name  
  glyph=Font.glyphs[sourceGlyphName]
  print glyph
  
  hasBrace=False

  for layer in glyph.layers:
    if layer.name.startswith("{"):
      layer.reinterpolate()
      hasBrace=True
  
  if hasBrace==False:
    newLayer = GSLayer()
    newLayer.name = '{224, 100}'
    newLayer.associatedMasterId = font.masters[-1].id
    glyph.layers.append(newLayer)
    newLayer.reinterpolate()

  
