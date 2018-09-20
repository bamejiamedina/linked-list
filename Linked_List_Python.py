class Linked_List:

  class __Node:

    def __init__(self, val):
        self.value = val
        self.previous = None
        self.next = None

  def __init__(self):
    self.__size = 0
    self.__header = Linked_List.__Node(None)
    self.__trailer = Linked_List.__Node(None)
    self.__header.next = self.__trailer
    self.__trailer.previous = self.__header

  def __len__(self):
    return self.__size

  def append_element(self, val):
    newest = Linked_List.__Node(val)
    newest.next = self.__trailer
    newest.previous = self.__trailer.previous
    self.__trailer.previous.next = newest
    self.__trailer.previous = newest
    self.__size = self.__size+1

  def insert_element_at(self, val, index):
    if index < 0 or index > self.__size:
        raise IndexError
    elif index == self.__size:
        self.append_element(val)
        return
    new_node = Linked_List.__Node(val)
    if index == 0:
        new_node.next = self.__header.next
        new_node.previous = self.__header
        new_node.next.previous = new_node
        self.__header.next = new_node
        self.__size = self.__size+1
    elif index < self.__size/2:
        current = self.__header.next
        for i in range(0, index-1):
            current = current.next
        new_node.next = current.next
        new_node.previous = current
        current.next.previous = new_node
        current.next = new_node
        self.__size = self.__size+1
    elif index >=self.__size/2:
        current = self.__trailer.previous
        for i in range(0, self.__size-(index)-1):
            current = current.previous
        new_node.previous = current.previous
        new_node.next = current
        current.previous.next = new_node
        current.previous = new_node
        self.__size = self.__size+1

  def remove_element_at(self, index):
    if index < 0 or index >= self.__size:
        raise IndexError
    if index == 0:
        self.__header.next = self.__header.next.next
        self.__header.next.previous = self.__header
    elif index == self.__size -1:
        self.__trailer.previous = self.__trailer.previous.previous
        self.__trailer.previous.next = self.__trailer
    elif index < self.__size/2:
        current = self.__header.next
        for i in range (0, index-1):
            current = current.next
        current.next = current.next.next
        current.next.previous = current
    elif index >= self.__size/2:
        current = self.__trailer.previous
        for i in range (0, self.__size-index-2):
            current = current.previous
        current.previous = current.previous.previous
        current.previous.next = current
    self.__size = self.__size-1

  def get_element_at(self, index):
    if index < 0 or index >= self.__size:
        raise IndexError
    if index == 0:
        return self.__header.next.value
    elif index == self.__size -1:
        return self.__trailer.previous.value
    elif index < self.__size/2:
        current = self.__header.next
        for i in range (0, index):
            current = current.next
        return current.value
    elif index >= self.__size/2:
        current = self.__trailer.previous
        for i in range (0, self.__size-index-1):
            current = current.previous
        return current.value

  def rotate_left(self):
    if self.__size == 0 or self.__size == 1:
        return
    temp_node = Linked_List.__Node(self.__header.next.value)
    self.__header.next = self.__header.next.next
    self.__header.next.previous = self.__header
    temp_node.next = self.__trailer
    temp_node.previous = self.__trailer.previous
    self.__trailer.previous.next = temp_node
    self.__trailer.previous = temp_node

  def __str__(self):
    temp1 = "[ "
    current = self.__header.next
    temp2 = temp1
    if self.__size >= 1:
        temp2 = temp1 + str(current.value)
        for i in range (0, self.__size-1):
            current = current.next
            temp2 = temp2 + ", " + str(current.value)
    temp1 = temp2 + " ]"
    return temp1

  def __iter__(self):
    self.__iter_node = self.__header.next
    return self

  def __next__(self):
    if self.__iter_node is self.__trailer:
        raise StopIteration
    to_return = self.__iter_node.value
    self.__iter_node = self.__iter_node.next
    return to_return

