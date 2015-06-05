#MenuTitle: Check Anchors
# -*- coding: utf-8 -*-
__doc__="""
Checks anchors across the font and optionally corrects positions respecting italic angle
"""
import GlyphsApp
import vanilla
import math
Font = Glyphs.font

Glyphs.clearLog()
Glyphs.showMacroWindow()

class AnchorsCheck(object):
	leftMargin=15
	lineHeight=30
	glyphs2Correct=[]

	def __init__(self):

		self.w = vanilla.FloatingWindow( (300, 200), "Check anchors' positions", minSize=(300,200), maxSize=(1000,200) )#, autosaveName="pl.dadastudio.Test.mainwindow"
		
		self.w.text_1 = vanilla.TextBox((self.leftMargin, self.setLineHeight(0), -15, 14), "Anchor:", sizeStyle='small' )
		
		self.w.anchor_name = vanilla.PopUpButton((self.leftMargin+75, self.setLineHeight(0), -self.leftMargin, 17), self.GetAnchorNames(), sizeStyle='small' )

		self.w.text_3 = vanilla.TextBox((self.leftMargin, self.setLineHeight(1), -15, 14), "subCategory", sizeStyle='small' )
		self.w.subCategory_name = vanilla.PopUpButton((self.leftMargin+75, self.setLineHeight(1), -self.leftMargin, 17), self.GetSubCategoryNames(), sizeStyle='small' )

		self.w.text_4 = vanilla.TextBox((self.leftMargin, self.setLineHeight(2), -15, 14), "Expected Y", sizeStyle='small' )
		self.w.setY = vanilla.EditText((self.leftMargin+75, self.setLineHeight(2), -self.leftMargin, 17), text="",sizeStyle='small' )
		
		self.w.hLine_1 = vanilla.HorizontalLine((self.leftMargin, self.setLineHeight(3), -15, 1))
		
		self.w.moveButton = vanilla.Button((-80-self.leftMargin, -40, -self.leftMargin, -self.leftMargin), "Search", sizeStyle='regular', callback=self.MoveCallback )
		self.w.correctButton = vanilla.Button((self.leftMargin, -40, 150, -self.leftMargin), "Correct", sizeStyle='regular', callback=self.CorrectCallback )
		self.w.setDefaultButton( self.w.moveButton )
		
		
		self.w.center()
		self.w.correctButton.enable(False)
	
	def italicSkew(self, x, y ):
		return x + ( y * math.tan( ( Font.selectedFontMaster.italicAngle / 180 ) * math.pi ) )

	def check(self):
		self.w.open()

	def setLineHeight(self,i):
		return self.lineHeight*i+self.leftMargin

	def CorrectCallback( self, sender ):
		
		Glyphs.clearLog()
		anchors=self.GetAnchorNames()
		anchor=anchors[self.w.anchor_name.get()]
		


		for gl in self.glyphs2Correct:
			m=gl.layers[Font.selectedFontMaster.id]
			
			mAnchor=m.anchors[anchor]
			yTarget=int(self.w.setY.get())
			
			mAnchor.x = self.italicSkew( mAnchor.x, yTarget-mAnchor.y )
			mAnchor.y=yTarget
			

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
										self.glyphs2Correct.append(gl)
										print gl.name+": " +str(l.anchors[anchor].y)

		if currText:

			Font.currentText=currText
			self.w.correctButton.enable(True)
		else :
			Glyphs.clearLog()
			print "ALL ANCHORS POSITIONED CORRECTLY!"
			self.w.correctButton.enable(False)
			Font.currentText=" "
								

	def GetAnchorNames(self):
		return ["top","bottom","center","_top"]

	def GetSubCategoryNames(self):
		return ["Uppercase","Lowercase","Smallcaps","Combining","Nonspacing","Spacing","Superscript","Modifier","Decimal Digit","Fraction","Parenthesis","Dash","Quote","Space","Format","Currency","Math","Arrow","Other"]



anchorsCheck=AnchorsCheck()
anchorsCheck.check()

