#MenuTitle: Sync Superscript
# -*- coding: utf-8 -*-
__doc__="""

Syncs metrics and kerning groups of Superscript, and creates missing .sups glyphs

"""
import GlyphsApp
import math
Font = Glyphs.font
# Glyphs.clearLog()
# Glyphs.showMacroWindow()

supName=""
suffix=""
kernName=""

def transformNodes( thisLayer , sf ):
	offset=Font.selectedFontMaster.capHeight
	
	xHeight= Font.selectedFontMaster.xHeight * sf
	offset-=xHeight/2
	
	nodes=[]
	
	for thisPath in thisLayer.paths:
		for thisNode in thisPath.nodes:
			thisNode.connection=GSSHARP
			pos = thisNode.position
			pos.x = pos.x * sf
			pos.y = pos.y * sf
			thisNode.position = pos

			thisNode.y += offset

			if thisNode.type!=GSOFFCURVE:
				nodes.append(thisNode)

	for thisAnchor in thisLayer.anchors:
		apos=thisAnchor.position
		apos.x=apos.x * sf
		apos.y=apos.y * sf + offset
		thisAnchor.position=apos


def setSidebearings(baseName,supG):
	values={"Light":".6","Regular":".6","Bold":".6"} 
	
	supGlyph=Font.glyphs[supG]
	for thisMaster in Font.masters:
		layer=supGlyph.layers[thisMaster.id]
		
		mn=thisMaster.name.split()
		

		layer.setLeftMetricsKey_(baseName+"*"+values[mn[0]]) 
		layer.setRightMetricsKey_(baseName+"*"+values[mn[0]]) 

		layer.syncMetrics()

def setKerningGroups(baseGlyph,supG):
	g=Font.glyphs[baseGlyph]
	supGlyph=Font.glyphs[supG]
	LeftKey = g.leftKerningGroupId()
	if LeftKey:

		scLeftKey = LeftKey[:7] + LeftKey[7:]+kernName 
		supGlyph.setLeftKerningGroupId_(scLeftKey)
	
	RightKey = g.rightKerningGroupId()
	if RightKey:

		scRightKey = RightKey[:7] + RightKey[7:]+kernName 
		supGlyph.setRightKerningGroupId_(scRightKey)

def scale(sGlyphName, tGlyphName):
	
	sourceGlyph=Font.glyphs[sGlyphName]
	targetGlyph=Font.glyphs[tGlyphName]

	for thisMaster in Font.masters:
	
		sourceLayer=sourceGlyph.layers[thisMaster.id]		

		targetGlyph.layers[thisMaster.id]=sourceLayer.copyDecomposedLayer()
		layer=targetGlyph.layers[thisMaster.id]
		
		transformNodes( layer, .6 )
		layer.setAnchors_( None )

def generate(sourceGlyphName,targetGlyphName):
	if Font.glyphs[targetGlyphName]==None:
		Font.glyphs.append( GSGlyph( targetGlyphName ) )

	scale(sourceGlyphName,targetGlyphName)	
	setKerningGroups(sourceGlyphName,targetGlyphName)
	# setSidebearings(sourceGlyphName,targetGlyphName)

def syncSelected():
	global supName
	global suffix
	global kernName
	Font.disableUpdateInterface()
	
	mods=("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",  "r", "s", "t", "u", "v", "w", "x", "y", "z")
	superiors=("plus","minus","equal","parenleft","parenright")
	selectedLayers = Font.selectedLayers

	for thisLayer in selectedLayers:

		sourceGlyphName=thisLayer.parent.name  

		if thisLayer.parent.category=="Number" or sourceGlyphName in superiors: # if selected glyph is a number

			suffixOffset = sourceGlyphName.find(".") # checks if has suffix eg .lf
			
			if suffixOffset>0:
				
				supName = sourceGlyphName[:suffixOffset]+"superior"
			else:
				supName = sourceGlyphName+"superior"
			kernName="superior"
		else:	

			ssPoz=sourceGlyphName.find(".ss") # if stylistic set
			
			if ssPoz>0:
				supName= sourceGlyphName[:ssPoz]+".sups"+sourceGlyphName[ssPoz:]

			else:
				supName=sourceGlyphName+".sups" 
			
			kernName=".sups"
			
		generate(sourceGlyphName,supName)
		
		if sourceGlyphName in mods: # creates superscript glyph (eg. lmod) with unicode value
			
			if Font.glyphs[sourceGlyphName+"mod"]==None:
				Font.glyphs.append( GSGlyph( sourceGlyphName+"mod" ) )

			modGlyph=Font.glyphs[sourceGlyphName+"mod"]
			for modMaster in Font.masters:
				
				modLayer=modGlyph.layers[modMaster.id]
				modLayer.components=[]
				modLayer.paths=[]
				modLayer.components.append(GSComponent(sourceGlyphName+".sups"))
				setKerningGroups(sourceGlyphName,sourceGlyphName+"mod")
				# setSidebearings(sourceGlyphName,targetGlyphName)			

	Font.enableUpdateInterface()


