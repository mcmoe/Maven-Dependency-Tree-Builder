from Tree import Tree
from Node import Node
from TreeParser import TreeParser
from TreeBuilder import TreeBuilder
import unittest

class TestNode():
		def __init__(self, data):
			self.data = data


class Test(unittest.TestCase):
	def setUp(self):
		self.rootData = "hello world"
		self.root = Node(self.rootData)
		self.tree = Tree(self.root)

	def testRoot(self):
		self.assertEqual(self.root, self.tree.getRoot())

	def testRootData(self):
		rootData = self.tree.getRoot().getData()
		self.assertEqual(self.rootData, rootData)

	def testContainsRootByReference(self):
		self.assertTrue(self.tree.contains(self.root))

	def testContainsNodeWithRootData(self):
		self.assertTrue(self.tree.contains(Node("hello world")))

	def testContainsNonExistingNode(self):
		self.assertFalse(self.tree.contains(Node("hello world!")))

	def testContainsNonNode(self):
		self.assertFalse(self.tree.contains(TestNode("hello world")))

	def testContainsChildNode(self):
		root = self.tree.getRoot()

		child1 = Node("child1")
		child2 = Node("child2")
		child3 = Node("child3")
		
		root.addChild(child1)
		root.addChild(child2)

		self.assertTrue(self.tree.contains(child1))
		self.assertTrue(self.tree.contains(child2))
		self.assertFalse(self.tree.contains(child3))

	def testContainsGrandChildNode(self):
		root = self.tree.getRoot()

		child1 = Node("child1")
		child2 = Node("child2")
		grandChild1 = Node("grandChild1")
		grandChild2 = Node("grandChild2")
		grandChild3 = Node("grandChild3")
		
		root.addChild(child1)
		root.addChild(child2)
		child1.addChild(grandChild1)
		child2.addChild(grandChild2)

		self.assertTrue(self.tree.contains(grandChild1))
		self.assertTrue(self.tree.contains(grandChild2))
		self.assertFalse(self.tree.contains(grandChild3))

	def testContainsDescendantNodes(self):
		root = self.tree.getRoot()

		child1 = Node("child1")
		child2 = Node("child2")
		child3 = Node("child3")
		grandChild1 = Node("grandChild1")
		grandChild11 = Node("grandChild11")
		grandChild2 = Node("grandChild2")
		grandChild22 = Node("grandChild22")
		descendant1 = Node("descendant1")
		descendant11 = Node("descendant11")
		descendant2 = Node("descendant2")
		descendant22 = Node("descendant22")
		descendant3 = Node("descendant3")
		
		root.addChild(child1)
		root.addChild(child2)
		root.addChild(child3)
		child1.addChild(grandChild1)
		child2.addChild(grandChild2)
		grandChild1.addChild(descendant1)
		grandChild1.addChild(descendant11)
		grandChild2.addChild(descendant2)
		grandChild2.addChild(descendant22)
		


		self.assertTrue(self.tree.contains(Node("descendant1")))
		self.assertTrue(self.tree.contains(Node("descendant11")))
		self.assertTrue(self.tree.contains(Node("descendant2")))
		self.assertTrue(self.tree.contains(Node("descendant22")))
		self.assertFalse(self.tree.contains(descendant3))

	def testFindRootByReference(self):
		self.assertEquals(self.root, self.tree.find(self.root))

	def testFindNodeWithRootData(self):
		node = Node("hello world")
		self.assertEquals(self.root, self.tree.find(node))

	def testFindNonExistingNode(self):
		self.assertEquals(None, self.tree.find(Node("hello world!")))

	def testFindNonNode(self):
		nonNode = TestNode("hello world")
		self.assertEquals(None, self.tree.find(nonNode))

	def testFindChildNode(self):
		root = self.tree.getRoot()

		child1 = Node("child1")
		child2 = Node("child2")
		child3 = Node("child3")
		
		root.addChild(child1)
		root.addChild(child2)

		foundC1 = self.tree.find(child1)
		foundC2 = self.tree.find(child2)
		self.assertEquals(child1, foundC1)
		self.assertEquals(child2, foundC2)
		self.assertEquals("child1", foundC1.getData())
		self.assertEquals("child2", foundC2.getData())
		self.assertEquals(None, self.tree.find(child3))

	def testFindGrandChildNode(self):
		root = self.tree.getRoot()

		child1 = Node("child1")
		child2 = Node("child2")
		grandChild1 = Node("grandChild1")
		grandChild2 = Node("grandChild2")
		grandChild3 = Node("grandChild3")
		
		root.addChild(child1)
		root.addChild(child2)
		child1.addChild(grandChild1)
		child2.addChild(grandChild2)
		
		foundGC1 = self.tree.find(grandChild1)
		foundGC2 = self.tree.find(grandChild2)

		self.assertEquals("grandChild1", foundGC1.getData())
		self.assertEquals("grandChild2", foundGC2.getData())
		self.assertEquals(None, self.tree.find(grandChild3))

	def testFindDescendantNodes(self):
		root = self.tree.getRoot()

		child1 = Node("child1")
		child2 = Node("child2")
		child3 = Node("child3")
		grandChild1 = Node("grandChild1")
		grandChild11 = Node("grandChild11")
		grandChild2 = Node("grandChild2")
		grandChild22 = Node("grandChild22")
		descendant1 = Node("descendant1")
		descendant11 = Node("descendant11")
		descendant2 = Node("descendant2")
		descendant22 = Node("descendant22")
		descendant3 = Node("descendant3")
		
		root.addChild(child1)
		root.addChild(child2)
		root.addChild(child3)
		child1.addChild(grandChild1)
		child2.addChild(grandChild2)
		grandChild1.addChild(descendant1)
		grandChild1.addChild(descendant11)
		grandChild2.addChild(descendant2)
		grandChild2.addChild(descendant22)

		foundD1 = self.tree.find(Node("descendant1"))
		foundD11 = self.tree.find(Node("descendant11"))
		foundD2 = self.tree.find(Node("descendant2"))
		foundD22 = self.tree.find(Node("descendant22"))

		self.assertEquals(descendant1.getData(), foundD1.getData())
		self.assertEquals(descendant11.getData(), foundD11.getData())

		self.assertEquals(descendant2.getData(), foundD2.getData())
		self.assertEquals(descendant22.getData(), foundD22.getData())

		self.assertEquals(None, self.tree.find(descendant3))


	def testTreeToString(self):
		root = self.tree.getRoot()

		child1 = Node("child1")
		child2 = Node("child2")
		child3 = Node("child3")
		grandChild1 = Node("grandChild1")
		grandChild11 = Node("grandChild11")
		grandChild2 = Node("grandChild2")
		grandChild22 = Node("grandChild22")
		descendant1 = Node("descendant1")
		descendant11 = Node("descendant11")
		descendant2 = Node("descendant2")
		descendant22 = Node("descendant22")
		descendant3 = Node("descendant3")
		
		root.addChild(child1)
		root.addChild(child2)
		root.addChild(child3)
		child1.addChild(grandChild1)
		child2.addChild(grandChild2)
		grandChild1.addChild(descendant1)
		grandChild1.addChild(descendant11)
		grandChild2.addChild(descendant2)
		grandChild2.addChild(descendant22)

		expectedString = (	"0 hello world\n"
							"1   child1\n"
							"2     grandChild1\n"
							"3       descendant1\n"
							"3       descendant11\n"
							"1   child2\n"
							"2     grandChild2\n"
							"3       descendant2\n"
							"3       descendant22\n"
							"1   child3\n")

		self.assertEquals(expectedString, self.tree.toString(True))

	def testFoundNodeBuildWithAncestors(self):
		root = self.tree.getRoot()

		child1 = Node("child1")
		child2 = Node("child2")
		child3 = Node("child3")
		grandChild1 = Node("grandChild1")
		grandChild11 = Node("grandChild11")
		grandChild2 = Node("grandChild2")
		grandChild22 = Node("grandChild22")
		descendant1 = Node("descendant1")
		descendant11 = Node("descendant11")
		descendant2 = Node("descendant2")
		descendant22 = Node("descendant22")
		descendant3 = Node("descendant3")
		
		root.addChild(child1)
		root.addChild(child2)
		root.addChild(child3)
		child1.addChild(grandChild1)
		child2.addChild(grandChild2)
		grandChild1.addChild(descendant1)
		grandChild1.addChild(descendant11)
		grandChild2.addChild(descendant2)
		grandChild2.addChild(descendant22)

		foundNode = self.tree.find(Node("descendant22"))

		expectedString = (	"0 hello world\n"
							"1   child2\n"
							"2     grandChild2\n"
							"3       descendant22\n")

		self.assertEquals(expectedString, foundNode.buildWithAncestors(True))

	def testFoundNodeBuildWithChildren(self):
		root = self.tree.getRoot()

		child1 = Node("child1")
		child2 = Node("child2")
		child3 = Node("child3")
		grandChild1 = Node("grandChild1")
		grandChild11 = Node("grandChild11")
		grandChild2 = Node("grandChild2")
		grandChild22 = Node("grandChild22")
		descendant1 = Node("descendant1")
		descendant11 = Node("descendant11")
		descendant2 = Node("descendant2")
		descendant22 = Node("descendant22")
		descendant3 = Node("descendant3")

		
		root.addChild(child1)
		root.addChild(child2)
		root.addChild(child3)
		child1.addChild(grandChild1)
		child2.addChild(grandChild2)
		grandChild1.addChild(descendant1)
		grandChild1.addChild(descendant11)
		grandChild2.addChild(descendant2)
		grandChild2.addChild(descendant22)

		foundNode = self.tree.find(Node("child2"))

		expectedString = (	"1   child2\n"
							"2     grandChild2\n"
							"3       descendant2\n"
							"3       descendant22\n")

		self.assertEquals(expectedString, foundNode.buildWithChildren(True))

	def testTreeParser(self):
		jarName = "[INFO] com.mcmoe:com.mcmoe.jsikulifut13:jar:0.0.1-SNAPSHOT"
		dataFile = "zdependencies.txt"
		nodeList = TreeParser(dataFile, jarName).parse()
		
		self.assertEquals(30, len(nodeList))
		self.assertEquals("[INFO] +- org.sikuli:sikuli-api:jar:1.0.2:compile", nodeList[0])
		self.assertEquals("[INFO] \- asprise:asprise-ocr:jar:4.0.0:compile", nodeList[29])
		

	def testTreeBuilder(self):
		jarName = "[INFO] com.mcmoe:com.mcmoe.jsikulifut13:jar:0.0.1-SNAPSHOT"
		dataFile = "zdependencies.txt"
		tree = TreeBuilder(dataFile, jarName).build()

		rootData = tree.getRoot().getData()
		self.assertEquals(jarName, rootData)

		firstNode = tree.find(Node("[INFO] +- org.sikuli:sikuli-api:jar:1.0.2:compile"))
		lastNode = tree.find(Node("[INFO] \- asprise:asprise-ocr:jar:4.0.0:compile"))
		self.assertTrue(firstNode)
		self.assertTrue(lastNode)
		self.assertEquals(1, firstNode.getLevel())
		self.assertEquals(1, lastNode.getLevel())
		#print(tree.toString(False))

		rawNodeText = "[INFO] |  |  +- org.antlr:stringtemplate:jar:4.0.2:compile"
		foundNode = tree.find(Node(rawNodeText))
		self.assertTrue(foundNode)
		self.assertEquals(rawNodeText, foundNode.getData())
		self.assertEquals("3 " + rawNodeText + '\n', foundNode.toString(False))

		ancestors = foundNode.buildWithAncestors(False)
		expectedAncestors=( "0 [INFO] com.mcmoe:com.mcmoe.jsikulifut13:jar:0.0.1-SNAPSHOT\n"
							"1 [INFO] +- org.sikuli:sikuli-api:jar:1.0.2:compile\n"
							"2 [INFO] |  +- org.sikuli:sikuli-core:jar:1.0.1:compile\n"
							"3 [INFO] |  |  +- org.antlr:stringtemplate:jar:4.0.2:compile\n")
		self.assertEquals(expectedAncestors, ancestors)

		children = foundNode.buildWithChildren(False)
		expectedChildren = ("3 [INFO] |  |  +- org.antlr:stringtemplate:jar:4.0.2:compile\n"
							"4 [INFO] |  |  |  +- (org.antlr:stringtemplate:jar:3.2.1:compile - omitted for cycle)\n"
							"4 [INFO] |  |  |  \\- org.antlr:antlr-runtime:jar:3.3:compile\n")
		self.assertEquals(expectedChildren, children)

if __name__ == '__main__':
	#unittest.main()
	suite = unittest.TestLoader().loadTestsFromTestCase(Test)
	unittest.TextTestRunner(verbosity=2).run(suite)