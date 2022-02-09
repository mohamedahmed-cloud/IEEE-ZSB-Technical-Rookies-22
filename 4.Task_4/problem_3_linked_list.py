
# Node Class
class Node :
    # To initialize the node object 
    def __init__(self, data):
        self.data=data
        self.next=None

# linkedlist class
class linkedlist:
    def __init__ (self):
        self.head=None
    # To add node in the front of linked list
   
        def push(self,new_data):
            new_node=Node(new_data)
            new_node.next=self.head
            self.head=new_node
    # To add node After of the linked list
   
        def insert_After(self,prev_node,new_data):
            if prev_node is None:
                print("The given previous node must inLinkedList.")
                return
            new_node = Node(new_data)
            new_node.next = prev_node.next
            prev_node.next = new_node

    # To add at the End of linked list
    
        def append(self, new_data):
            new_node = Node(new_data)
            if self.head is None:
                self.head = new_node
                return
            last = self.head
            while (last.next):
                last = last.next
            last.next =  new_node
  
        # Utility function to print the linked list
        def printList(self):
            temp = self.head
            while (temp):
                print (temp.data),
                temp = temp.next


    # deletion 
    def deleteNode(self, key):
         
        # Store head node
        temp = self.head

        # If head node itself holds the key to be deleted
        if (temp is not None):
            if (temp.data == key):
                self.head = temp.next
                temp = None
                return
 
        # Search for the key to be deleted, keep track of the previous node as we need to change 'prev.next
        while(temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
 
        # if key was not present in linked list
        if(temp == None):
            return
 
        # Unlink the node from linked list
        prev.next = temp.next
 
        temp = None
 
 
    # Utility function to print the linked LinkedList
    def printList(self):
        temp = self.head
        while(temp):
            print (" %d" %(temp.data)),
            temp = temp.next


    # counting
    def getCount(self):
        temp = self.head # Initialise temp
        count = 0 # Initialise count
 
        # Loop while end of linked list is not reached
        while (temp):
            count += 1
            temp = temp.next
        return count



                          
