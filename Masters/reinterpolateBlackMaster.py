#MenuTitle: Reinterpolate Black
import GlyphsApp
import copy

font = Glyphs.font

selectedLayer= Font.selectedLayers


minVal=42
maxVal=224
weightVal=maxVal
# weightVal=160

font.masters[-1].weightValue=minVal

for thisLayer in selectedLayer:

  sourceGlyphName=thisLayer.parent.name  
  glyph=Font.glyphs[sourceGlyphName]

  newInstance = GSInstance()
  newInstance.weightValue=weightVal

  font.instances.insert(0, newInstance )

  interpolated = newInstance.interpolatedFont
  # print interpolated.glyphs[sourceGlyphName].layers[0].copyDecomposedLayer()
  del font.instances[0] #clean up
 
  dLayer = copy.copy(interpolated.glyphs[sourceGlyphName].layers[0])
  # dLayer = interpolated.glyphs[sourceGlyphName].layers[0].copyDecomposedLayer()
  # newLayer=GSLayer()
  # newLayer.name="Black 2"

  print dLayer.paths

  lastLayer=glyph.layers[font.masters[-1].id]
  # lastLayer=thisLayer.background


  lastLayer.paths=copy.copy(dLayer.paths)


  # lastLayer.anchors=copy.copy(dLayer.anchors)
  


  # newLayer.associatedMasterId = font.masters[-1].id # attach to last master

  # thisLayer=newLayer
  # font.glyphs[sourceGlyphName].layers.append(newLayer)
  # newLayer.LSB=100
  # newLayer.RSB=100

font.masters[-1].weightValue=maxVal


