class LinkedListNode:
  def __init__(self,data):
    self.value=data
    self.next=None

class LinkedList:
  def __init__(self):
    self.head=None

  def insert_atStart(self,data):
    new_node=LinkedListNode(data)
    new_node.next=self.head
    self.head=new_node

  def insert_atPosition(self,data,position):
    new_node=LinkedListNode(data)
    if not self.head:
      self.head=new_node
      return
    current=self.head
    count = 0
    while current and count < position - 1:
      current = current.next
      count += 1
    if not current:
      print(f"Position {position} is out of bounds")
      return
    new_node.next=current.next
    current.next=new_node

  def insert_atEnd(self,data):
    new_node=LinkedListNode(data)
    if not self.head:
      self.head=new_node
      return
    current=self.head
    while current.next:
      current=current.next
    current.next=new_node

  def print(self):
    if not self.head:
      print('Empty Linked List')
      return
    current=self.head
    while current.next:
      print(current.value,end='->'if current.next else '')
      current=current.next
    print('End')

  def delete_atStart(self):
    if not self.head:
      print('Empty Linked List')
      return
    self.head=self.head.next

  def delete_atEnd(self):
    if not self.head:
      print('Empty Linked List')
      return
    if not self.head.next:
      self.head = None
      return
    current=self.head
    while current.next.next:
      current=current.next
    current.next=None

  def delete_atPosition(self,position):
    if not self.head:
      return 'Empty Linked List'
    current=self.head
    count=0
    while current and count<position-1:
      current=current.next
      count+=1
    if not current:
      return f'Position {position} is out of bounds'
    current.next=current.next.next

  def delete_byValue(self,value):
    if not self.head:
      return 'Empty Linked List'
    current=self.head
    if current.value==value:
      self.head=current.next
      return
    while current.next:
      if current.next.value==value:
        current.next=current.next.next
        return
      current=current.next
    return 'Value not found'

ll=LinkedList()
ll.insert_atStart(10)
ll.insert_atEnd(20)
ll.insert_atEnd(30)
ll.insert_atPosition(15,1)
ll.insert_atPosition(25,3)
ll.print()
ll.delete_atStart()
ll.print()
ll.delete_atEnd()
ll.print()
ll.delete_atPosition(1)
ll.print()