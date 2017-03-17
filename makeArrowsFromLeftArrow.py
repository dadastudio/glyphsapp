#MenuTitle: Make Arrows from leftArrow
# -*- coding: utf-8 -*-
__doc__="""

copies and rotates leftArrow component

"""
import GlyphsApp
import math

Font = Glyphs.font

arrows=("northWestArrow","upArrow","northEastArrow","rightArrow","southEastArrow","downArrow","southWestArrow")

def getItalic(x, y, angle ):
	return x + ( y * math.tan( ( angle / 180 ) * math.pi ) )


def rotationTransform( angle=180.0, xOrigin=0.0, yOrigin=0.0 ):
	"""Returns a TransformStruct for rotating."""
	RotationTransform = NSAffineTransform.transform()
	RotationTransform.translateXBy_yBy_( xOrigin, yOrigin )
	RotationTransform.rotateByDegrees_( angle )
	RotationTransform.translateXBy_yBy_( -xOrigin, -yOrigin )
	
	return RotationTransform

def transformComponent( myComponent, myTransform ):
	compTransform = NSAffineTransform.transform()
	compTransform.setTransformStruct_( myComponent.transform )
	compTransform.appendTransform_( myTransform )
	myComponent.transform = compTransform.transformStruct()



for m in Font.masters:
	angle=-45

	for arrow in arrows:
		a=Font.glyphs[arrow]

		layer=a.layers[m.id]
		
		layer.components=[]
		layer.paths=[]

		layer.components.append(GSComponent("leftArrow"))
		comp=layer.components[0]
		
		RotationTransform = NSAffineTransform.transform()

		comp.transform=( 1, 0, 0, 1, 0, 0 )
		offset=getItalic(0,m.xHeight/2,m.italicAngle)
		transformComponent(comp,rotationTransform(angle,layer.bounds.size.width/2+layer.LSB+offset,m.xHeight/2))
		
		layer.syncMetrics()
		angle-=45	

	



