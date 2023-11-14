import numpy as np

class openHash:
	table_size = 11
	class _Node:
		def __init__(uid, element):
			self.uid = uid
			self.name = element
			self.next = None
	def __init__():
		self.hashTable = []
		self.p = 13
		self.a = np.random.randint(1,p)
		self.b = np.random.randint(0,p)

		self._initializeHashTable()

	def _initializeHashTable():
		self.hashTable = [None] * openHash.table_size

	def _getHashValue(self, element):
		hashvalue = 0
		for ch in element:
			hashvalue = hashvalue << 5
			hashvalue = hashvalue + ord(ch)
		return hashvalue

	def _compressHashValue(self, hashval):
		return ( ( (hashval*a + b)%self.p)%openHash.table_size)

	def _hash(self, element):
		hashvalue = self._getHashValue(element)
		table_index = _compressHashValue(hashvalue)
		return table_index

	def isMember(self, element):
		bucket = self._hash(element)
		current = sel.hashTable[bucket]

		while current != None:
			if current.uid == element:
				return True
			else:
				current = current.next
		return False
			
	def addElement(self, element, name):
		if not self.isMember(element):
			bucket = self._hash(element)			
			newNode = self._Node(element, name)
 			newNode.next = self.hashTable[bucket]
			self.hashTable[bucket] = newNode

	def deleteElement(self, element):
		bucket = self._hash(element)
		if self.hashTable[bucket] != None:
			if self.hashTable[bucket].uid == element:
				self.hashTable[bucket] = self.hashTable[bucket].next
			else:
				current = self.hashTable[bucket]
				while current.next != None:
					if current.next.uid == element:
						current.next = current.next.next
					else:
						current = current.next

	
								
						