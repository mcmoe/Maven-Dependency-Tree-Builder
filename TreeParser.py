class TreeParser:
	def __init__(self, data, jarName):
		self.data = data
		self.rootName = jarName

	def parse(self):
		treeStart = self.rootName
		treeEnd = "[INFO] ------------------------------------------------------------------------"

		with open(self.data) as f:
			content = f.read()
		#print(content)

		rawTree = str.split(content, treeStart+'\n', 1)[1]
		rawTree = str.split(rawTree, '\n' + treeEnd, 1)[0]
		#print(rawTree)

		nodeList = str.split(rawTree, '\n')
		#print(len(nodeList))
		return nodeList

def main():
	jarName = "[INFO] com.mcmoe:com.mcmoe.jsikulifut13:jar:0.0.1-SNAPSHOT"
	dataFile = "zdependencies.txt"
	nodeList = TreeParser(dataFile, jarName).parse()
	for rawNode in nodeList:
		print(rawNode)


if __name__ == '__main__':
	main()