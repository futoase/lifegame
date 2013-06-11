#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import lifegame

def testLifeGame():
    count = 0
    life = lifegame.LifeGame()
    life.setX(20)
    life.setY(20)
    life.createBugField()
    life.field[(5,5)].setTrueLife()
    life.field[(6,4)].setTrueLife()
    life.field[(7,4)].setTrueLife()
    life.field[(7,5)].setTrueLife()
    life.field[(7,6)].setTrueLife()
    while count < 100:
        time.sleep(0.3)
        print 'step: %05d' % count
        for x in range(life.getX()):
            for y in range(life.getY()):
                if life.field[(x,y)].getLife():
                    print '*',
                else:
                    print '-',
            print '\n',
        [life.checkDeadOrAlive(n,m)
         for n in range(life.getX())
         for m in range(life.getY())]
        life.setBugsLife()
        count += 1
        
if __name__ == '__main__':
    testLifeGame()
