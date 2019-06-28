#*, bvNode execute/run a node(because node itself is just a function), then depending on the return value, jump/move/stay to next/prev/another node then execute/run that node.
#1, bvNode data has two parts, function and children //object state is passed to 'function' as parameter.
#2, function returns specific value to indicate which node to be executed next, another words to control the flow
#3, according to tree structure, this type of "behavior tree" takes advantage of 
#   a, the "tree branches", tree branches can be used as selector.
#   b, tree parent/child hierarchy
#4, somehow I feel neural network will be used as a new type of "neural behavior network"
#5, what about using graph to make "behavior graph", at each inode, there are many choices too.
#6, behavior tree joins animation controller to form smooth animations

import sys 
import naryTree3.py     

#from enum import 

def dispRepeat(node):
    print('dispRepeat')
    return node
    
def dispPrev(node):
    print('dispPrev')
    prev = node.prev
    if prev == None:
        prev = node.parent.lastChild
    return prev
    
def dispNext(node):
    print('dispNext')
    next = node.next
    if next == None:
        next = node.parent.firstChild
    return next
    
def dispParent(node):
    print('dispParent')
    return node.parent
    
def dispRandomChild(node):
    print('dispRandomChild')
    return node.getRandomChildNode()

bvDispatch = {
    #0: not done,
    -3 : dispRepeat,
    -1 : dispPrev,
    1 : dispNext,
    -2: dispParent,
    3: dispRandomChild
}   
    
def getDispatchNode(i, node):
    return bvDispatch[i](node)
    
class bvNode(naryNode3) :
    def __init__(self, func):
        super(bvNode, self).__init__(func)
        
    def newNode(self, data):
        return bvNode(data)

    def execute(self, data, param):
        bvNode = self  #TODO: can self be used?
        while 1:
            ret = bvNode.data(data, param)
            if ret == 0:  
                return bvNode
            #print('ret = ', ret)
            bvNode = getDispatchNode(ret, bvNode)
    
	################## test begin #############################
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
	################## test end #############################
        
        



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
