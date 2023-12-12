import js as p5
from main import *
from Ending_1 import *
from Ending_2 import *
from Characterselect import *
ending_1 = Ending_1()
ending_2 = Ending_2()
BattleBackground = p5.loadImage('Battle Background.png')

class Battle1(Character_Select):
  
  def __init__(self):
    self.Turn = 1
    self.ATKR = p5.random(1,3)
    self.ATK = 0
    self.bmHP = 100
    self.bmDMG = 50
    self.bmSPD = 50
    self.bmDodge = 40
    self.Hands = 2
    self.CallOfTheWild = 3

    self.chHP = 150
    self.chDMG = 30
    self.chSPD = 40
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

    
    if(self.Turn == 1):
      if(self.character == self.otto):
        self.BMATKR = p5.random(1,5)
        if(self.BMATKR == 1):
          self.BMATK = self.bite
          if(self.BMATK == self.bite):
            self.chHP -= 30
            print('The Beast Mother bites you.')
            print('you lose 20 HP.')
            print('Character HP =', self.chHP)
            print('Character DMG =', self.chDMG)
            print('Character SPD =', self.chSPD)
            self.Turn = 3
  


        elif(self.BMATKR > 2):
          if(self.BMATKR < 3):
            self.BMATK = self.Hands
            if(self.BMATK == self.Hands):
              self.chHP -=25
              print('The Beast Mothers hands squeeze your body')
              print('you lose 20 HP')
              print('Character HP =', self.chHP)
              print('Character DMG =', self.chDMG)
              print('Character SPD =', self.chSPD)
              self.Turn = 2
      


        elif(self.BMATKR > 3):
          if(self.BMATKR < 4):
            self.BMATK = self.CallOfTheWild
            if(self.BMATK == self.CallofTheWild):
              self.chDMG -= 10
              print('The Beast Mother Howls.')
              print('your damage decreases by 10.')
              print('Character HP =', self.chHP)
              print('Character DMG =', self.chDMG)
              print('Character SPD =', self.chSPD)


              self.Turn = 2
      

        elif(self.BMATKR > 4):
          self.BMATK = self.dodge
          if(self.BMATK == self.dodge):
            print('The Beast Mother dodges your attack')
            print('Character HP =', self.chHP)
            print('Character DMG =', self.chDMG)
            print('Character SPD =', self.chSPD)
            self.Turn = 2
  
      else:
        pass
  
    if(self.Turn == 2):      
      if(self.character == self.ulya):
        self.BMATKR = p5.random(1,5)
        if(self.BMATKR == 1):
          self.BMATK = self.bite
          if(self.BMATK == self.bite):
            self.chHP -= 30
            print('The Beast Mother bites you.')
            print('you lose 20 HP.')
            print('Character HP =', self.chHP)
            print('Character DMG =', self.chDMG)
            print('Character SPD =', self.chSPD)
            self.Turn = 3
  


        elif(self.BMATKR > 2):
          if(self.BMATKR < 3):
            self.BMATK = self.Hands
            if(self.BMATK == self.Hands):
              self.chHP -=25
              print('The Beast Mothers hands squeeze your body')
              print('you lose 20 HP')
              print('Character HP =', self.chHP)
              print('Character DMG =', self.chDMG)
              print('Character SPD =', self.chSPD)


              self.Turn = 3
      


        elif(self.BMATKR > 3):
          if(self.BMATKR < 4):
            self.BMATK = self.CallOfTheWild
            if(self.BMATK == self.CallofTheWild):
              self.chDMG -= 10
              print('The Beast Mother Howls.')
              print('your damage decreases by 10.')
              print('Character HP =', self.chHP)
              print('Character DMG =', self.chDMG)
              print('Character SPD =', self.chSPD)


              self.Turn = 3
      

        elif(self.BMATKR > 4):
          self.BMATK = self.dodge
          if(self.BMATK == self.dodge):
            print('The Beast Mother dodges your attack')
            print('Character HP =', self.chHP)
            print('Character DMG =', self.chDMG)
            print('Character SPD =', self.chSPD)
            self.Turn = 3
  
      else:
        pass


  
    elif(self.Turn == 3):
      if(self.character == self.otto):
        self.BMATKR = p5.random(1,5)
        if(self.BMATKR == 1):
          self.BMATK = self.bite
          if(self.BMATK == self.bite):
            self.chHP -= 30
            print('The Beast Mother bites you.')
            print('you lose 20 HP.')
            print('Character HP =', self.chHP)
            print('Character DMG =', self.chDMG)
            print('Character SPD =', self.chSPD)
            self.Turn = 4
  


        elif(self.BMATKR > 2):
          if(self.BMATKR < 3):
            self.BMATK = self.Hands
            if(self.BMATK == self.Hands):
              self.chHP -= 25
              print('The Beast Mothers hands squeeze your body')
              print('you lose 20 HP')
              print('Character HP =', self.chHP)
              print('Character DMG =', self.chDMG)
              print('Character SPD =', self.chSPD)


              self.Turn = 4
      


        elif(self.BMATKR > 3):
          if(self.BMATKR < 4):
            self.BMATK = self.CallOfTheWild
            if(self.BMATK == self.CallofTheWild):
              self.chDMG -= 10
              print('The Beast Mother Howls.')
              print('your damage decreases by 10.')
              print('Character HP =', self.chHP)
              print('Character DMG =', self.chDMG)
              print('Character SPD =', self.chSPD)


              self.Turn = 4
      

        elif(self.BMATKR > 4):
          self.BMATK = self.dodge
          if(self.BMATK == self.dodge):
            print('The Beast Mother dodges your attack')
            print('Character HP =', self.chHP)
            print('Character DMG =', self.chDMG)
            print('Character SPD =', self.chSPD)
            self.Turn = 4
  
      else:
        pass

    
    elif(self.Turn == 4):
      if(self.character == self.ulya):
        self.BMATKR = p5.random(1,5)
        if(self.BMATKR == 1):
          self.BMATK = self.bite
          if(self.BMATK == self.bite):
            self.chHP -= 30
            print('The Beast Mother bites you.')
            print('you lose 20 HP.')
            print('Character HP =', self.chHP)
            print('Character DMG =', self.chDMG)
            print('Character SPD =', self.chSPD)
            self.Turn = 5
  
        elif(self.BMATKR > 2):
          if(self.BMATKR < 3):
            self.BMATK = self.Hands
            if(self.BMATK == self.Hands):
              self.chHP -=25
              print('The Beast Mothers hands squeeze your body')
              print('you lose 20 HP')
              print('Character HP =', self.chHP)
              print('Character DMG =', self.chDMG)
              print('Character SPD =', self.chSPD)


              self.Turn = 5
      


        elif(self.BMATKR > 3):
          if(self.BMATKR < 4):
            self.BMATK = self.CallOfTheWild
            if(self.BMATK == self.CallofTheWild):
              self.chDMG -= 10
              print('The Beast Mother Howls.')
              print('your damage decreases by 10.')
              print('Character HP =', self.chHP)
              print('Character DMG =', self.chDMG)
              print('Character SPD =', self.chSPD)


              self.Turn = 5
      

        elif(self.BMATKR > 4):
          self.BMATK = self.dodge
          if(self.BMATK == self.dodge):
            print('The Beast Mother dodges your attack')
            print('Character HP =', self.chHP)
            print('Character DMG =', self.chDMG)
            print('Character SPD =', self.chSPD)
            self.Turn = 5
  


    
    elif(self.Turn == 5):
      if(self.character == self.otto):
        self.BMATKR = p5.random(1,5)
        if(self.BMATKR == 1):
          self.BMATK = self.bite
          if(self.BMATK == self.bite):
            self.chHP -= 30
            print('The Beast Mother bites you.')
            print('you lose 20 HP.')
            print('Character HP =', self.chHP)
            print('Character DMG =', self.chDMG)
            print('Character SPD =', self.chSPD)
            self.Turn = 6
  


        elif(self.BMATKR > 2):
          if(self.BMATKR < 3):
            self.BMATK = self.Hands
            if(self.BMATK == self.Hands):
              self.chHP -=25
              print('The Beast Mothers hands squeeze your body')
              print('you lose 20 HP')
              print('Character HP =', self.chHP)
              print('Character DMG =', self.chDMG)
              print('Character SPD =', self.chSPD)


              self.Turn = 6
      


        elif(self.BMATKR > 3):
          if(self.BMATKR < 4):
            self.BMATK = self.CallOfTheWild
            if(self.BMATK == self.CallofTheWild):
              self.chDMG -= 10
              print('The Beast Mother Howls.')
              print('your damage decreases by 10.')
              print('Character HP =', self.chHP)
              print('Character DMG =', self.chDMG)
              print('Character SPD =', self.chSPD)


              self.Turn = 6
      

        elif(self.BMATKR > 4):
          self.BMATK = self.dodge
          if(self.BMATK == self.dodge):
            print('The Beast Mother dodges your attack')
            print('Character HP =', self.chHP)
            print('Character DMG =', self.chDMG)
            print('Character SPD =', self.chSPD)
            self.Turn = 6
  
      else:
        pass




    
    elif(self.Turn == 6):
      if(self.character == self.ulya):
        self.BMATKR = p5.random(1,5)
        if(self.BMATKR == 1):
          self.BMATK = self.bite
          if(self.BMATK == self.bite):
            self.chHP -= 30
            print('The Beast Mother bites you.')
            print('you lose 20 HP.')
            print('Character HP =', self.chHP)
            print('Character DMG =', self.chDMG)
            print('Character SPD =', self.chSPD)
            self.Turn = 7
  


        elif(self.BMATKR > 2):
          if(self.BMATKR < 3):
            self.BMATK = self.Hands
            if(self.BMATK == self.Hands):
              self.chHP -= 25
              print('The Beast Mothers hands squeeze your body')
              print('you lose 20 HP')
              print('Character HP =', self.chHP)
              print('Character DMG =', self.chDMG)
              print('Character SPD =', self.chSPD)
              self.Turn = 7


        elif(self.BMATKR > 3):
          if(self.BMATKR < 4):
            self.BMATK = self.CallOfTheWild
            if(self.BMATK == self.CallofTheWild):
              self.chDMG -= 10
              print('The Beast Mother Howls.')
              print('your damage decreases by 10.')
              print('Character HP =', self.chHP)
              print('Character DMG =', self.chDMG)
              print('Character SPD =', self.chSPD)
              self.Turn = 7

        elif(self.BMATKR > 4):
          self.BMATK = self.dodge
          if(self.BMATK == self.dodge):
            print('The Beast Mother dodges your attack')
            print('Character HP =', self.chHP)
            print('Character DMG =', self.chDMG)
            print('Character SPD =', self.chSPD)
            self.Turn = 7
      else:
        pass



      
    elif(self.Turn == 7):
      if(self.character == self.otto):
        self.BMATKR = p5.random(1,5)
        if(self.BMATKR == 1):
          self.BMATK = self.bite
          if(self.BMATK == self.bite):
            self.chHP -= 30
            print('The Beast Mother bites you.')
            print('you lose 20 HP.')
            print('Character HP =', self.chHP)
            print('Character DMG =', self.chDMG)
            print('Character SPD =', self.chSPD)
            self.Turn = 8


        elif(self.BMATKR > 2):
          if(self.BMATKR < 3):
            self.BMATK = self.Hands
            if(self.BMATK == self.Hands):
              self.chHP -=25
              print('The Beast Mothers hands squeeze your body')
              print('you lose 20 HP')
              print('Character HP =', self.chHP)
              print('Character DMG =', self.chDMG)
              print('Character SPD =', self.chSPD)
              self.Turn = 8


        elif(self.BMATKR > 3):
          if(self.BMATKR < 4):
            self.BMATK = self.CallOfTheWild
            if(self.BMATK == self.CallofTheWild):
              self.chDMG -= 10
              print('The Beast Mother Howls.')
              print('your damage decreases by 10.')
              print('Character HP =', self.chHP)
              print('Character DMG =', self.chDMG)
              print('Character SPD =', self.chSPD)
              self.Turn = 8

        elif(self.BMATKR > 4):
          self.BMATK = self.dodge
          if(self.BMATK == self.dodge):
            print('The Beast Mother dodges your attack')
            print('Character HP =', self.chHP)
            print('Character DMG =', self.chDMG)
            print('Character SPD =', self.chSPD)
            self.Turn = 8
      else:
        pass




    
    elif(self.Turn == 8):
      if(self.character == self.ulya):
        self.BMATKR = p5.random(1,5)
        if(self.BMATKR == 1):
          self.BMATK = self.bite
          if(self.BMATK == self.bite):
            self.chHP -= 30
            print('The Beast Mother bites you.')
            print('you lose 20 HP.')
            print('Character HP =', self.chHP)
            print('Character DMG =', self.chDMG)
            print('Character SPD =', self.chSPD)
            self.Turn = 9


        elif(self.BMATKR > 2):
          if(self.BMATKR < 3):
            self.BMATK = self.Hands
            if(self.BMATK == self.Hands):
              self.chHP -= 25
              print('The Beast Mothers hands squeeze your body')
              print('you lose 20 HP')
              print('Character HP =', self.chHP)
              print('Character DMG =', self.chDMG)
              print('Character SPD =', self.chSPD)
              self.Turn = 9


        elif(self.BMATKR > 3):
          if(self.BMATKR < 4):
            self.BMATK = self.CallOfTheWild
            if(self.BMATK == self.CallofTheWild):
              self.chDMG -= 10
              print('The Beast Mother Howls.')
              print('your damage decreases by 10.')
              print('Character HP =', self.chHP)
              print('Character DMG =', self.chDMG)
              print('Character SPD =', self.chSPD)
              self.Turn = 9

        elif(self.BMATKR > 4):
          self.BMATK = self.dodge
          if(self.BMATK == self.dodge):
            print('The Beast Mother dodges your attack')
            print('Character HP =', self.chHP)
            print('Character DMG =', self.chDMG)
            print('Character SPD =', self.chSPD)
            self.Turn = 9
      else:
        pass




    
    elif(self.Turn == 9):
      if(self.character == self.otto):
        self.BMATKR = p5.random(1,5)
        if(self.BMATKR == 1):
          self.BMATK = self.bite
          if(self.BMATK == self.bite):
            self.chHP -= 30
            print('The Beast Mother bites you.')
            print('you lose 20 HP.')
            print('Character HP =', self.chHP)
            print('Character DMG =', self.chDMG)
            print('Character SPD =', self.chSPD)
            self.Turn = 10



        elif(self.BMATKR > 2):
          if(self.BMATKR < 3):
            self.BMATK = self.Hands
            if(self.BMATK == self.Hands):
              self.chHP -=25
              print('The Beast Mothers hands squeeze your body')
              print('you lose 20 HP')
              print('Character HP =', self.chHP)
              print('Character DMG =', self.chDMG)
              print('Character SPD =', self.chSPD)
              self.Turn = 10


        elif(self.BMATKR > 3):
          if(self.BMATKR < 4):
            self.BMATK = self.CallOfTheWild
            if(self.BMATK == self.CallofTheWild):
              self.chDMG -= 10
              print('The Beast Mother Howls.')
              print('your damage decreases by 10.')
              print('Character HP =', self.chHP)
              print('Character DMG =', self.chDMG)
              print('Character SPD =', self.chSPD)
              self.Turn = 10


        elif(self.BMATKR > 4):
          self.BMATK = self.dodge
          if(self.BMATK == self.dodge):
            print('The Beast Mother dodges your attack')
            print('Character HP =', self.chHP)
            print('Character DMG =', self.chDMG)
            print('Character SPD =', self.chSPD)
            self.Turn = 10
      else:
        pass




    
    elif(self.Turn == 10):
      if(self.character == self.ulya):
        self.BMATKR = p5.random(1,5)
        if(self.BMATKR == 1):
          self.BMATK = self.bite
          if(self.BMATK == self.bite):
            self.chHP -= 30
            print('The Beast Mother bites you.')
            print('you lose 20 HP.')
            print('Character HP =', self.chHP)
            print('Character DMG =', self.chDMG)
            print('Character SPD =', self.chSPD)
            self.Turn = 11
            


        elif(self.BMATKR > 2):
          if(self.BMATKR < 3):
            self.BMATK = self.Hands
            if(self.BMATK == self.Hands):
              self.chHP -= 25
              print('The Beast Mothers hands squeeze your body')
              print('you lose 20 HP')
              print('Character HP =', self.chHP)
              print('Character DMG =', self.chDMG)
              print('Character SPD =', self.chSPD)
              self.Turn = 11
              


        elif(self.BMATKR > 3):
          if(self.BMATKR < 4):
            self.BMATK = self.CallOfTheWild
            if(self.BMATK == self.CallofTheWild):
              self.chDMG -= 10
              print('The Beast Mother Howls.')
              print('your damage decreases by 10.')
              print('Character HP =', self.chHP)
              print('Character DMG =', self.chDMG)
              print('Character SPD =', self.chSPD)
              self.Turn = 11

        elif(self.BMATKR > 4):
          self.BMATK = self.dodge
          if(self.BMATK == self.dodge):
            print('The Beast Mother dodges your attack')
            print('Character HP =', self.chHP)
            print('Character DMG =', self.chDMG)
            print('Character SPD =', self.chSPD)
            self.Turn = 11
      else:
        pass
        
    elif(self.Turn == 11):
      if(self.bmHP > self.chHP):
        program_state = 'LOSE'
        if(program_state == 'LOSE'):
          Ending_1.draw

      elif(self.bmHP < self.chHP):
        program_state = 'WIN'
        if(program_state == 'WIN'):
          Ending_2.draw

          
  def keyPressed(self, event):
    #print('Battle1 keyPressed.. ' + str(p5.key))
    pass
