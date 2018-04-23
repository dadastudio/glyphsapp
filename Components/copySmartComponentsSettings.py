#MenuTitle: Copy Smart Components Settings
# -*- coding: utf-8 -*-
__doc__="""
Compare glyphs in files
"""

import GlyphsApp
import vanilla
import math
import copy

Glyphs.clearLog()
Glyphs.showMacroWindow()


Font = Glyphs.font
Font.disableUpdateInterface()
for ff in Glyphs.fonts:
  if(ff==Font): continue

  if(ff.familyName==Font.familyName):
    Font2=ff
  else:
    print "Brak fonta o tej samej nazwie"




for selectedLayer in Font.selectedLayers:

  glyph=selectedLayer.parent
  
  if(Font2.glyphs[glyph.name]!=None):
    otherGlyph=Font2.glyphs[glyph.name]

    for m in range(len(Font.masters)):

      master=Font.masters[m]
      master2=Font2.masters[m]
      print "***********************************"
      selectedLayer2=otherGlyph.layers[master2.id]
      thisLayer=glyph.layers[master.id]
      
      for c in range(len(thisLayer.components)):


        thisComp = thisLayer.components[c]
        otherComp = selectedLayer2.components[c]

        # print thisComp.componentName
        
        axes=thisComp.component.smartComponentAxes

        # print thisComp.pieceSettings()
        # props=thisComp.pieceSettings()
        # for p in props.keys():
        #   print ("key "+p)


        # otherComp
        # thisComp.smartComponentValues["width"]=0
        sourceSettings=[]
        thisSettings=[]


        print otherComp.smartComponentValues
        properties = otherComp.pieceSettings().keys()
        for thisProperty in properties:
          sourceSettings.append(otherComp.pieceSettings()[thisProperty])
          print "%s: %f" % ( thisProperty, otherComp.pieceSettings()[thisProperty] )


        properties = thisComp.pieceSettings().keys()
        for thisProperty in properties:
          # sourceSettings.append(thisComp.pieceSettings()[thisProperty])
          print "%s: %f" % ( thisProperty, thisComp.pieceSettings()[thisProperty] )






        # for a in range(len(axes)):

        #   axis=axes[a]
        #   print (axis.name)
        #   try:
        #     properties[a]
        #   except Exception as e:
        #     print e

        #   else:

        #     print sourceSettings[a]
        #     print ("jest "+axis.name)
            
          




          # print otherComp.pieceSettings()
          # print otherComp.smartComponentValues



        



        # settings=otherComp.pieceSettings()

        # print settings
        # for k in settings.items():
        #   print k

        
        






          # v=0

          # try:
          #   v= otherComp.smartComponentValues[axis.name]
          # except Exception as e:
          #   print ("error ")
          #   print e



          # print ("v "+str(v))
          # if v==None:
          #   v=0
          
          # thisComp.smartComponentValues[axis.name]=v
          # try:
          #   thisComp.smartComponentValues[axis.name]=v
          # except Exception as e:
          #   thisComp.setPieceSettings_({axis.name:v})
            

          # print thisComp.smartComponentValues

          # if thisComp.smartComponentValues[axis.name]!=None:
            # thisComp.smartComponentValues[axis.name]=v

          # if (v):
          # else:
          #   thisComp.pieceSettings()[axis.name]=0


          # print thisComp.smartComponentValues[axis.name]
        #   if otherComp.smartComponentValues[axis.name]:
        #     print otherComp.smartComponentValues[axis.name]


      


        # thisComp.smartComponentValues=copy.copy(otherComp.smartComponentValues)

        # print thisLayer.components[c].componentName
        # print thisLayer.components[c].smartComponentValues



        if thisLayer.components[c].smartComponentValues:
          
          


          # properties = thisLayer.components[c].pieceSettings()
          
          # print properties.keys()

          # for k in properties.keys():
          #   print k
          #   av= selectedLayer2.components[c].pieceSettings[k]
          #   thisLayer.components[c].smartComponentValues[k]=av


          # print properties
          # print thisLayer.components[c].smartComponentValues
          # for sv in thisLayer.components[c].smartComponentValues:
          #   vv=thisLayer.components[c].smartComponentValues[sv]
          #   print vv

          # for axis in axes:
          #   print axis.name

          print "====="
            
          #   if selectedLayer2.components[c].smartComponentValues[axis.name]:
          #     av= selectedLayer2.components[c].smartComponentValues[axis.name]
          #     thisLayer.components[c].smartComponentValues[axis.name]=av







Font.enableUpdateInterface()
