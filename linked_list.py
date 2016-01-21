class Node():
	def __init__(self):
		self.content = None
		self.next = None

class LinkedList():
	def __init__(self):
		self.head = None

	def __str__(self):
		if(self.head is None):
			return('[]')
		else:
			str = '['
			current = self.head
			while(current is not None):
				str += '{0}'.format(current.content)
				if(current.next is not None):
					str += ', '
				current = current.next
			str += ']'
			return(str)

	def enqueue(self, object):
		node = Node()
		node.content = object
		if(self.head is None):
			self.head = node
		else:
			current = self.head
			while(current and current.next):
				current = current.next
			current.next = node

	def dequeue(self):
		if(self.head is None):
			return(None)
		else:
			node = self.head
			self.head = self.head.next
			return(node.content)
