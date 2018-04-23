#MenuTitle: Insert instances
# -*- coding: utf-8 -*-
from __future__ import division
__doc__="""
Inserts instances, based on the Luc(as), Pablo, and Maciej algorithms.
"""
import vanilla
import GlyphsApp

rangemin = 3
rangemax = 11

def distribute_lucas( min, max, n ):
  q = max / min
  return [ min * q**(i/(n-1)) for i in range(n) ]
 
def distribute_equal( min, max, n ):
  d = (max - min) / (n-1)
  return [ min + i*d for i in range(n) ]
 
def distribute_pablo( min, max, n ):
  es = distribute_equal(min, max, n)
  ls = distribute_lucas(min, max, n)
  return [ l*(1-i/(n-1)) + e*(i/(n-1)) for (i, e, l) in zip(range(n), es, ls) ]

def distribute_maciej( lightMasterWeightX, lightMasterWeightY, boldMasterWeightX, boldMasterWeightY, interpolationWeightX ):
  """
  Algorithm by Maciej Ratajski
  http://jsfiddle.net/Dm2Zk/1/
  """
  interpolationPointX =  ( interpolationWeightX - lightMasterWeightX ) / ( boldMasterWeightX - lightMasterWeightX )
  interpolationWeightY = ( ( 1 - interpolationPointX ) * ( lightMasterWeightY / lightMasterWeightX - boldMasterWeightY / boldMasterWeightX ) + boldMasterWeightY / boldMasterWeightX ) * interpolationWeightX
  interpolationPointY =  ( interpolationWeightY - lightMasterWeightY) / ( boldMasterWeightY - lightMasterWeightY )
    
  return round( ( boldMasterWeightX - lightMasterWeightX ) * interpolationPointY + lightMasterWeightX, 1 )

