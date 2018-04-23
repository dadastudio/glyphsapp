#MenuTitle: Generate Test Instances
# -*- coding: utf-8 -*-
__doc__="""
Generates Test Fonts with A-z glyphs
"""
import GlyphsApp


font = Glyphs.font
Glyphs.clearLog()
Glyphs.showMacroWindow()
suffix="Test"
exportPath="/htdocs/capitalics/storage/fonts/test"

itemsToRemove=[]
kp=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "zero", "comma", "period", "hyphen","space"]

for instance in font.instances:
  if instance.familyName[-4:]==suffix:
    itemsToRemove.append(instance)
    
font.instances=[x for x in font.instances if x not in itemsToRemove]

features=[]

for feature in font.features:
  if feature.automatic==False:
    features.append(feature)

for instance in font.instances:
  
  newInstance = GSInstance()
  newInstance.active = False

  newInstance.name = instance.name
  newInstance.name = instance.name[9:] #Geller

  newInstance.weight = instance.weight
  newInstance.width = instance.width
  newInstance.weightValue = instance.weightValue
  # newInstance.widthValue = instance.widthValue
  newInstance.isItalic = False
  newInstance.isBold = False

  if len(features)>0: 
    newInstance.customParameters["Remove Features"]=features

  newInstance.customParameters["Keep Glyphs"]=kp
  newInstance.customParameters["sampleText"]="This is a test font. Not for commercial use."
  newInstance.customParameters["weightClass"]=instance.customParameters["weightClass"]

 
  newInstance.familyName=instance.familyName+" "+suffix
  newInstance.familyName="GellerHeadlineTest" #geller

  font.instances.append(newInstance)

  print newInstance.generate(FontPath = exportPath)


Glyphs.showNotification('Export fonts', 'The export of %s Test was successful.' % (Glyphs.font.familyName))

