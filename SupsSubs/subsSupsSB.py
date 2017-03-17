#MenuTitle: Set sidebearings for subs and sups
# -*- coding: utf-8 -*-
__doc__="""
Set sidebearings for subs and sups
"""
import GlyphsApp
import math
Font = Glyphs.font


for g in Font.glyphs:


	if g.name.endswith("superior") or g.name.endswith("inferior"):
		org=g.name[:-8]

	# if g.name.endswith(".subs") or g.name.endswith(".sups"):
		
		print g.name
		
		org=g.name[:-5]

		# g.setLeftMetricsKey_(org+"*"+str(.6)) 
		# g.setRightMetricsKey_(org+"*"+str(.6)) 
		
		for thisMaster in Font.masters:
			layer=g.layers[thisMaster.id]
			
			layer.setLeftMetricsKey_(org+"*"+str(.6)) 
			layer.setRightMetricsKey_(org+"*"+str(.6)) 
			layer.syncMetrics()
		
		