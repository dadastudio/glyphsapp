#MenuTitle: Test
# -*- coding: utf-8 -*-
__doc__="""
test
"""

import GlyphsApp
import vanilla
import math
Font = Glyphs.font

# Glyphs.clearLog()
# Glyphs.showMacroWindow()
leftMargin=15
lineHeight=30

def setLineHeight(i=0):
		return lineHeight*i+leftMargin

def getItalic(x, y, angle ):
	return x + ( y * math.tan( ( angle / 180 ) * math.pi ) )

selectedLayer = Font.selectedLayers[0]
firstPoint=GSNode()

selection = []


def setWidthCallback(sender):
	global selection
	selection = selectedLayer.selection()
	if selection.count() ==2:
		selection[0].x=int(selection[0].x)
		selection[0].x=selection[1].x+float(w.offset_text.get())


def moveCallback(sender):
	global selection
	
	selection=[]
	selection = selectedLayer.selection()
	
	for sel in selection:

	
		movePoint=sel

		if firstPoint.y > movePoint.y:
			yTarget=-firstPoint.y+movePoint.y
		else:
			yTarget=movePoint.y-firstPoint.y


		italic=getItalic(firstPoint.x,yTarget,float(w.angle_text.get()))

		movePoint.x=italic+float(w.offset_text.get())+1
		movePoint.x=italic+float(w.offset_text.get())
		

def selectCallback(sender):
	global selection

	w.offset_text.setItems(Font.selectedFontMaster.verticalStems)

	selection = selectedLayer.selection()
	if selection.count() == 1:
		firstPoint.x=selection[0].x
		firstPoint.y=selection[0].y

w = vanilla.FloatingWindow( (300, 146), "Align Nodes")
# w.anchor_label = vanilla.TextBox((leftMargin, setLineHeight(), 50, 14), "Anchor:", sizeStyle='small' )
# w.anchor_name = vanilla.PopUpButton((leftMargin+60, setLineHeight()-4, -leftMargin, 20), GetAnchorNames(), sizeStyle='small' )


w.selectButton = vanilla.Button((leftMargin, setLineHeight(), -leftMargin, leftMargin), "Select", sizeStyle='regular', callback=selectCallback )

w.offset_label = vanilla.TextBox((leftMargin, setLineHeight(1), 0, 14), "Offset", sizeStyle='small' )
w.offset_text = vanilla.ComboBox((leftMargin+60, setLineHeight(1)-4, -leftMargin, 20), Font.selectedFontMaster.verticalStems, sizeStyle='small' )

w.angle_label = vanilla.TextBox((leftMargin, setLineHeight(2), 0, 14), "Angle", sizeStyle='small' )
w.angle_text = vanilla.EditText((leftMargin+60, setLineHeight(2)-4, -leftMargin, 20), Font.selectedFontMaster.italicAngle, sizeStyle='small' )

w.moveButton = vanilla.Button((leftMargin, setLineHeight(3), -leftMargin, leftMargin), "Move", sizeStyle='regular', callback=moveCallback )


w.offset_text.set("0")
# w.setDefaultButton( w.mainButton )
# w.widthButton = vanilla.Button((leftMargin, setLineHeight(3), -leftMargin, leftMargin), "Correct Width", sizeStyle='regular', callback=setWidthCallback )
	

w.open()
w.center()

# for l in Font.selectedLayers:
# 	if l.anchors["origin"]:
# 		del(l.anchors["origin"])
# 		# print l.anchors["origin"]

		

