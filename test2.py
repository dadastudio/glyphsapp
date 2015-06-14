#MenuTitle: Get angle between 2 points 
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
angle=0
def setLineHeight(i=0):
		return lineHeight*i+leftMargin

def getItalic(x, y, angle ):
	return x + ( y * math.tan( ( angle / 180 ) * math.pi ) )

def getAngle(pt1,pt2):


	dx = pt2.x - pt1.x
	dy = pt2.y - pt1.y
	rads = math.atan2(dy,dx)
	rads %= 2*math.pi
	return 90-math.degrees(rads)



selectedLayer = Font.selectedLayers[0]
firstPoint=GSNode()

selection = []


def getAngleCallback(sender):
	global angle
	selection = selectedLayer.selection()

	if selection.count() == 2:
		
		angle= getAngle(selection[0],selection[1])
		
	print "angle "+ str(angle)


def moveCallback(sender):
	Glyphs.showMacroWindow()
	
	selection=[]
	selection = selectedLayer.selection()
	
	print "------------------------ "
	print "moveCallback "
	
	gap=20

	for sel in selection:

	
		movePoint=sel

		if firstPoint.y > movePoint.y:
			yTarget=-firstPoint.y+movePoint.y
		else:
			yTarget=movePoint.y-firstPoint.y

		# topOffsetX= math.cos(90-angle)
		# print "topOffsetX "+str(topOffsetX)	

		italic=getItalic(firstPoint.x,yTarget,angle)
		print "angle "+str(angle)
		print "italic "+str(italic)

		nn= firstPoint.x + ( yTarget * math.cos( ( (90-angle) / 180 ) * math.pi ) )
		movePoint.x=nn
		# movePoint.x=italic+float(w.angle_text.get())
		

def selectCallback(sender):
	w.angle_text.setItems(Font.selectedFontMaster.verticalStems)

	selection = selectedLayer.selection()
	if selection.count() == 1:
		firstPoint.x=selection[0].x
		firstPoint.y=selection[0].y




w = vanilla.FloatingWindow( (300, 160), "Align Nodes")
# w.anchor_label = vanilla.TextBox((leftMargin, setLineHeight(), 50, 14), "Anchor:", sizeStyle='small' )
# w.anchor_name = vanilla.PopUpButton((leftMargin+60, setLineHeight()-4, -leftMargin, 20), GetAnchorNames(), sizeStyle='small' )


w.angleButton = vanilla.Button((leftMargin, setLineHeight(), -leftMargin, leftMargin), "Get Angle", sizeStyle='regular', callback=getAngleCallback )
w.selectButton = vanilla.Button((leftMargin, setLineHeight(1), -leftMargin, leftMargin), "Select", sizeStyle='regular', callback=selectCallback )
w.moveButton = vanilla.Button((leftMargin, setLineHeight(2), -leftMargin, leftMargin), "Move", sizeStyle='regular', callback=moveCallback )

w.angle_label = vanilla.TextBox((leftMargin, setLineHeight(3), 0, 14), "Offset", sizeStyle='small' )

w.angle_text = vanilla.ComboBox((leftMargin+60, setLineHeight(3)-4, -leftMargin, 20), Font.selectedFontMaster.verticalStems, sizeStyle='small' )

w.angle_text.set("0")
# w.setDefaultButton( w.mainButton )
# w.widthButton = vanilla.Button((leftMargin, setLineHeight(4), -leftMargin, leftMargin), "Correct Width", sizeStyle='regular', callback=setWidthCallback )
	

w.open()
w.center()

# for l in Font.selectedLayers:
# 	if l.anchors["origin"]:
# 		del(l.anchors["origin"])
# 		# print l.anchors["origin"]

		

