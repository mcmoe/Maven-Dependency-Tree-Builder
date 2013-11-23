######### CLASS TREE  ######### 
import Node

class Tree():
	def __init__(self, root):
		self.root = root
	def getRoot(self):
		return self.root
	def contains(self, node):
		return self.root.contains(node)
	def find(self, node):
		return self.root.find(node)
	def toString(self, tabulate):
		return self.root.buildWithChildren(tabulate)
######### END OF CLASS #########