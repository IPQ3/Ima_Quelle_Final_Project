import js as p5

from Characterselect import *
from Battle1 import *
from Ending_1 import *
from Ending_2 import *

#battlestats = BattleStats()
character = 0
ulya = 2
otto = 3
character_select = Character_Select()
battle1 = Battle1()
ending_1 = Ending_1()
ending_2 = Ending_2()
ending_1 = Ending_1()

CharacterSelect = p5.loadImage('Character Select.png')
BattleBackground = p5.loadImage('Battle Background.png')

program_state = 'START'
print('program_state =', program_state)

def title():
  p5.background(0)
  p5.fill(0,0,180)
  p5.stroke(180,0,0)
  p5.textSize(17)
  p5.text('Press e to play',96,150)

    
chHP = 1
chDMG = 1
chSPD = 1

def setup():
  p5.createCanvas(300, 300)
  p5.background(0)
  p5.rectMode(p5.CENTER)


def draw():
  global character_select,program_state
  p5.background(0)
  cursor_xy = (int(p5.mouseX), int(p5.mouseY))
  #p5.text(cursor_xy, 10, 20)  # cursor (x, y) 
  #print(p5.mouseX, p5.mouseY)
  if(program_state == 'START'):
    title()
  else:
    pass
  if(battle1.bmHP == 0):
    program_state = 'WIN'
    ending_2.draw()
  else:
    pass




  
  if(program_state == 'START'):
    if(p5.keyIsPressed == True):
      if(p5.key == 'e'):
        program_state = 'CHARACTERSELECT'
        if(program_state == 'CHARACTERSELECT'):
          print('program_state =', program_state)
          character_select.draw()
    else:
      pass
  elif(program_state == 'CHARACTERSELECT'):
    character_select.draw()
    #battlestats.draw()
    if(p5.mouseIsPressed == True):
      battle1.draw()
      #battlestats.draw()

  elif(program_state == 'BATTLE1'):
    battle1.draw()
    #battle1.update()
    battle1.update(program_state)
    #battlestats.draw()
    
  elif(program_state == 'ENDING_1'):
    ending_1.draw()
  elif(program_state == 'ENDING_2'):
    ending_2.draw()

