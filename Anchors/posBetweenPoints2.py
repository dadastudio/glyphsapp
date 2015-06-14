#MenuTitle: Position test
# -*- coding: utf-8 -*-
__doc__="""
Position anchor along the node respecting italic angle or any given
"""

import GlyphsApp
import vanilla
import math
Font = Glyphs.font

Glyphs.clearLog()
Glyphs.showMacroWindow()
leftMargin=15
lineHeight=30

def getItalic(x, y, angle ):
	return x + ( y * math.tan( ( angle / 180 ) * math.pi ) )


def GetAnchorNames():
	myAnchorList = []
	selectedLayers = Glyphs.currentDocument.selectedLayers()
	
	try:
		for thisLayer in selectedLayers:
			AnchorNames = list( thisLayer.anchors.keys() ) # hack to avoid traceback
			for thisAnchorName in AnchorNames:
				if thisAnchorName not in myAnchorList:
					myAnchorList.append( str(thisAnchorName) )
	except:
		print "Error: Cannot collect anchor names from the current selection."
	
	return sorted( myAnchorList )
def setLineHeight(i=0):
		return lineHeight*i+leftMargin

def moveCallback(sender):

	selectedLayer = Font.selectedLayers[0]
	try:
		selection = selectedLayer.selection()
		
		if selection.count() == 2:
			s=selection[0]
			a=selection[1]
			# a=selectedLayer.anchors[GetAnchorNames()[w.anchor_name.get()]]
			if s.y > a.y:
				yTarget=-s.y+a.y
			else:
				yTarget=a.y-s.y
			a.x=getItalic(s.x,yTarget, float(w.angle_text.get()))+26
			
		else:
			Glyphs.showMacroWindow()
			print "Make a selection!"
	except Exception, e:
		Glyphs.showMacroWindow()
		if selection == ():
			print "Cannot distribute nodes: nothing selected in frontmost layer."
		else:
			print "Error. Cannot distribute nodes:", selection
			print e


w = vanilla.FloatingWindow( (300, 130), "Position under the node")
w.anchor_label = vanilla.TextBox((leftMargin, setLineHeight(), 50, 14), "Anchor:", sizeStyle='small' )
w.anchor_name = vanilla.PopUpButton((leftMargin+60, setLineHeight()-4, -leftMargin, 20), GetAnchorNames(), sizeStyle='small' )

w.angle_label = vanilla.TextBox((leftMargin, setLineHeight(1), 0, 14), "Angle", sizeStyle='small' )
w.angle_text = vanilla.EditText((leftMargin+60, setLineHeight(1)-4, 0, 20), str(Font.selectedFontMaster.italicAngle), sizeStyle='small' )

w.mainButton = vanilla.Button((-leftMargin-150, -40, 150, -leftMargin), "Move", sizeStyle='regular', callback=moveCallback )
w.setDefaultButton( w.mainButton )
		

w.open()
w.center()



