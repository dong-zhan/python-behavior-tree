#1, there are two types of node in a behavior tree, flow node and action node
#2, flow node is something like the node in neural system, or iNode in a tree
#3, action node is like cell or leave node.
#4, control, the root node should be the human brain, the ultimate flow node/fall back node.
#5, 

import sys 
from naryTree3 import naryNode3   

#from enum import 

#trying to define enumeration.
class BvNodeTypes:
    def __init__(self) :
        self.selector = 0
        self.action = 1
        self.repeat = 2
        
bvNodeTypes = BvNodeTypes()

def dispRepeat(node):           #dispatch repeat
    #print('dispRepeat')
    return node
    
def dispPrev(node):
    #print('dispPrev')
    prev = node.prev
    if prev == None:
        prev = node.parent.lastChild
    return prev
    
def dispNext(node):
    #print('dispNext')
    next = node.next
    if next == None:
        next = node.parent.firstChild
    return next
    
def dispParent(node):
    #print('dispParent')
    return node.parent
    
def dispRandomChild(node):
    #print('dispRandomChild')
    return node.getRandomChildNode()
    
def dispFindClosestSelector(node):
    while not node.parent.data.data['type'] == bvNodeTypes.selector :
        node = node.parent

bvDispatch = {
    #0: not done,
    -3 : dispRepeat,
    -1 : dispPrev,
    1 : dispNext,
    -2: dispParent,     #if the leaf node is not responsible for 'flow control', just return -2 to let 'flow' be controlled by parent.
    3: dispRandomChild,
    4: dispFindClosestSelector,
}   
    
def getDispatchNode(i, node):
    return bvDispatch[i](node)

#why is bvData needed, because naryNodes has only one member data.
#why can't data/proc be put in bvNode? consistency?     -> because this bvNOde is just a shell, everything is in naryNode3
#and in naryNode3, it's needed for generalization
class bvData:
    def __init__(self, func, data):
        self.data = data
        self.func = func
                
class bvNode(naryNode3) :
    def __init__(self, func):   #this should be called data, not func????
        super(bvNode, self).__init__(func)
        
    def newNode(self, data):
        return bvNode(data)

    #execute() can be customized.
    def execute(self, param):
        bvNode = self  #TODO: can self be used?
        while 1:
            ret = bvNode.data.func(bvNode.data.data, param)  #bvNode.data is process
            if ret == 0:  
                return bvNode
            #print('ret = ', ret)
            bvNode = getDispatchNode(ret, bvNode)  #this node is already not bvNode but naryNode3

    def execute2(self, param1, param2):
        bvNode = self  #TODO: can self be used?
        while 1:
            ret = bvNode.data.func(bvNode.data.data, param1, param2)  #bvNode.data is process
            if ret == 0:  
                return bvNode
            #print('ret = ', ret)
            bvNode = getDispatchNode(ret, bvNode)   
            
    def execute3(self, param1, param2, param3):
        bvNode = self  #TODO: can self be used?
        while 1:
            ret = bvNode.data.func(bvNode.data.data, param1, param2, param3)  #bvNode.data is process
            if ret == 0:  
                return bvNode
            #print('ret = ', ret)
            bvNode = getDispatchNode(ret, bvNode)   
            
