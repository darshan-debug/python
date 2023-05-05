class Node:
    def __init__(self,x,leftt=None,rightt=None):
        self.val=x
        self.left=leftt
        self.right=rightt
class Tree:
    def __init__(self):
        self.root=None
    def inorder(self):
        def kk(root):
            if(root==None):
                return
            kk(root.left)
            print(root.val,end=" ")
            kk(root.right)
        kk(self.root)
        print()   
    def postorder(self):
        def kk1(root):
            if(root==None):
                return
            kk1(root.left)
            kk1(root.right)
            print(root.val,end=" ")            
        kk1(self.root)
        print() 
        print()   
    def preorder(self):
        def kk2(root):
            if(root==None):
                return
            print(root.val,end=" ")
            kk2(root.left)
            kk2(root.right)       
            
        kk2(self.root)
        print()  
    def addToBST(self,x):        
        def ff(root,x):
            if(root==None):
                return Node(x)
            if(x<root.val):
                root.left=ff(root.left,x)
            else:
                root.right=ff(root.right,x)
            return root
        if(type(x)==list):
            for i in x:
                self.root=ff(self.root,i)
            print("inorder after addition:",end=" ")
            self.inorder()
#             self.preorder()
#             self.postorder()
#             self.binarySearch(2)
#             self.binarySearch(-2)
        else:    
            self.root=ff(self.root,x)
            self.inorder()
    def binarySearch(self,x):
        def ff1(root,x):
            if(root==None):
                return False
            if(x==root.val):
                return True
            k1=k2=False
            if(x<root.val):
                k1=ff1(root.left,x)            
            else:
                k2=ff1(root.right,x)
            if(k1 or k2):
                return True
            return False
        print(ff1(self.root,x))            
                
    def deleteFromBST(self,x):
        def qq(root,x):            
            if(root==None):
                return None
            if(x==root.val):
                if(root.left==None and root.right==None):
                    return None
                if(root.left!=None and root.right==None):
                    return root.left
                elif(root.left==None and root.right!=None):
                    return root.right
                else:
                    temp=root.left
                    while(temp.right!=None):
                        temp=temp.right
                    root.val=temp.val
                    root.left=qq(root.left,temp.val)
                    return root
                    
            if(x<root.val):
                root.left=qq(root.left,x)
            else:
                root.right=qq(root.right,x)
            return root
        self.root=qq(self.root,x)
        print("after deletion of ",x)
        print("inorder:",end=" ")
        self.inorder()
        print("preorder:",end=" ")
        self.preorder()
        print("postorder:",end=" ")
        self.postorder()
if(__name__=="__main__"):
    obj=Tree()
    obj.addToBST([3,1,4,2,5,-1,4])
    obj.deleteFromBST(4)
    obj.deleteFromBST(2)
    obj.deleteFromBST(-1)
    obj.deleteFromBST(4)
    obj.deleteFromBST(5)
    obj.deleteFromBST(3)
    obj.deleteFromBST(1)
    
