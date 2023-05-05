#leetcode daily challenge: day 17
# trie data structure- autocomplete, spell checker,prefix matching
class TrieNode:
    def __init__(self):
        self.links=[None]*26   #since there r 26 chars
        self.isEnd=False
    def containsKey(self,ch):
        return self.links[ord(ch)-ord('a')]!=None
    def put(self,ch,node): #ch is a char, node is a TrieNode obj
        self.links[ord(ch)-ord('a')]=node
    def get(self,ch):
        return self.links[ord(ch)-ord('a')]
    def setEnd(self):
        self.isEnd=True
    def isEnd(self):
        return self.isEnd



class Trie:
    

    def __init__(self):
        self.root=TrieNode()
        

    def insert(self, word: str) -> None:
        node=self.root
        for i in word:
            if(node.containsKey(i)==False):
                node.put(i,TrieNode())
            node=node.get(i)
        node.setEnd()
        
    def searchPrefix(self,word):
        node=self.root
        for i in word:
            if(node.containsKey(i)):
                node=node.get(i)
            else:
                return None
        return node

    def search(self, word: str) -> bool:
        node=self.searchPrefix(word)
        if(node!=None):
            if(node.isEnd==True):
                return True
            return False
        return False
        
        

    def startsWith(self, prefix: str) -> bool:
        node=self.searchPrefix(prefix)
        return (node!=None)
        
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)