import sys 
from naryTree3 import naryNode3   

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
    -2: dispParent,		#if the leaf node is not responsible for 'flow control', just return -2 to let 'flow' be controlled by parent.
    3: dispRandomChild
}   
    
def getDispatchNode(i, node):
    return bvDispatch[i](node)
    
class bvNode(naryNode3) :
    def __init__(self, func):
        super(bvNode, self).__init__(func)
        
    def newNode(self, data):
        return bvNode(data)

    #execute() can be customized.
    def execute(self, data, param):
        bvNode = self  #TODO: can self be used?
        while 1:
            ret = bvNode.data(data, param)  #bvNode.data is process
            if ret == 0:  
                return bvNode
            #print('ret = ', ret)
            bvNode = getDispatchNode(ret, bvNode)

