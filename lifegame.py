# -*- coding: utf-8 -*- 
# Life Game

import traceback
import sys
import bugs

class LifeGame(object):
  field = {}
  def __init__(self):
    pass

  def setField(self, v):
    self.field = v

  def createBugField(self):
    for x in range(self.getX()):
      for y in range(self.getY()):
        self.field[(x,y)] = bugs.Bugs(x,y)
      
  def setX(self, v):
    self.x = v

  def getX(self):
    return self.x
  
  def getXMaxRange(self):
    return self.getX()-1

  def setY(self, v):
    self.y = v

  def getY(self):
    return self.y

  def getYMaxRange(self):
    return self.getY()-1

  def checkDeadOrAlive(self, x, y):
    count = 0
    position = (self.checklefl(x,y),          
                self.checkrigl(x,y),
                self.checktopl(x,y),
                self.checkbotl(x,y),
                self.checkrigtl(x,y),
                self.checkrigbl(x,y),
                self.checkleftl(x,y),
                self.checklefbl(x,y))

    for tx,ty in position:
      if self.checkFieldLife(tx,ty):
        self.field[(x,y)].incCount()
  
    if (self.field[(x,y)].getCount() in (2,3) and
        self.field[(x,y)].getLife()):
      self.field[(x,y)].setNextTrue()

    elif (self.field[(x,y)].getCount() == 3 and
          not self.field[(x,y)].getLife()):
      self.field[(x,y)].setNextTrue()

    else:
      self.field[(x,y)].setNextFalse()

    self.field[(x,y)].clearCount()

  def setBugsLife(self):
    for x in range(self.getX()):
      for y in range(self.getY()):
        if self.field[(x,y)].getNext():
          self.field[(x,y)].setTrueLife()
        else:
          self.field[(x,y)].setFalseLife()
          self.field[(x,y)].setNextFalse()

  def checklefl(self, x, y):
    if x == 0:
      lefl = (self.getXMaxRange(),
              self.field[(x,y)].getY())
    else:
      lefl = (self.field[(x,y)].getX()-1,
              self.field[(x,y)].getY())

    return lefl
  
  def checkrigl(self, x, y):
    if x == self.getXMaxRange():
      rigl = (0,
              self.field[(x,y)].getY())
    else:
      rigl = (self.field[(x,y)].getX()+1,
              self.field[(x,y)].getY())

    return rigl            

  def checktopl(self, x, y):
    if y == 0:
      topl = (self.field[(x,y)].getX(),
              self.getYMaxRange())
    else:
      topl = (self.field[(x,y)].getX(),
              self.field[(x,y)].getY()-1)

    return topl
  
  def checkbotl(self, x, y):
    if y == self.getYMaxRange():
      botl = (self.field[(x,y)].getX(),
              0)
    else:
      botl = (self.field[(x,y)].getX(),
              self.field[(x,y)].getY()+1)
    return botl
  
  def checkrigtl(self, x, y):
    if (x == self.getXMaxRange() and
        y == 0):
      rigtl = (0, self.getYMaxRange())
    elif (x == self.getXMaxRange() and
          y > 0):
      rigtl = (0,
               self.field[(x,y)].getY()-1)
    elif (x < self.getXMaxRange() and
          y == 0):
      rigtl = (self.field[(x,y)].getX()+1,
              self.getYMaxRange())
    else:
      rigtl = (self.field[(x,y)].getX()+1,
               self.field[(x,y)].getY()-1)

    return rigtl

  def checkrigbl(self, x, y):
    if (x == self.getXMaxRange() and
        y == self.getYMaxRange()):
      rigbl = (0,0)
    elif (x == self.getXMaxRange() and
          y < self.getYMaxRange()):
      rigbl = (0,
               self.field[(x,y)].getY()+1)
    elif (x < self.getXMaxRange() and
          y == self.getYMaxRange()):
      rigbl = (self.field[(x,y)].getX()+1,
               0)
    else:
      rigbl = (self.field[(x,y)].getX()+1,
               self.field[(x,y)].getY()+1)
    return rigbl

  def checkleftl(self, x, y):
    if (x == 0 and
        y == 0):
      leftl = (self.getXMaxRange(),
               self.getYMaxRange())
    elif (x == 0 and
          y > 0):
      leftl = (self.getXMaxRange(),
               self.field[(x,y)].getY()-1)
    elif (x > 0 and
          y == 0):
      leftl = (self.field[(x,y)].getX()-1,
               self.getYMaxRange())
    else:
      leftl = (self.field[(x,y)].getX()-1,
               self.field[(x,y)].getY()-1)
    return leftl
  
  def checklefbl(self, x, y):
    if (x == 0 and
        y == self.getYMaxRange()):
      lefbl = (self.getXMaxRange(),
               0)
    elif (x == 0 and
          y < self.getYMaxRange()):
      lefbl = (self.getXMaxRange(),
               self.field[(x,y)].getY()+1)
    elif (x > 0 and
          y == self.getYMaxRange()):
      lefbl = (self.field[(x,y)].getX()-1,
               0)
    else:
      lefbl = (self.field[(x,y)].getX()-1,
               self.field[(x,y)].getY()+1)
        
    return lefbl
      
  def checkFieldLife(self, x, y):
    try:
      return self.field[(x,y)].getLife()
    except KeyError, e:
      print(e.args[0])
      traceback.print_exc(file=sys.stdout)

  def checkFieldNext(self, x, y):
    try:
      return self.field[(x,y)].getNext()
    except KeyError, e:
      print(e.args[0])
      traceback.print_exc(file=sys.stdout)
