import js as p5
from main import *
from Characterselect import *
#from Battle1 import *
class Ending_2():
  #print('Ending 2')
  def __init__(self):
    character_select.character
    character_select.ulya
    character_select.otto
    
  def draw(self):
    p5.background(0)
    p5.fill(0,180,0)
    p5.stroke(0)
    p5.text('With the Beast Mother slain, you hold',15,240)
    p5.text('its head in your hands. The beasts bow.',15,260)
    if(character_select.character == character_select.ulya):
      p5.text('Queen of the Beasts Ending 2/2',15,280)

    elif(character_select.character == character_select.otto):
      p5.text('Monarch of the Beasts Ending 2/2',15,280)