def keyPressed(event):
  print('keyPressed.. ' + str(p5.key))
  global character_select, program_state
  battle1.keyPressed(event)
    
  if(program_state == 'BATTLE1'):
    if(battle1.Turn == 1):
      #print('turn 1')
      if(battle1.character == battle1.ulya):
        if(p5.keyIsPressed == True):
          print('key is pressed')
          if(p5.key == 'l'):
            print('low attack')
            battle1.bmHP -= 30
            print('bmHP =', battle1.bmHP)
            #f(p5.keyIsPressed == True):
              #if(p5.key == ''):
            battle1.Turn = 2
            #else:
              #pass

          elif(p5.key == 'h'):
            print('high attack')
            battle1.ATKR = p5.random(1,2)
            if(battle1.ATKR >1.5):
              print('high roll')
              print('bmHP =', battle1.bmHP)
              battle1.ATK = 30
              if(battle1.ATK == 30):
                battle1.bmHP -= 30
                #f(p5.keyIsPressed == True):
                  #if(p5.key == ''):
                battle1.Turn = 2
                #else:
                  #pass
            elif(battle1.ATKR < 1.6):
              print('low roll')
              print('bmHP =', battle1.bmHP)
              battle1.ATK = 20
              if(battle1.ATK == 20):
                battle1.bmHP -= 20
                #f(p5.keyIsPressed == True):
                  #if(p5.key == ''):
                battle1.Turn = 2
                #else:
                  #pass

          elif(p5.key == 'd'):
            print('dodge')
            print('bmHP =', battle1.bmHP)
            battle1.bmHP = battle1.bmHP
            #f(p5.keyIsPressed == True):
              #if(p5.key == ''):
            battle1.Turn = 2
            #else:
              #pass

      
      elif(battle1.character == battle1.otto):
        battle1.BMATKR = p5.random(1,5)
        if(battle1.BMATKR == 1):
          battle1.BMATK = bite
          if(battle1.BMATK == bite):
            battle1.chHP -= 30
            p5.fill(0,0,180)
            p5.stroke(180,0,0)
            p5.textSize(17)
            print('The Beast Mother bites you.')
            p5.text('you lose 20 HP.',15,280)
            print('Character HP =', battle1.chHP)
            print('Character DMG =', battle1.chDMG)
            print('Character SPD =', battle1.chSPD)
            #f(p5.keyIsPressed == True):
              #if(p5.key == ''):
            battle1.Turn = 2
            #else:
              #pass


        elif(battle1.BMATKR > 2):
          if(battle1.BMATKR < 3):
            battle1.BMATK = battle1.Hands
            if(battle1.BMATK == battle1.Hands):
              battle1.chHP -=25
              print('The Beast Mothers hands squeeze your body')
              print('you lose 20 HP')
              print('Character HP =', battle1.chHP)
              print('Character DMG =', battle1.chDMG)
              print('Character SPD =', battle1.chSPD)
              #f(p5.keyIsPressed == True):
                #if(p5.key == ''):
              battle1.Turn = 2
              #else:
                #pass


        elif(battle1.BMATKR > 3):
          if(battle1.BMATKR < 4):
            battle1.BMATK = battle1.CallOfTheWild
            if(battle1.BMATK == battle1.CallofTheWild):
              battle1.chDMG -= 10
              print('The Beast Mother Howls.')
              print('your damage decreases by 10.')
              print('Character HP =', battle1.chHP)
              print('Character DMG =', battle1.chDMG)
              print('Character SPD =', battle1.chSPD)
              #f(p5.keyIsPressed == True):
                #if(p5.key == ''):
              battle1.Turn = 2
              #else:
                #pass

        elif(battle1.BMATKR > 4):
          battle1.BMATK = battle1.dodge
          if(battle1.BMATK == battle1.dodge):
            print('The Beast Mother dodges your attack')
            print('Character HP =', battle1.chHP)
            print('Character DMG =', battle1.chDMG)
            print('Character SPD =', battle1.chSPD)
            #f(p5.keyIsPressed == True):
              #if(p5.key == ''):
            battle1.Turn = 2
            #else:
              #pass
    elif(battle1.Turn == 2):
          #print('turn 1')
      if(battle1.character == battle1.otto):
        if(p5.keyIsPressed == True):
          print('key is pressed')
          if(p5.key == 'l'):
            print('low attack')
            battle1.bmHP -= 30
            print('bmHP =', battle1.bmHP)
            #if(p5.keyIsPressed == True):
              #if(p5.key == ''):
            battle1.Turn = 3
            #else:
                #pass

          elif(p5.key == 'h'):
            print('high attack')
            battle1.ATKR = p5.random(1,2)
            if(battle1.ATKR >1.5):
              print('high roll')
              print('bmHP =', battle1.bmHP)
              battle1.ATK = 30
              if(battle1.ATK == 30):
                battle1.bmHP -= 30
                print('bmHP =', battle1.bmHP)
                #f(p5.keyIsPressed == True):
                  #if(p5.key == ''):
                battle1.Turn = 3
                    #else:
                      #pass
            elif(battle1.ATKR < 1.6):
              print('low roll')
              print('bmHP =', battle1.bmHP)
              battle1.ATK = 20
              if(battle1.ATK == 20):
                battle1.bmHP -= 20
                print('bmHP =', battle1.bmHP)
                #f(p5.keyIsPressed == True):
                  #if(p5.key == ''):
                battle1.Turn = 3
                #else:
                  #pass

            elif(p5.key == 'd'):
              print('dodge')
              print('bmHP =', battle1.bmHP)
              battle1.bmHP = battle1.bmHP
              print('bmHP =', battle1.bmHP)
              #f(p5.keyIsPressed == True):
                #if(p5.key == ''):
              battle1.Turn = 3
              #else:
                #pass


    elif(battle1.Turn == 3):
      #print('turn 1')
      if(battle1.character == battle1.ulya):
        if(p5.keyIsPressed == True):
          print('key is pressed')
          if(p5.key == 'l'):
            print('low attack')
            battle1.bmHP -= 30
            print('bmHP =', battle1.bmHP)
            #f(p5.keyIsPressed == True):
              #if(p5.key == ''):
            battle1.Turn = 4
            #else:
              #pass

          elif(p5.key == 'h'):
            print('high attack')
            battle1.ATKR = p5.random(1,2)
            if(battle1.ATKR >1.5):
              print('high roll')
              print('bmHP =', battle1.bmHP)
              battle1.ATK = 30
              if(battle1.ATK == 30):
                battle1.bmHP -= 30
                #f(p5.keyIsPressed == True):
                  #if(p5.key == ''):
                battle1.Turn = 4
                #else:
                  #pass
            elif(battle1.ATKR < 1.6):
              print('low roll')
              print('bmHP =', battle1.bmHP)
              battle1.ATK = 20
              if(battle1.ATK == 20):
                battle1.bmHP -= 20
                #f(p5.keyIsPressed == True):
                  #if(p5.key == ''):
                battle1.Turn = 4
                #else:
                  #pass

          elif(p5.key == 'd'):
            print('dodge')
            print('bmHP =', battle1.bmHP)
            battle1.bmHP = battle1.bmHP
            #f(p5.keyIsPressed == True):
              #if(p5.key == ''):
            battle1.Turn = 4
            #else:
              #pass

    elif(battle1.Turn == 4):
      print('turn 4')
      if(battle1.character == battle1.otto):
        if(p5.keyIsPressed == True):
          print('key is pressed')
          if(p5.key == 'l'):
            print('low attack')
            battle1.bmHP -= 30
            print('bmHP =', battle1.bmHP)
            #if(p5.keyIsPressed == True):
              #if(p5.key == ''):
            battle1.Turn = 5
            #else:
              #pass

          elif(p5.key == 'h'):
            print('high attack')
            battle1.ATKR = p5.random(1,2)
            if(battle1.ATKR >1.5):
              print('high roll')
              print('bmHP =', battle1.bmHP)
              battle1.ATK = 30
              if(battle1.ATK == 30):
                battle1.bmHP -= 30
                print('bmHP =', battle1.bmHP)
              #f(p5.keyIsPressed == True):
                #if(p5.key == ''):
                battle1.Turn = 5
                  #else:
                    #pass
            elif(battle1.ATKR < 1.6):
              print('low roll')
              print('bmHP =', battle1.bmHP)
              battle1.ATK = 20
              if(battle1.ATK == 20):
                battle1.bmHP -= 20
                print('bmHP =', battle1.bmHP)
                #f(p5.keyIsPressed == True):
                  #if(p5.key == ''):
                battle1.Turn = 5
                #else:
                  #pass

          elif(p5.key == 'd'):
            print('dodge')
            print('bmHP =', battle1.bmHP)
            battle1.bmHP = battle1.bmHP
            print('bmHP =', battle1.bmHP)
            #f(p5.keyIsPressed == True):
              #if(p5.key == ''):
            battle1.Turn = 5
            #else:
              #pass



    elif(battle1.Turn == 5):
      #print('turn 1')
      if(battle1.character == battle1.ulya):
        if(p5.keyIsPressed == True):
          print('key is pressed')
          if(p5.key == 'l'):
            print('low attack')
            battle1.bmHP -= 30
            print('bmHP =', battle1.bmHP)
            #f(p5.keyIsPressed == True):
              #if(p5.key == ''):
            battle1.Turn = 6
            #else:
              #pass

          elif(p5.key == 'h'):
            print('high attack')
            battle1.ATKR = p5.random(1,2)
            if(battle1.ATKR >1.5):
              print('high roll')
              print('bmHP =', battle1.bmHP)
              battle1.ATK = 30
              if(battle1.ATK == 30):
                battle1.bmHP -= 30
                #f(p5.keyIsPressed == True):
                  #if(p5.key == ''):
                battle1.Turn = 6
                #else:
                  #pass
            elif(battle1.ATKR < 1.6):
              print('low roll')
              print('bmHP =', battle1.bmHP)
              battle1.ATK = 20
              if(battle1.ATK == 20):
                battle1.bmHP -= 20
                #f(p5.keyIsPressed == True):
                  #if(p5.key == ''):
                battle1.Turn = 6
                #else:
                  #pass

          elif(p5.key == 'd'):
            print('dodge')
            print('bmHP =', battle1.bmHP)
            battle1.bmHP = battle1.bmHP
            #f(p5.keyIsPressed == True):
              #if(p5.key == ''):
            battle1.Turn = 6
            #else:
              #pass

    elif(battle1.Turn == 6):
        #print('turn 1')
      if(battle1.character == battle1.otto):
        if(p5.keyIsPressed == True):
          print('key is pressed')
          if(p5.key == 'l'):
            print('low attack')
            battle1.bmHP -= 30
            print('bmHP =', battle1.bmHP)
            #if(p5.keyIsPressed == True):
              #if(p5.key == ''):
            battle1.Turn = 7
            #else:
              #pass

          elif(p5.key == 'h'):
            print('high attack')
            battle1.ATKR = p5.random(1,2)
            if(battle1.ATKR >1.5):
              print('high roll')
              print('bmHP =', battle1.bmHP)
              battle1.ATK = 30
              if(battle1.ATK == 30):
                battle1.bmHP -= 30
                print('bmHP =', battle1.bmHP)
                #f(p5.keyIsPressed == True):
                  #if(p5.key == ''):
                battle1.Turn = 7
                  #else:
                    #pass
            elif(battle1.ATKR < 1.6):
              print('low roll')
              print('bmHP =', battle1.bmHP)
              battle1.ATK = 20
              if(battle1.ATK == 20):
                battle1.bmHP -= 20
                print('bmHP =', battle1.bmHP)
                #f(p5.keyIsPressed == True):
                  #if(p5.key == ''):
                battle1.Turn = 7
                #else:
                  #pass

          elif(p5.key == 'd'):
            print('dodge')
            print('bmHP =', battle1.bmHP)
            battle1.bmHP = battle1.bmHP
            print('bmHP =', battle1.bmHP)
            #f(p5.keyIsPressed == True):
              #if(p5.key == ''):
            battle1.Turn = 7
            #else:
              #pass


    elif(battle1.Turn == 7):
    #print('turn 1')
      if(battle1.character == battle1.ulya):
        if(p5.keyIsPressed == True):
          print('key is pressed')
          if(p5.key == 'l'):
            print('low attack')
            battle1.bmHP -= 30
            print('bmHP =', battle1.bmHP)
            #f(p5.keyIsPressed == True):
            #if(p5.key == ''):
            battle1.Turn = 8
            #else:
              #pass

          elif(p5.key == 'h'):
            print('high attack')
            battle1.ATKR = p5.random(1,2)
            if(battle1.ATKR >1.5):
              print('high roll')
              print('bmHP =', battle1.bmHP)
              battle1.ATK = 30
              if(battle1.ATK == 30):
                battle1.bmHP -= 30
                #f(p5.keyIsPressed == True):
                #if(p5.key == ''):
                battle1.Turn = 8
                #else:
                #pass
            elif(battle1.ATKR < 1.6):
              print('low roll')
              print('bmHP =', battle1.bmHP)
              battle1.ATK = 20
              if(battle1.ATK == 20):
                battle1.bmHP -= 20
                #f(p5.keyIsPressed == True):
                #if(p5.key == ''):
                battle1.Turn = 8
              #else:
                #pass

          elif(p5.key == 'd'):
            print('dodge')
            print('bmHP =', battle1.bmHP)
            battle1.bmHP = battle1.bmHP
          #f(p5.keyIsPressed == True):
            #if(p5.key == ''):
            battle1.Turn = 8
          #else:
            #pass


    elif(battle1.Turn == 8):
      #print('turn 1')
      if(battle1.character == battle1.otto):
        if(p5.keyIsPressed == True):
          print('key is pressed')
          if(p5.key == 'l'):
            print('low attack')
            battle1.bmHP -= 30
            print('bmHP =', battle1.bmHP)
            #if(p5.keyIsPressed == True):
              #if(p5.key == ''):
            battle1.Turn = 9
          #else:
              #pass

          elif(p5.key == 'h'):
            print('high attack')
            battle1.ATKR = p5.random(1,2)
            if(battle1.ATKR >1.5):
              print('high roll')
              print('bmHP =', battle1.bmHP)
              battle1.ATK = 30
              if(battle1.ATK == 30):
                battle1.bmHP -= 30
                print('bmHP =', battle1.bmHP)
                #f(p5.keyIsPressed == True):
                  #if(p5.key == ''):
                battle1.Turn = 9
                  #else:
                    #pass
            elif(battle1.ATKR < 1.6):
              print('low roll')
              print('bmHP =', battle1.bmHP)
              battle1.ATK = 20
              if(battle1.ATK == 20):
                battle1.bmHP -= 20
                print('bmHP =', battle1.bmHP)
                #f(p5.keyIsPressed == True):
                  #if(p5.key == ''):
                battle1.Turn = 9
                #else:
                  #pass

          elif(p5.key == 'd'):
            print('dodge')
            print('bmHP =', battle1.bmHP)
            battle1.bmHP = battle1.bmHP
            print('bmHP =', battle1.bmHP)
            #f(p5.keyIsPressed == True):
              #if(p5.key == ''):
            battle1.Turn = 9
            #else:
              #pass

    elif(battle1.Turn == 9):
      #print('turn 1')
      if(battle1.character == battle1.ulya):
        if(p5.keyIsPressed == True):
          if(p5.key == 'l'):
            print('low attack')
            battle1.bmHP -= 30
            print('bmHP =', battle1.bmHP)
            battle1.Turn = 10
            

          elif(p5.key == 'h'):
            print('high attack')
            battle1.ATKR = p5.random(1,2)
            if(battle1.ATKR >1.5):
              print('high roll')
              print('bmHP =', battle1.bmHP)
              battle1.ATK = 30
              if(battle1.ATK == 30):
                battle1.bmHP -= 30
                battle1.Turn = 10
              
            elif(battle1.ATKR < 1.6):
              print('low roll')
              print('bmHP =', battle1.bmHP)
              battle1.ATK = 20
              if(battle1.ATK == 20):
                battle1.bmHP -= 20
                battle1.Turn = 10

          elif(p5.key == 'd'):
            print('dodge')
            print('bmHP =', battle1.bmHP)
            battle1.bmHP = battle1.bmHP
            battle1.Turn = 10

    elif(battle1.Turn == 10):
    #print('turn 1')
      if(battle1.character == battle1.otto):
        if(p5.keyIsPressed == True):
          print('key is pressed')
          if(p5.key == 'l'):
            print('low attack')
            battle1.bmHP -= 30
            print('bmHP =', battle1.bmHP)
            if(battle1.bmHP > battle1.chHP):
              program_state = 'LOSE'
              Ending_1()
            elif(battle1.bmHP < battle1.chHP):
              program_state = 'WIN'
              Ending_2()
          
          elif(p5.key == 'h'):
            print('high attack')
            battle1.ATKR = p5.random(1,2)
            if(battle1.ATKR >1.5):
              print('high roll')
              print('bmHP =', battle1.bmHP)
              battle1.ATK = 30
              if(battle1.ATK == 30):
                battle1.bmHP -= 30
                print('bmHP =', battle1.bmHP)
                if(battle1.bmHP > battle1.chHP):
                  program_state = 'LOSE'
                  Ending_1()
                elif(battle1.bmHP < battle1.chHP):
                  program_state = 'WIN'
                  Ending_2()
              
            elif(battle1.ATKR < 1.6):
              print('low roll')
              print('bmHP =', battle1.bmHP)
              battle1.ATK = 20
              if(battle1.ATK == 20):
                battle1.bmHP -= 20
                print('bmHP =', battle1.bmHP)
                if(battle1.bmHP > battle1.chHP):
                  program_state = 'LOSE'
                  Ending_1()
                elif(battle1.bmHP < battle1.chHP):
                  program_state = 'WIN'
                  Ending_2()
              

          elif(p5.key == 'd'):
            print('dodge')
            print('bmHP =', battle1.bmHP)
            battle1.bmHP = battle1.bmHP
            print('bmHP =', battle1.bmHP)
            if(battle1.bmHP > battle1.chHP):
              program_state = 'LOSE'
              Ending_1()
            elif(battle1.bmHP < battle1.chHP):
              program_state = 'WIN'
              Ending_2()
          


def keyReleased(event):
  #print('keyReleased.. ' + str(p5.key))
  pass

def mousePressed(event):
  #print('mousePressed..')
  global program_state
  if(program_state == 'CHARACTERSELECT'):
    if(p5.mouseX > 100 and p5.mouseX < 200):
      character_select.character = character_select.ulya
      program_state = 'BATTLE1'
      print('change program_state to', program_state)
      battle1.draw()
      print('Character = Ulya')
      character_select.chHP = 150
      character_select.chDMG = 30
      character_select.chSPD = 50
      print('Character HP =', battle1.chHP)
      print('Character DMG =', battle1.chDMG)
      print('Character SPD =', battle1.chSPD)

    elif(p5.mouseX > 200 and p5.mouseX < 300):
      character_select.character = character_select.otto
      program_state = 'BATTLE1'
      print('change program_state to', program_state)
      battle1.draw()
      print('Character = Otto')
      character_select.chHP = 150
      character_select.chDMG = 30
      character_select.chSPD = 30
      print('Character HP =', battle1.chHP)
      print('Character DMG =', battle1.chDMG)
      print('Character SPD =', battle1.chSPD)

def mouseReleased(event):
  #print('mouseReleased..')
  pass