def syncList():
	
	global supName
	global suffix
	global kernName
	Font.disableUpdateInterface()
	glyphsToSync=("a", "aacute", "abreve", "acaron", "acircumflex", "adblgrave", "adieresis", "agrave", "ainvertedbreve", "alpha-latin", "amacron", "aogonek", "aring", "aringacute", "atilde", "ae", "aeacute", "b", "c", "cacute", "ccaron", "ccedilla", "ccircumflex", "cdotaccent", "d", "eth", "dcaron", "dcroat", "ddotbelow", "dz", "dzcaron", "e", "eacute", "ebreve", "ecaron", "ecedilla", "ecircumflex", "edblgrave", "edieresis", "edotaccent", "edotbelow", "egrave", "einvertedbreve", "emacron", "eogonek", "etilde", "f", "g", "gacute", "gbreve", "gcaron", "gcircumflex", "gcommaaccent", "gdotaccent", "h", "hbar", "hcircumflex", "hdotbelow", "i", "idotless", "iacute", "ibreve", "icaron", "icircumflex", "idblgrave", "idieresis", "idotaccent", "idotbelow", "igrave", "iinvertedbreve", "ij", "imacron", "iogonek", "itilde", "j", "jdotless", "jcircumflex", "k", "kacute", "kcommaaccent", "kgreenlandic", "l", "lacute", "lcaron", "lcommaaccent", "ldot", "lslash", "m", "n", "nacute", "ncaron", "ncommaaccent", "ndotaccent", "eng", "ntilde", "o", "oacute", "obreve", "ocaron", "ocircumflex", "odblgrave", "odieresis", "odotbelow", "ograve", "ohungarumlaut", "oinvertedbreve", "omacron", "oogonek", "oslash", "oslashacute", "otilde", "oe", "p", "thorn", "q", "r", "racute", "rcaron", "rcommaaccent", "rdblgrave", "rdotbelow", "rinvertedbreve", "s", "sacute", "scaron", "scedilla", "scircumflex", "scommaaccent", "sdotbelow", "germandbls", "longs", "schwa", "t", "tbar", "tcaron", "tcedilla", "tcommaaccent", "tdotbelow", "u", "uacute", "ubreve", "ucaron", "ucircumflex", "udblgrave", "udieresis", "udieresisacute", "udieresiscaron", "udieresisgrave", "udieresismacron", "udotbelow", "ugrave", "uhungarumlaut", "uinvertedbreve", "umacron", "uogonek", "uring", "utilde", "v", "w", "wacute", "wcircumflex", "wdieresis", "wgrave", "x", "y", "yacute", "ycircumflex", "ydieresis", "ygrave", "ytilde", "z", "zacute", "zcaron", "zdotaccent", "zdotbelow", "iacute_j.loclNLD", "a.ss01", "aacute.ss01", "abreve.ss01", "acaron.ss01", "acircumflex.ss01", "adieresis.ss01", "agrave.ss01", "amacron.ss01", "aogonek.ss01", "aring.ss01", "aringacute.ss01", "atilde.ss01", "g.ss02", "gbreve.ss02", "gcaron.ss02", "gcircumflex.ss02", "gcommaaccent.ss02", "gdotaccent.ss02", "y.ss03", "yacute.ss03", "ycircumflex.ss03", "ydieresis.ss03", "ygrave.ss03", "ytilde.ss03", "a-cy", "be-cy", "ve-cy", "ge-cy", "gje-cy", "gheupturn-cy", "de-cy", "ie-cy", "iegrave-cy", "io-cy", "zhe-cy", "ze-cy", "ii-cy", "iishort-cy", "iigrave-cy", "ka-cy", "kje-cy", "el-cy", "em-cy", "en-cy", "o-cy", "pe-cy", "er-cy", "es-cy", "te-cy", "u-cy", "ushort-cy", "ef-cy", "ha-cy", "che-cy", "tse-cy", "sha-cy", "shcha-cy", "dzhe-cy", "softsign-cy", "hardsign-cy", "yeru-cy", "lje-cy", "nje-cy", "dze-cy", "e-cy", "ereversed-cy", "i-cy", "yi-cy", "je-cy", "tshe-cy", "iu-cy", "ia-cy", "dje-cy", "shha-cy", "ve-cy.loclBGR", "ge-cy.loclBGR", "de-cy.loclBGR", "zhe-cy.loclBGR", "ze-cy.loclBGR", "ii-cy.loclBGR", "iishort-cy.loclBGR", "ka-cy.loclBGR", "el-cy.loclBGR", "pe-cy.loclBGR", "te-cy.loclBGR", "tse-cy.loclBGR", "sha-cy.loclBGR", "shcha-cy.loclBGR", "softsign-cy.loclBGR", "hardsign-cy.loclBGR", "iu-cy.loclBGR", "A", "Aacute", "Abreve", "Acaron", "Acircumflex", "Adblgrave", "Adieresis", "Agrave", "Ainvertedbreve", "Amacron", "Aogonek", "Aring", "Aringacute", "Atilde", "AE", "AEacute", "B", "C", "Cacute", "Ccaron", "Ccedilla", "Ccircumflex", "Cdotaccent", "D", "DZ", "DZcaron", "Eth", "Dcaron", "Dcroat", "Ddotbelow", "Dz", "Dzcaron", "E", "Eacute", "Ebreve", "Ecaron", "Ecedilla", "Ecircumflex", "Edblgrave", "Edieresis", "Edotaccent", "Edotbelow", "Egrave", "Einvertedbreve", "Emacron", "Eogonek", "Etilde", "F", "G", "Gacute", "Gbreve", "Gcaron", "Gcircumflex", "Gcommaaccent", "Gdotaccent", "H", "Hbar", "Hcircumflex", "Hdotbelow", "I", "IJ", "Iacute", "Ibreve", "Icaron", "Icircumflex", "Idblgrave", "Idieresis", "Idotaccent", "Idotbelow", "Igrave", "Iinvertedbreve", "Imacron", "Iogonek", "Itilde", "J", "Jcircumflex", "K", "Kcommaaccent", "L", "Lacute", "Lcaron", "Lcommaaccent", "Ldot", "Lslash", "M", "N", "Nacute", "Ncaron", "Ncommaaccent", "Ndotaccent", "Eng", "Ntilde", "O", "Oacute", "Obreve", "Ocaron", "Ocircumflex", "Odblgrave", "Odieresis", "Odotbelow", "Ograve", "Ohungarumlaut", "Oinvertedbreve", "Omacron", "Oogonek", "Oslash", "Oslashacute", "Otilde", "OE", "P", "Thorn", "Q", "R", "Racute", "Rcaron", "Rcommaaccent", "Rdblgrave", "Rdotbelow", "Rinvertedbreve", "S", "Sacute", "Scaron", "Scedilla", "Scircumflex", "Scommaaccent", "Sdotbelow", "Germandbls", "Schwa", "T", "Tbar", "Tcaron", "Tcedilla", "Tcommaaccent", "Tdotbelow", "U", "Uacute", "Ubreve", "Ucaron", "Ucircumflex", "Udblgrave", "Udieresis", "Udieresisacute", "Udieresiscaron", "Udieresisgrave", "Udieresismacron", "Udotbelow", "Ugrave", "Uhungarumlaut", "Uinvertedbreve", "Umacron", "Uogonek", "Uring", "Utilde", "V", "W", "Wacute", "Wcircumflex", "Wdieresis", "Wgrave", "X", "Y", "Yacute", "Ycircumflex", "Ydieresis", "Ygrave", "Ytilde", "Z", "Zacute", "Zcaron", "Zdotaccent", "Zdotbelow", "Iacute_J.loclNLD", "A-cy", "Be-cy", "Ve-cy", "Ge-cy", "Gje-cy", "Gheupturn-cy", "De-cy", "Ie-cy", "Iegrave-cy", "Io-cy", "Zhe-cy", "Ze-cy", "Ii-cy", "Iishort-cy", "Iigrave-cy", "Ka-cy", "Kje-cy", "El-cy", "Em-cy", "En-cy", "O-cy", "Pe-cy", "Er-cy", "Es-cy", "Te-cy", "U-cy", "Ushort-cy", "Ef-cy", "Ha-cy", "Che-cy", "Tse-cy", "Sha-cy", "Shcha-cy", "Dzhe-cy", "Softsign-cy", "Hardsign-cy", "Yeru-cy", "Lje-cy", "Nje-cy", "Dze-cy", "E-cy", "Ereversed-cy", "I-cy", "Yi-cy", "Je-cy", "Tshe-cy", "Iu-cy", "Ia-cy", "Dje-cy", "Shha-cy", "De-cy.loclBGR", "El-cy.loclBGR", "cent", "dollar", "euro", "florin", "franc", "hryvnia", "ruble", "sterling", "yen", "approxequal", "asciitilde", "divide", "emptyset", "equal", "greater", "greaterequal", "infinity", "integral", "less", "lessequal", "logicalnot", "micro", "minus", "multiply", "notequal", "partialdiff", "plus", "plusminus", "at", "ampersand", "section", "dagger", "daggerdbl", "backslash", "colon", "comma", "ellipsis", "exclam", "exclamdown", "numbersign", "period", "question", "questiondown", "quotedbl", "quotesingle", "semicolon", "slash", "underscore", "braceleft", "braceright", "bracketleft", "bracketright", "parenleft", "parenright", "emdash", "endash", "hyphen", "guillemetleft", "guillemetright", "guilsinglleft", "guilsinglright", "quotedblbase", "quotedblleft", "quotedblright", "quoteleft", "quoteright", "quotesinglbase", "zero.lf", "one.lf", "two.lf", "three.lf", "four.lf", "five.lf", "six.lf", "seven.lf", "eight.lf", "nine.lf" )

	mods=("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",  "r", "s", "t", "u", "v", "w", "x", "y", "z")
	superiors=("plus","minus","equal","parenleft","parenright")

	for g in glyphsToSync:
		sourceGlyph=Font.glyphs[g]
		if sourceGlyph==None:
			pass

		sourceGlyphName=g  
		print g
		if sourceGlyph.category=="Number" or sourceGlyphName in superiors: # if selected glyph is a number

			suffixOffset = sourceGlyphName.find(".") # checks if has suffix eg .lf
			
			if suffixOffset>0:
				
				supName = sourceGlyphName[:suffixOffset]+"superior"
			else:
				supName = sourceGlyphName+"superior"
			kernName="superior"
		else:	

			ssPoz=sourceGlyphName.find(".ss") # if stylistic set
			
			if ssPoz>0:
				supName= sourceGlyphName[:ssPoz]+".sups"+sourceGlyphName[ssPoz:]

			else:
				supName=sourceGlyphName+".sups" 
			
			kernName=".sups"

		generate(sourceGlyphName,supName)
		if sourceGlyphName in mods: # creates superscript glyph (eg. lmod) with unicode value
			
			if Font.glyphs[sourceGlyphName+"mod"]==None:
				Font.glyphs.append( GSGlyph( sourceGlyphName+"mod" ) )

			modGlyph=Font.glyphs[sourceGlyphName+"mod"]
			for modMaster in Font.masters:
				
				modLayer=modGlyph.layers[modMaster.id]
				modLayer.components=[]
				modLayer.paths=[]
				modLayer.components.append(GSComponent(sourceGlyphName+".sups"))
				setKerningGroups(sourceGlyphName,sourceGlyphName+"mod")
				# setSidebearings(sourceGlyphName,targetGlyphName)			

	Font.enableUpdateInterface()





#syncList()
syncSelected()