if __name__ == '__main__':
  new = Linked_List()
  print("instantiate new list")
  print("linked list: ", new)
  print("length: ", len(new))
  print(" ")

  #appending, verifying that element has added and size has incremented
  new.append_element(4)
  print("append 4")
  print("linked list: ", new)
  print("length: ", len(new))
  print(" ")

  #adding at head, verifying that element has added and size has incremented
  new.insert_element_at(1, 0)
  print("insert 1 at head")
  print("linked list: ", new)
  print("length: ", len(new))
  print(" ")

  #adding in the middle, verifying that element has added and size has incremented
  new.insert_element_at(2, 1)
  print("insert 2 at index 1")
  print("linked list: ", new)
  print("length: ", len(new))
  print(" ")

  #adding at the end, verifying that element has added and size has incremented
  new.insert_element_at(5, 3)
  print("insert 5 at index 3")
  print("linked list: ", new)
  print("length: ", len(new))
  print(" ")

  #adding at an invalid low index, verifying that the appropriate exception is raised
  print("add before the head")
  try:
      new.insert_element_at(3, -1)
      print("linked list: ", new)
      print("length: ", len(new))
  except (IndexError):
    print("invalid index")
    print(" ")

  #adding at an invalid high index, verifying that the appropriate exception is raised
  print("add after the tail")
  try:
      new.insert_element_at(3, 5)
      print("linked list: ", new)
      print("length: ", len(new))
  except (IndexError):
      print("invalid index")
      print(" ")

  #all of the insert_element_at test cases also test __str__ and __len__

  #removing the head, verifying that the element has been removed and size has decremented
  new.remove_element_at(0)
  print("remove the head")
  print("linked list: ", new)
  print("length: ", len(new))
  print(" ")

  #removing from the middle, verifying that the element has been removed and size has decremented
  new.remove_element_at(1)
  print("remove from index 1")
  print("linked list: ", new)
  print("length: ", len(new))
  print(" ")

  #removing the tail, verifying that the element has been removed and size has decremented
  new.remove_element_at(1)
  print("remove the tail")
  print("linked list: ", new)
  print("length: ", len(new))
  print(" ")

  #removing from an invalid low index, verifying that the appropriate exception is raised
  #now commented out to allow the rest of the code to execute
  print ("remove before the head")
  try:  
    new.remove_element_at(-1)
    print("linked list: ", new)
    print("length: ", len(new))
  except (IndexError):
    print ("index error")
    print(" ")

  #removing from an invalid high index, verifying that the appropriate exception is raised
  #now commented out to allow the rest of the code to execute
  print("remove after the tail")
  try:
    new.remove_element_at(2)
    print("linked list: ", new)
    print("length: ", len(new))
  except (IndexError):
    print ("index error")
    print(" ")
    
  #removing the only element, verifying that the element has been removed and size has decremented
  new.remove_element_at(0)
  print("remove the only element")
  print("linked list: ", new)
  print("length: ", len(new))
  print(" ")

  #repopulating the linked list
  print("repopulating")
  for i in range (0, 5):
    new.append_element(2*i)
    print("index: ", i)
    print("linked list: ", new)
    print("length: ", len(new))
    print(" ")

  #traversing the linked list with a for loop, verifying that the values are accessible in an appropriate format
  print("traversing the linked list")
  for j in new:
    print ("value: ", j)
    print ("type: ", type(j))
  print(" ")

  #accessing the value at each index, verifying that the linked list remains unchanged
  print("accessing values")
  for k in range(len(new)):
    print("index: ", k)
    print("value: ", new.get_element_at(k))
    print("linked list: ", new)
    print("length: ", len(new))
    print(" ")

  #accessing an invalid high index, verifying that the appropriate exception is raised
  print("get element after the tail")
  try:
    new.get_element_at(7)
    print("linked list: ", new)
    print("length: ", len(new))
  except (IndexError):
    print ("index error")
    print(" ")

  #accessing an invalid low index, verifying that the appropriate exception is raised
  print("get element before the head")
  try:
    new.get_element_at(-2)
    print("linked list: ", new)
    print("length: ", len(new))
  except (IndexError):
    print ("index error")
    print(" ")

  #rotating left, verifying that the linked list rearranges properly and the size remains the same
  print("rotating left")
  new.rotate_left()
  print("linked list: ", new)
  print("length: ", len(new))
  print(" ")

  #depopulating linked list, rotating left
  print("depopulating linked list")
  for l in range(len(new)):
    new.remove_element_at(0)
  print("linked list: ", new)
  print("length: ", len(new))
  print(" ")

  print("rotating linked list left")
  new.rotate_left()
  print("linked list: ", new)
  print("length: ", len(new))
  print(" ")
  
    