class InstanceMaker( object ):
  """GUI for injecting instances."""
  def __init__( self ):
    self.w = vanilla.FloatingWindow( (360, 380), "Insert weight instances", minSize=(360, 370), maxSize=(360, 550), autosaveName="com.mekkablue.InstanceMaker.mainwindow" )

    self.w.text_1 = vanilla.TextBox( (15-1, 12+2, 75, 14), "Insert", sizeStyle='small' )
    self.w.numberOfInstances = vanilla.PopUpButton( (15+40, 12, 50, 17), [str(x) for x in range( 3, 19 )], callback=self.UpdateSample, sizeStyle='small' )
    # self.w.numberOfInstances = vanilla.PopUpButton( (15+40, 12, 50, 17), [str(x) for x in range( 3, 12 )], callback=self.UpdateSample, sizeStyle='small' )
    self.w.text_2 = vanilla.TextBox( (15+40+55, 12+2, 120, 14), "instances with prefix", sizeStyle='small' )
    self.w.prefix = vanilla.EditText( (15+40+55+120, 12-1, -15, 19), "A-", callback=self.UpdateSample, sizeStyle='small')

    self.w.text_3  = vanilla.TextBox( (15-1, 40+2, 60, 14), "from:", sizeStyle='small')
    self.w.master1 = vanilla.ComboBox((15+40, 40-1, 50, 19), self.MasterList(1), callback=self.UpdateSample, sizeStyle='small' )
    self.w.text_4  = vanilla.TextBox( (15+40+55, 40+2, 55, 14), "through:", sizeStyle='small')
    self.w.master2 = vanilla.ComboBox((15+40+55+55, 40-1, 50, 19), self.MasterList(-1), callback=self.UpdateSample, sizeStyle='small' )
    self.w.text_5  = vanilla.TextBox( (15+40+55+55+55, 40+2, 55, 14), "at width:", sizeStyle='small')
    self.w.width   = vanilla.EditText((15+40+45+55+55+65, 40-1, -15, 19), "100", callback=self.UpdateSample, sizeStyle='small')
    
    self.w.text_6 = vanilla.TextBox( (15-1, 68+2, 60, 14), "using", sizeStyle='small')
    self.w.algorithm = vanilla.PopUpButton((15+40, 68, 80, 17), [ "Pablo", "Luc(as)", "linear" ], callback=self.UpdateSample, sizeStyle='small' )
    self.w.text_7 = vanilla.TextBox( (15+40+85, 68+2, 110, 14), "distribution:", sizeStyle='small')
    self.w.help_instances = vanilla.HelpButton((-15-21, 68+2, -15, 20), callback=self.openURL )
    
    self.w.existingInstances = vanilla.RadioGroup((15+30, 100, -10, 60), [ "Leave existing instances as they are", "Deactivate existing instances", "Delete existing instances" ], callback=self.SavePreferences, sizeStyle = 'small' )
    self.w.existingInstances.set( 0 )
    
    self.w.maciej        = vanilla.CheckBox((15, 170, 160, 19), "Maciej y distribution from:", value=False, callback=self.UpdateSample, sizeStyle='small' )
    self.w.text_maciej_1 = vanilla.TextBox( (15+165+55, 170+2, 55, 19), "through:", sizeStyle='small')
    self.w.text_maciej_2 = vanilla.TextBox( (15+15, 170+2+20, -40, 40), "Provide horizontal stem widths in extreme masters to interpolate contrast rather than stems.", sizeStyle='small', selectable=True )
    self.w.maciej_light  = vanilla.ComboBox((15+165, 170-2, 50, 19), self.MasterList(1), callback=self.UpdateSample, sizeStyle='small' )
    self.w.maciej_bold   = vanilla.ComboBox((15+165+55+55, 170-2, -15, 19), self.MasterList(-1), callback=self.UpdateSample, sizeStyle='small' )
    self.w.help_maciej   = vanilla.HelpButton((-15-21, 170+6+20, -15, 20), callback=self.openURL )
    
    self.w.shouldRound   = vanilla.CheckBox((15, 170+60, -15, 19), "Round all interpolation values", value=True, callback=self.UpdateSample, sizeStyle='small' )
    
    self.w.sample = vanilla.Box( (15, 170+30+40+20, -15, -30-15) )
    self.w.sample.text = vanilla.TextBox( (5, 5, -5, -5), "", sizeStyle='small')
    
    self.w.createButton = vanilla.Button((-80-15, -20-15, -15, -15), "Create", sizeStyle='regular', callback=self.CreateInstances )
    self.w.setDefaultButton( self.w.createButton )
    
    if not self.LoadPreferences():
      print "Error: Could not load preferences. Will resort to defaults."

    self.w.open()
    self.UpdateSample( self )
    self.w.makeKey()
  
  def MasterList( self, factor ):
    Font = Glyphs.font
    MasterValues = sorted( [m.weightValue for m in Font.masters], key=lambda m: m * factor )
    return MasterValues
  
  def Distribution( self ):
    a = self.w.master1.get().floatValue()
    b = self.w.master2.get().floatValue()
    n = int( self.w.numberOfInstances.getItems()[self.w.numberOfInstances.get()] )
    
    algorithm = self.w.algorithm.getItems()[self.w.algorithm.get()]
    if algorithm == "Pablo":
      distributedValues = distribute_pablo( a, b, n )
    elif algorithm == "Luc(as)":
      distributedValues = distribute_lucas( a, b, n )
    else:
      distributedValues = distribute_equal( a, b, n )
    
    return distributedValues
  
  def UpdateSample( self, sender ):
    try:
      distributedValues = self.Distribution()
      n = len( distributedValues )
      prefix = self.w.prefix.get()
      sampleText = "Will create %i instances: %s" % ( n, ", ".join( prefix+"{0:.0f}".format(weight) for weight in distributedValues ))
      
      if self.w.algorithm.getItems()[self.w.algorithm.get()] == "Luc(as)":
        sampleText += ", growth: %.1f%%" % ( (distributedValues[1] / distributedValues[0]) *100-100 )
      
      if self.w.maciej.get():
        maciejValues = self.MaciejValues()
        if maciejValues:
          maciejList = [ str( int( round( distribute_maciej( maciejValues[0], maciejValues[1], maciejValues[2], maciejValues[3], w)))) for w in distributedValues ]
          sampleText += "\n\nWill add interpolationWeightY parameters to the respective instances: %s" % ( ", ".join( maciejList ) + "." )
      
      self.w.sample.text.set( sampleText )
      self.SavePreferences( self )
    except Exception, e:
      print e
  
  def DealWithExistingInstances( self ):
    instancesChoice = self.w.existingInstances.get()
    
    if instancesChoice == 1: # deactivate
      for thisInstance in Glyphs.font.instances:
        thisInstance.active = False
    elif instancesChoice == 2: # delete
      while len( Glyphs.font.instances ) != 0:
        Glyphs.font.removeInstanceAtIndex_(0)
        
    return True
    
  def SavePreferences( self, sender ):
    Glyphs.defaults["com.mekkablue.InstanceMaker.numberOfInstances"] = self.w.numberOfInstances.get()
    Glyphs.defaults["com.mekkablue.InstanceMaker.prefix"] = self.w.prefix.get()
    Glyphs.defaults["com.mekkablue.InstanceMaker.master1"] = self.w.master1.get()
    Glyphs.defaults["com.mekkablue.InstanceMaker.master2"] = self.w.master2.get()
    Glyphs.defaults["com.mekkablue.InstanceMaker.width"] = self.w.width.get()
    Glyphs.defaults["com.mekkablue.InstanceMaker.algorithm"] = self.w.algorithm.get()
    Glyphs.defaults["com.mekkablue.InstanceMaker.existingInstances"] = self.w.existingInstances.get()
    Glyphs.defaults["com.mekkablue.InstanceMaker.maciej"] = self.w.maciej.get()
    Glyphs.defaults["com.mekkablue.InstanceMaker.maciej1"] = self.w.maciej_light.get()
    Glyphs.defaults["com.mekkablue.InstanceMaker.maciej2"] = self.w.maciej_bold.get()
    Glyphs.defaults["com.mekkablue.InstanceMaker.shouldRound"] = self.w.shouldRound.get()
    return True

  def LoadPreferences( self ):
    try:
      NSUserDefaults.standardUserDefaults().registerDefaults_(
        {
          "com.mekkablue.InstanceMaker.numberOfInstances": "6",
          "com.mekkablue.InstanceMaker.prefix": "A-",
          "com.mekkablue.InstanceMaker.master1": self.MasterList(1),
          "com.mekkablue.InstanceMaker.master2": self.MasterList(-1),
          "com.mekkablue.InstanceMaker.width": "100",
          "com.mekkablue.InstanceMaker.algorithm": "0",
          "com.mekkablue.InstanceMaker.existingInstances": "0",
          "com.mekkablue.InstanceMaker.maciej": "0",
          "com.mekkablue.InstanceMaker.maciej1": self.MasterList(1),
          "com.mekkablue.InstanceMaker.maciej2": self.MasterList(-1),
          "com.mekkablue.InstanceMaker.shouldRound": "1",
        }
      )
      self.w.numberOfInstances.set( Glyphs.defaults["com.mekkablue.InstanceMaker.numberOfInstances"] )
      self.w.prefix.set( Glyphs.defaults["com.mekkablue.InstanceMaker.prefix"] )
      self.w.master1.set( Glyphs.defaults["com.mekkablue.InstanceMaker.master1"] )
      self.w.master2.set( Glyphs.defaults["com.mekkablue.InstanceMaker.master2"] )
      self.w.width.set( Glyphs.defaults["com.mekkablue.InstanceMaker.width"] )
      self.w.algorithm.set( Glyphs.defaults["com.mekkablue.InstanceMaker.algorithm"] )
      self.w.existingInstances.set( Glyphs.defaults["com.mekkablue.InstanceMaker.existingInstances"] )
      self.w.maciej.set( Glyphs.defaults["com.mekkablue.InstanceMaker.maciej"] )
      self.w.maciej_light.set( Glyphs.defaults["com.mekkablue.InstanceMaker.maciej1"] )
      self.w.maciej_bold.set( Glyphs.defaults["com.mekkablue.InstanceMaker.maciej2"] )
      self.w.shouldRound.set( Glyphs.defaults["com.mekkablue.InstanceMaker.shouldRound"] )
    except:
      return False
    
    return True
  
  def openURL( self, sender ):
    URL = None
    if sender == self.w.help_instances:
      URL = "http://www.glyphsapp.com/tutorials/multiple-masters-part-3-setting-up-instances"
    if sender == self.w.help_maciej:
      URL = "http://www.maciejratajski.com/theory/interpolation-of-contrast/"
    if URL:
      import webbrowser
      webbrowser.open( URL )
  
  def MaciejValues( self ):
    lightX = self.w.master1.get().floatValue()
    boldX  = self.w.master2.get().floatValue()
    lightY = self.w.maciej_light.get().floatValue()
    boldY  = self.w.maciej_bold.get().floatValue()
    if lightX and boldX and lightY and boldY:
      return [ lightX, lightY, boldX, boldY ]
    else:
      return False
    
  def CreateInstances( self, sender ):
    try:
      if self.DealWithExistingInstances():
        distributedValues = self.Distribution()
        widthValue = self.w.width.get().floatValue()
        prefix = self.w.prefix.get()
        maciejYesOrNo = self.w.maciej.get()
        roundingYesOrNo  = self.w.shouldRound.get()
        
        if maciejYesOrNo:
          maciejValues = self.MaciejValues()
          # invalid if entered values are empty or invalid:
          if not maciejValues:
            maciejYesOrNo = False
    
        for thisWeight in distributedValues:
          if roundingYesOrNo:
            thisWeight = round(thisWeight)
            
          newInstance = GSInstance()
          newInstance.active = True
          newInstance.name = prefix + "{0:.0f}".format( thisWeight )
          newInstance.weightValue = thisWeight
          newInstance.widthValue = widthValue
          newInstance.isItalic = False
          newInstance.isBold = False
          
          if maciejYesOrNo:
            interpolationY = distribute_maciej( maciejValues[0], maciejValues[1], maciejValues[2], maciejValues[3], float( thisWeight ) )
            if roundingYesOrNo:
              interpolationY = round(interpolationY)
            newInstance.customParameters["InterpolationWeightY"] = ("%.1f" % interpolationY).replace(".0","")
          
          theFont = Glyphs.font
          if theFont:
            theFont.instances.append( newInstance )
            newInstance.updateInterpolationValues()
          else:
            print "Error: No current font."
      
      if not self.SavePreferences( self ):
        print "Error writing preferences."
      
      self.w.close()
    except Exception, e:
      raise e

InstanceMaker()
