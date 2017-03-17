#MenuTitle: Update n
import GlyphsApp

font = Glyphs.font

selectedLayer= Font.selectedLayers

for thisLayer in selectedLayer:

	sourceGlyphName=thisLayer.parent.name  
	glyph=Font.glyphs[sourceGlyphName]

	
	for layer in glyph.layers:
		if layer.name.startswith("{"):
			layer.reinterpolate()

	
