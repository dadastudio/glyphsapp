#MenuTitle: Sups Maker
# -*- coding: utf-8 -*-
__doc__="""

Scales the glyph down and inserts paths from specified instance

"""
import GlyphsApp
import vanilla
import copy
Glyphs.clearLog()
Glyphs.showMacroWindow()
Font = Glyphs.font
#////////////////////////////////////#
scaleFactor=.6
widthGain=0
# widthGain=.02
figuresHeight=700
#////////////////////////////////////#
leftMargin=15
lineHeight=30
offset=0
selectedMaster = Font.selectedFontMaster

def setLineHeight(i=0):
    return lineHeight*i+leftMargin
scOffset=90



def GetPresets():
  return ["Choose...","sups","subs","numr","numr from .lf","dnom","dnom from .lf","ordn"]

def getLabel(text,lH=0,lm=0,ll=0):
  return vanilla.TextBox((leftMargin+lm, setLineHeight(lH)+2, 80+ll, 14), text, sizeStyle='small' )

def getPopUpButton(data,lH=0,callback=None):
  return vanilla.PopUpButton((leftMargin+scOffset, setLineHeight(lH)-3, -leftMargin, 20), data,callback=callback ,sizeStyle='small' )

def getCheckbox(text,lH=0,selected=True):
  return vanilla.CheckBox((leftMargin+scOffset, setLineHeight(lH), -leftMargin, 20), text, sizeStyle='small')

def getEditText(lH=0):
  return vanilla.EditText((leftMargin+scOffset, setLineHeight(lH), -leftMargin, 20), sizeStyle='small')



def scale(sender) :

  Font.disableUpdateInterface() 
  
  figures=["zero","one","two","three","four","five","six","seven","eight","nine"]

  selectedLayers = Font.selectedLayers
  selectedMaster = Font.selectedFontMaster

  selectedMaster.userData["supsWeightGain"]=w.weight_text.get()
  

  newInstance = GSInstance()
  newInstance.weightValue=selectedMaster.weightValue+selectedMaster.weightValue*(int(w.weight_text.get())/float(100))

  Font.instances.insert(0, newInstance )

  interpolated = newInstance.interpolatedFont
  del Font.instances[0] #clean up

  originY=Font.selectedFontMaster.capHeight

  # originH=Font.selectedLayers[0].bounds.size.height#Font.selectedFontMaster.xHeight
  
  originH=Font.selectedFontMaster.capHeight

  scaledH=originH*scaleFactor

  corrOffset=scaledH*int(w.corr_text.get())/float(100) 

  #offset przeneisc do petli – nie

  if w.offset_text.get()=="auto":
    if preset=="none":
      offset=0
    elif preset=="sups":
      # originY=664
      # scaledH=664*scaleFactor
      offset=originY - scaledH/2+corrOffset

    elif preset=="subs":
      offset=-scaledH/2+corrOffset
    elif preset=="dnom" :
      offset=corrOffset
    elif preset=="dnom lf" :
      offset=0
    elif preset=="numr":
      offset=figuresHeight - figuresHeight*scaleFactor+corrOffset
    elif preset=="numr lf":
      offset=figuresHeight - figuresHeight*scaleFactor

    elif preset=="ordn":
      offset=originY - scaledH  
  else:
    offset=int(w.offset_text.get())#+corrOffset
  

  for selectedLayer in selectedLayers:  

    glyphName=selectedLayer.parent.name

    if(glyphName[-5:]==".case"):      
      sourceGlyphName=glyphName[:-10]+".case"

    elif(glyphName[-3:]==".lf"):
      sourceGlyphName=glyphName[:-8]+".lf"

    elif(glyphName[-5:]==".zero"):
      if w.fromLf_checkbox.get():
        sourceGlyphName=glyphName.replace("."+preset,".lf")
      else:
        sourceGlyphName=glyphName.replace("."+preset,"")
    else:
      sourceGlyphName=glyphName[:-5]


    if sourceGlyphName in figures:
      if w.fromLf_checkbox.get():
        sourceGlyphName+=".lf"

    sourceGlyph=Font.glyphs[sourceGlyphName]
    # bracketLayer=None
    # bracket=None
    for lay in sourceGlyph.layers:
      if Font.selectedFontMaster.id==lay.associatedMasterId:
        if "[" in lay.name:
          bracket=lay
          print lay.name
          print interpolated.glyphs[sourceGlyphName]

          newLayer = GSLayer()
          newLayer.name = bracket.name
          # newLayer.associatedMasterId = Font.selectedFontMaster.id

          selectedLayer.parent.layers[Font.masters[-1].id]
          
          
          # font.glyphs[glyphName].layers.append(newLayer)


          # bracketLayer=interpolated.glyphs[sourceGlyphName].layers[lay.layerId].copyDecomposedLayer()


    dLayer=interpolated.glyphs[sourceGlyphName].layers[0].copyDecomposedLayer()

    hhh=dLayer.bounds.size.height*scaleFactor
    hhhh=hhh*(int(w.corr_text.get())/float(100))

    paths= dLayer.paths
    selectedLayer.clear()

    for thisPath in paths:
      for thisNode in thisPath.nodes:
        pos = thisNode.position
        pos.x = pos.x * (scaleFactor+widthGain)
        pos.y = pos.y * scaleFactor + offset #+ hhhh
        thisNode.position = pos

    selectedLayer.paths = copy.copy(paths)

    # try:
    #   bracketLayer
    # except NameError:
    #   print "brak"
    # else:
    #   print "jest"
    
    # if bracketLayer:
    #   print "jest bracket"
    #   bracketPaths= bracketLayer.paths

    #   for bracketPath in bracketPaths:
    #     for bracketNode in bracketPath.nodes:
    #       pos = bracketNode.position
    #       pos.x = pos.x * scaleFactor
    #       pos.y = pos.y * scaleFactor + offset #+ hhhh
    #       bracketNode.position = pos


    #   newLayer = GSLayer()
    #   newLayer.name = bracket.name
    #   newLayer.associatedMasterId = Font.selectedFontMaster.id
    #   font.glyphs[glyphName].layers.append(newLayer)


    selectedLayer.setLeftMetricsKey_(sourceGlyphName+"*"+str(scaleFactor)) 
    selectedLayer.setRightMetricsKey_(sourceGlyphName+"*"+str(scaleFactor))
    
    
    # selectedLayer.setLeftMetricsKey_(sourceGlyphName) 
    # selectedLayer.setRightMetricsKey_(sourceGlyphName)
    selectedLayer.syncMetrics()

    if selectedLayer.RSB<0:
      selectedLayer.setRightMetricsKey_(sourceGlyphName+"*"+str(scaleFactor)) 

    if selectedLayer.LSB<0:
      selectedLayer.setLeftMetricsKey_(sourceGlyphName+"*"+str(scaleFactor)) 


    selectedLayer.syncMetrics()

  Font.enableUpdateInterface()

