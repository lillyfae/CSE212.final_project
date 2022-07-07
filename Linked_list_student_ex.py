class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node_in_order(self, new_node):
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            current = self.head
            while current.price <= new_node.price and current.next != None:
                current = current.next
            if current.prev != None:
                current.prev.next = new_node
                new_node.prev = current.prev
            else:
                self.head = new_node
            new_node.next = current
            current.prev = new_node

    def print_self(self):
        current = self.head
        while current != None:
            print(current.name + ": $" + str(current.price))
            current = current.next
            

class Streaming_Service_Node:
    def __init__(self, name, price):
        self.name = name
        self.next = None
        self.prev = None
        self.price = price

linked_list = Linked_List()

netflix = Streaming_Service_Node("Netflix", 10.99)
linked_list.insert_node_in_order(netflix)

hulu = Streaming_Service_Node("Hulu", 7.99)
linked_list.insert_node_in_order(hulu)

disney = Streaming_Service_Node("Disney+", 8.99)
linked_list.insert_node_in_order(disney)

linked_list.print_self()

