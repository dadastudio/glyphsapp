#MenuTitle: Check Anchors
# -*- coding: utf-8 -*-
__doc__="""
check anchors across the font
"""
import GlyphsApp
import vanilla
Font = Glyphs.font

Glyphs.clearLog()
Glyphs.showMacroWindow()

class AnchorsCheck(object):
	leftMargin=15
	lineHeight=30

	def __init__(self):
		

		self.w = vanilla.FloatingWindow( (300, 200), "Check anchors' positions", minSize=(300,200), maxSize=(1000,200) )#, autosaveName="pl.dadastudio.Test.mainwindow"
		
		self.w.text_1 = vanilla.TextBox((self.leftMargin, self.setLineHeight(0), -15, 14), "Anchor:", sizeStyle='small' )
		
		self.w.anchor_name = vanilla.PopUpButton((self.leftMargin+75, self.setLineHeight(0), -self.leftMargin, 17), self.GetAnchorNames(), sizeStyle='small' )

		self.w.text_3 = vanilla.TextBox((self.leftMargin, self.setLineHeight(1), -15, 14), "subCategory", sizeStyle='small' )
		self.w.subCategory_name = vanilla.PopUpButton((self.leftMargin+75, self.setLineHeight(1), -self.leftMargin, 17), self.GetSubCategoryNames(), sizeStyle='small' )

		self.w.text_4 = vanilla.TextBox((self.leftMargin, self.setLineHeight(2), -15, 14), "Expected Y", sizeStyle='small' )
		self.w.setY = vanilla.EditText((self.leftMargin+75, self.setLineHeight(2), -self.leftMargin, 17), sizeStyle='small' )
		
		self.w.hLine_1 = vanilla.HorizontalLine((self.leftMargin, self.setLineHeight(3), -15, 1))
		
		self.w.moveButton = vanilla.Button((-80-self.leftMargin, -40, -self.leftMargin, -self.leftMargin), "Search", sizeStyle='regular', callback=self.MoveCallback )
		self.w.setDefaultButton( self.w.moveButton )
		
		self.w.open()
		self.w.center()


	def setLineHeight(self,i):
		return self.lineHeight*i+self.leftMargin

	def MoveCallback( self, sender ):
		master=Font.selectedFontMaster.name
		currText=""
		
		height=int(self.w.setY.get())

		subCategories=self.GetSubCategoryNames()
		subCategory=subCategories[self.w.subCategory_name.get()]
		
		anchors=self.GetAnchorNames()
		anchor=anchors[self.w.anchor_name.get()]

		for gl in Font.glyphs:

				if gl.subCategory==subCategory:

					for l in gl.layers:

						m=Font.masters[l.associatedMasterId]

						if m.name == master:
							if l.layerId == l.associatedMasterId: # only Master Layer
								if l.anchors[anchor]: # if anchor exists
									
									anchorY=l.anchors[anchor].y
									if anchorY != height: # and anchorY!=700:
										currText=currText+"/"+gl.name+" "
										print gl.name+": " +str(l.anchors[anchor].y)

		if currText:

			Font.currentText=currText
			print currText
		else :
			print "ALL ANCHORS POSITIONED CORRECTLY!"
								

	def GetAnchorNames(self):
		return ["_top","top","bottom","center"]

	def GetSubCategoryNames(self):
		return ["Uppercase","Lowercase","Smallcaps","Combining","Nonspacing","Spacing","Superscript","Modifier","Decimal Digit","Fraction","Parenthesis","Dash","Quote","Space","Format","Currency","Math","Arrow","Other"]



AnchorsCheck()

