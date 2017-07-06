#MenuTitle: Generate opentype config file
# -*- coding: utf-8 -*-
__doc__="""
Generates opentype.php config file
"""
import GlyphsApp
import re

font = Glyphs.font

Glyphs.clearLog()
Glyphs.showMacroWindow()

familyName= font.familyName.lower().replace(" ","-")

otString='"'+familyName+'"=>"'

for f in font.features:
  otString+=f.name+","
otString=otString[:-1]

otString+='",'
# print otString

# Read in the file
filet = "/htdocs/plon/config/opentype.php"


with open(filet, 'r') as file :
  filedata = file.read()

# Replace the target string
# filedata = filedata.replace('atoli', 'atoli')
index=filedata.find(familyName)

replaced=re.sub('\"'+familyName+'\"=>\"(,?[a-zA-Z][a-zA-Z0-9]*,?)*\",',otString,filedata)


# Write the file out again
with open(filet, 'w') as file:
  file.write(replaced)

