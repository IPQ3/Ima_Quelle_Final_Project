import js as p5
from main import *
CharacterSelect = p5.loadImage('Character Select.png')
class Character_Select:
  #print('select character') < This is to make sure its on
  
  def __init__(self):
    self.character = 0
    self.ulya = 2
    self.otto = 3
    program_state = 'CHARACTERSELECT'

    
  def draw(self):
    global character,program_state
    program_state = 'CHARACTERSELECT'
    p5.background(40)
    p5.image(CharacterSelect,0,0)
    p5.stroke(0,0,135)
    p5.fill(0)
    p5.rect(150,265,380,60)
    p5.stroke(255,0,0)
    p5.fill(135,0,0)
    p5.text('Ulya',65,270)
    p5.stroke(0,0,255)
    p5.fill(0,0,135)
    p5.text('Otto',205,270)
