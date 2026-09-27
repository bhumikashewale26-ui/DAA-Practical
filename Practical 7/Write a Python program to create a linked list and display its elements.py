#practical7.1
#Write a Python program to create a linked list and display its elements.


class Node:


  def __init__(self, data):


      self.data = data


      self.next = None


# Create nodes


n1 = Node(10)


n2 = Node(20)


n3 = Node(30)
# Connect nodes


n1.next = n2


n2.next = n3


# Display linked list
current = n1
while current:


  print(current.data)


  current = current.next


#Insert Node in Linked List


#Question: Insert a new node at the beginning of a linked list.


class Node:


  def __init__(self, data):


      self.data = data


      self.next = None


head = Node(20)


head.next = Node(30)


# Insert new node


new_node = Node(10)


new_node.next = head


head = new_node


# Display


current = head


while current:


  print(current.data)


  current = current.next


#Insert Node at the End


class Node:


  def __init__(self, data):


      self.data = data


      self.next = None


head = Node(10)


head.next = Node(20)


new_node = Node(30)


current = head


while current.next:


  current = current.next


current.next = new_node


current = head


while current:


  print(current.data)


  current = current.next


#Delete Node from Linked List


#Question: Delete a node containing a given value.


class Node:


  def __init__(self, data):


      self.data = data


      self.next = None


head = Node(10)


head.next = Node(20)


head.next.next = Node(30)


# Delete 20


head.next = head.next.next


current = head


while current:


  print(current.data)


  current = current.next


#Search an Element in Linked List


class Node:


  def __init__(self, data):


      self.data = data


      self.next = None


head = Node(10)


head.next = Node(20)


head.next.next = Node(30)


search = int(input("Enter value to search: "))


current = head


found = False


while current:
  if current.data == search:
      found = True


      break
  current = current.next
if found:


  print("Element found")


else:


  print("Element not found")






