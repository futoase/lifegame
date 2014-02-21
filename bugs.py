# -*- coding: UTF-8 -*-

class Bugs(object):
  count = 0 
  def __init__(self, x, y):
    self.setX(x)
    self.setY(y)
    self.setFalseLife()
    self.setNextFalse()
      
  def getNext(self):
    return self._next

  def setNextTrue(self):
    self._next = True

  def setNextFalse(self):
    self._next = False
      
  def setX(self, v):
    self.x = v

  def getX(self):
    return self.x

  def setY(self, v):
    self.y = v

  def getY(self):
    return self.y
  
  def setTrueLife(self):
    self.setLife(True)

  def setFalseLife(self):
    self.setLife(False)

  def setLife(self, v):
    self.Life = v

  def getLife(self):
    return self.Life

  def getCount(self):
    return self.count

  def incCount(self):
    self.count += 1

  def decCount(self):
    self.count -= 1

  def clearCount(self):
    self.count = 0
