#MenuTitle: Generate Test Instances 2
# -*- coding: utf-8 -*-
__doc__="""
Open fonts and Generate Test Fonts with A-z glyphs
"""
import GlyphsApp


# font = Glyphs.font
mainPath="/Users/michaljarocinski/Documents/Glyphs/Glyphs Files/"

maciek=["Maciek/Artigua Italic","Maciek/Artigua","Maciek/Mato_italic","Maciek/Mato","Maciek/Praho Italic","Maciek/Praho"]
ludka=["Ludka/Atoli Cursive","Ludka/Atoli Transitional","Ludka/Atoli Venetian"]
machalski=["Machalski/Favela_Italic_Master","Machalski/Favela_Regular_Master","Machalski/Migrena_Grotesque_FIN_ITALIC_MASTER","Machalski/Migrena_Grotesque_FIN_REGULAR_MASTER","Machalski/Nocturne_Serif_ITALIC_MASTER","Machalski/Nocturne_Serif_NORMAL_MASTER"]
ja=["Macho/Macho Italic","Macho/Macho","Clavo/Clavo/Clavo","Clavo/Clavo/Clavo Italic","Servus/Servus Super","Servus/Servus Italic Super","Sharik/Sharik","Sharik/Sharik Italic"]
fonts=ludka
# fonts=maciek+ludka+machalski+ja

suffix="Test"
exportPath="/htdocs/plon/storage/fonts/test"

for fontPath in fonts:

  font=Glyphs.open(mainPath+fontPath+".glyphs",False)

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
    newInstance.weight = instance.weight
    newInstance.width = instance.width
    newInstance.weightValue = instance.weightValue
    newInstance.widthValue = instance.widthValue
    newInstance.isItalic = False
    newInstance.isBold = False

    if len(features)>0: 
      newInstance.customParameters["Remove Features"]=features

    newInstance.customParameters["Keep Glyphs"]=kp
    newInstance.customParameters["sampleText"]="This is a test font. Not for commercial use."
    newInstance.customParameters["weightClass"]=instance.customParameters["weightClass"]

   
    newInstance.familyName=instance.familyName+" "+suffix
    font.instances.append(newInstance)

    print newInstance.generate(FontPath = exportPath)
    Glyphs.showNotification('Export fonts', 'The export of %s Test was successful.' % (font.familyName))
    font.save()
    font.close


