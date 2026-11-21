class node:
    def __init__(self , data):
        self.data=data
        self.next=None

class linkedlist:
    def __init__(self):
        self.head = None
    def insert(self,data):
        new_node = node(data)
        if self.head is None:
            self.head=new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
        print("inserted")
    def delete(self,key):
        if self.head is None:
            print("list is empty .. ")
            return
        if self.head.data == key:
            self.head = self.head.next
            print("deleted")
        temp = self.head
        while temp.next is not None:
            if temp.next.data == key:
                temp.next = temp.next.next
                print("deleted.")
            temp = temp.next
        print("invalid")
    def display(self):
        if self.head is None:
            print("empty..")
            return 
        temp = self.head
        while temp is not None:
            print(temp.data , end="->")
            temp = temp.next
        print("none")

ll = linkedlist()
while True:
    print("1.insert")
    print("2.delete")
    print("3.display")
    print("4.exit")
    choice = int(input("enter the choice:"))
    if choice == 1:
        data = int(input("enter the number to insert :"))
        ll.insert(data)
    elif choice == 2:
        key = int (input("enter the number:"))
        ll.delete(key)
    elif choice == 3:
        ll.display()
    else:
        break