w = vanilla.FloatingWindow( (370, 260), "Generate Sups/Subs")

w.weight_label = getLabel("Weight gain: ",0)
w.weight_text = vanilla.EditText((leftMargin+scOffset, setLineHeight(0), 60, 20), sizeStyle='small')
w.weight_label2 = getLabel("% (L:~40, R:~20, B:~0)",0,153,100)

w.offset_label = getLabel("Offset: ",1)
w.offset_text = vanilla.EditText((leftMargin+scOffset, setLineHeight(1), 60, 20), sizeStyle='small')

w.corr_label = getLabel("Correction Y: ",2)
w.corr_text = vanilla.EditText((leftMargin+scOffset, setLineHeight(2), 60, 20), sizeStyle='small')
w.corr2_label = getLabel("%",2,153)

w.figH_label = getLabel("Figures Height: ",3)
w.figH_text = vanilla.EditText((leftMargin+scOffset, setLineHeight(3), 60, 20), sizeStyle='small')

w.fromLf_checkbox=getCheckbox("From .lf",4)

w.weight_text.set(20)
xOff=0

weightGain=40

if selectedMaster.userData["supsWeightGain"]:  
  weightGain=int(selectedMaster.userData["supsWeightGain"])


def onPresetsChange(sender):
  global preset
  item=sender.get()

  if item == 0: #Reset
    preset="none"
    
    w.offset_text.set("0")
    w.corr_text.set(0)
    w.weight_text.set(0)

  elif item == 1:#superscirpt
    preset="sups"
    w.weight_text.set(weightGain)
    w.corr_text.set(-15)

    w.offset_text.set("auto")
    w.fromLf_checkbox.set(True)

  elif item == 2:#subscript
    preset="subs"
    w.weight_text.set(weightGain)
    w.corr_text.set(15)

    w.offset_text.set("auto")
    w.fromLf_checkbox.set(True)

  elif item == 3: #numerators osf

    preset="numr"
    w.weight_text.set(weightGain)
    w.corr_text.set(-24)

    w.offset_text.set("auto")
    w.fromLf_checkbox.set(True)

  elif item == 4: #numerators lf

    preset="numr"
    w.weight_text.set(weightGain)
    w.corr_text.set(0)

    w.offset_text.set("auto")
    w.fromLf_checkbox.set(True)

  elif item == 5: #denominators osf

    preset="dnom"
    w.weight_text.set(weightGain)
    w.corr_text.set(-24)    

    w.offset_text.set("auto")
    w.fromLf_checkbox.set(True)

  elif item == 6: #denominators lf

    preset="dnom"
    w.weight_text.set(weightGain)
    w.corr_text.set(0)    

    w.offset_text.set("auto")
    w.fromLf_checkbox.set(True)
  
  elif item == 7: #ordinals

    preset="ordn"
    w.weight_text.set(weightGain)
    w.corr_text.set(0)    

    w.offset_text.set("auto")
    w.fromLf_checkbox.set(True)

  else:
    w.offset_text.set("auto")
    



w.presetsBtnLabel=getLabel("Presets: ",5.5)
w.presetsBtn=vanilla.PopUpButton((leftMargin+scOffset, setLineHeight(5.5)-3, -leftMargin, 20), GetPresets(),callback=onPresetsChange ,sizeStyle='small' )

w.presetsBtn.set(1)
preset="sups"

w.weight_text.set(weightGain)
w.corr_text.set(-15)

w.offset_text.set("auto")
w.fromLf_checkbox.set(True)



w.mainButton = vanilla.Button((-leftMargin-150, -40, 150, -leftMargin), "Generate", sizeStyle='regular', callback=scale )
w.setDefaultButton( w.mainButton )


w.open()
# w.center()
