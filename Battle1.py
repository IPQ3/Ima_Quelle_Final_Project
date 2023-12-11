import js as p5
from main import *
from Ending_1 import *
from Ending_2 import *
from Characterselect import *
#character_select = Character_Select()
ending_1 = Ending_1()
ending_2 = Ending_2()
BattleBackground = p5.loadImage('Battle Background.png')

class Battle1(Character_Select):
  
  def __init__(self):
    self.Turns1 = 1
    self.ATKR = p5.random(1,3)
    self.ATK = 0
    self.bmHP = 300
    self.bmDMG = 50
    self.bmSPD = 50
    self.bmDodge = 40
    self.Hands = 2
    self.CallOfTheWild = 3

    self.chHP = 1
    self.chDMG = 1
    self.chSPD = 1
    self.BATKR = p5.random(1,5) #For random Numbers
    self.BATK = 0  #To assign attack
    self.ATKR = 0
    self.ATK = 0
    self.griffith = 1
    self.ulya = 2
    self.otto = 3
    self.character = self.ulya
    program_state = 'BATTLE1'
    
  def draw(self):
    #print('Battle1 draw()')
    global program_state
    self.character = self.ulya
    program_state = 'BATTLE1'
    p5.image(BattleBackground,0,0)
    #p5.noLoop()
    #p5.background(0)
    p5.stroke(0,0,135)
    p5.fill(0)
    p5.rect(100,265,380,60)
    p5.fill(0,0,180)
    p5.stroke(180,0,0)
    p5.textSize(15)
    p5.text('The Beast Mother stands before you.',15,270)
    #print('program_state =',program_state)
    #print('character =', self.character)
    #p5.noLoop()
    #if(p5.mouseIsPressed == True):
    #  self.update(self)
    #else:
    #  pass
    

  #def update(self):
  def update(self, program_state):
    #global program_state
    #battlestats.draw()
    p5.image(BattleBackground,0,0)
    p5.stroke(0,0,135)
    p5.fill(0)
    p5.rect(100,265,380,60)
    p5.fill(0,0,180)
    p5.stroke(180,0,0)
    p5.textSize(15)
    p5.text('The Beast Mother stands before you.',15,250)
    p5.text('What do you do.',15,270)
    p5.text('l = low attack',189,20)
    p5.text('h = high attack', 189,40)
    p5.text('d = dodge', 189,60)
