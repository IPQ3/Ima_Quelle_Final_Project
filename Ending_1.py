import js as p5
from main import *
class Ending_1:
  def draw(self):
    global program_state
    p5.background(0)
    print('Ending 1')
    p5.fill(0,180,0)
    p5.stroke(0)
    p5.text('You have been slain.',250,230)
    p5.text('Ending 1/2',260,250) 
    p5.text('Press Mouse to Restart.',280,270)
    if(program_state == 'LOSE'):
      if(p5.mouseIsPressed == True):
        program_state = 'Start'
    else:
      pass
