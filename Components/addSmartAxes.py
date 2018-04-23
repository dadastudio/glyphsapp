#MenuTitle: Add Smart Axes
# -*- coding: utf-8 -*-
__doc__="""
 Add Smart Axes
"""

import GlyphsApp
import copy
Font = Glyphs.font

Glyphs.clearLog()
Glyphs.showMacroWindow()

a1={"name":"short","top":100,"bottom":0}
a2={"name":"long","top":0,"bottom":100}
a3={"name":"width","top":0,"bottom":100}

axes=[a1,a2]
axes=[a3]

def addAxis(glyph,name,top,bottom):


  axisExists=0

  for a in glyph.smartComponentAxes:
   
    if a.name==name:
      axisExists=1
      break

  if axisExists==0:
    axis = GSSmartComponentAxis()
    axis.setName_(name)
    # axis.name(name)
    axis.topValue = top
    axis.bottomValue = bottom
    glyph.smartComponentAxes.append(axis)

    # print axis.name



for selectedLayer in Font.selectedLayers:
  glyph=selectedLayer.parent

  for i in xrange(len(axes)):
    addAxis(glyph,axes[i]["name"],axes[i]["top"],axes[i]["bottom"])

  for layer in glyph.layers:

    if layer.layerId == layer.associatedMasterId:  # master layer
      print layer.smartComponentPoleMapping
      for i in xrange(len(axes)):        
        
        # layer.smartComponentPoleMapping.__setitem__()#[axes[i]["name"]]=2

        lName=layer.name[:1]+"_"+axes[i]["name"]
        
        if glyph.layers[lName]==None:
          newLayer=copy.copy(layer)
          newLayer.name=lName
          glyph.layers.append(newLayer)
          # glyph.layers[lName].smartComponentPoleMapping[axes[i]["name"]]=2

  




