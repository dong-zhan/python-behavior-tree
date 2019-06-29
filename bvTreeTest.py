import sys 
from bvTree import bvNode  

class bvNodeTest(bvNode) :
    def __init__(self, func):
        super(bvNode, self).__init__(func)
		
    def testAddAnimations(self):
        self.addChildLast(singleAnimation1)
        self.addChildLast(singleAnimation2)
        self.addChildLast(singleAnimation3)
        self.addChildLast(singleAnimation4) 
            
    def t(self):      
        self.removeAll()        
        self.data = singleAnimation5 
        self.testAddAnimations()       
        node = self.firstChild
        for i in range(10):
            node = node.execute(1,1)

#for test
#functions process specific part of the data only
def singleAnimation1(stateData, param):
    print('singleAnimation1', stateData, param)
    return randint(-3,1)

def singleAnimation2(stateData, param):
    print('singleAnimation2', stateData, param)
    return randint(-3,1)

def singleAnimation3(stateData, param):
    print('singleAnimation3', stateData, param)
    return randint(-3,1)

def singleAnimation4(stateData, param):
    print('singleAnimation4', stateData, param)
    return randint(-3,1) 

def singleAnimation5(stateData, param):
    print('singleAnimation5', stateData, param)
    return 3        			
