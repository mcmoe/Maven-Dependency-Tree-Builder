from Tree import Tree
from Node import Node
from TreeParser import TreeParser

class TreeBuilder:
	def __init__(self, data, rootName):
		self.data = data
		self.rootName = rootName
		self.root = Node(self.rootName)
		self.tree = Tree(self.root)

	def computeLevel(self, rawNode):
		level = 1
		for c in rawNode:
			if(c == '|'):
				level = level + 1
			elif(c == '+' or c == '\\'):
				break
		return level

	def build(self):
		nodeList = TreeParser(self.data, self.rootName).parse()

		parent = self.root
		previousNode = self.root

		for rawNode in nodeList:
			level = self.computeLevel(rawNode)
			child = Node(rawNode)
			#print(str(level) + ' ' + rawNode)

			while(parent.getLevel() >= level):
				parent = parent.getParent()

			parent.addChild(child)
			parent = child

		return self.tree


def main():
	# read from dependencies.txt file
	# parse file into Tree
	# run some find and contains
	# run some print path on nodes

	jarName = "[INFO] com.mcmoe:com.mcmoe.jsikulifut13:jar:0.0.1-SNAPSHOT"
	dataFile = "zdependencies.txt"
	tree = TreeBuilder(dataFile, jarName).build()

	print(tree.toString(False))

	rawNodeText = "[INFO] |  |  +- org.antlr:stringtemplate:jar:4.0.2:compile"
	foundNode = tree.find(Node(rawNodeText))

	print(foundNode.toString(False))
	print(foundNode.buildWithChildren(False))
	print(foundNode.buildWithAncestors(False))

if __name__ == '__main__':
	main()

