#MenuTitle: Delete anchor
# -*- coding: utf-8 -*-
__doc__="""
Delete specified anchor from all masters of selected glyphs
"""

import GlyphsApp
import vanilla
Font = Glyphs.font

Glyphs.clearLog()
Glyphs.showMacroWindow()
leftMargin=15
lineHeight=30

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

# allAnchors=GetAnchorNames()
def setLineHeight(i=0):
		return lineHeight*i+leftMargin


def DeleteCallback(sender):

	allAnchors=GetAnchorNames()
	a2d=allAnchors[w.anchor_name.get()]
	
	aCount=0

	for l in Font.selectedLayers:

		for master in Font.masters:		
			glyph=l.parent
			layer=glyph.layers[master.id]

			if layer.anchors[a2d]:
				del(layer.anchors[a2d])
				aCount=aCount+1

	w.status_text.set(str(aCount)+" anchor/s deleted")
	
	try:
		# del allAnchors
		# allAnchors=GetAnchorNames()
		w.anchor_name.setItems(GetAnchorNames())
		# allAnchors=GetAnchorNames()
	except:
		print "Error: UPs."
	
w = vanilla.FloatingWindow( (300, 130), "Delete Anchor")
w.text_1 = vanilla.TextBox((leftMargin, setLineHeight(), 50, 14), "Anchor:", sizeStyle='small' )
w.anchor_name = vanilla.PopUpButton((leftMargin+60, setLineHeight()-2, -leftMargin, 20), GetAnchorNames(), sizeStyle='small' )

w.status_text = vanilla.TextBox((leftMargin+60, setLineHeight(1), 0, 14), "", sizeStyle='small' )

w.mainButton = vanilla.Button((-leftMargin-150, -40, 150, -leftMargin), "Delete", sizeStyle='regular', callback=DeleteCallback )
w.setDefaultButton( w.mainButton )
		

w.open()
w.center()


