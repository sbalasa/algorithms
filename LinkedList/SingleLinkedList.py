class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = new_node

    def insert_beg(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at(self, pos, data):
        if pos == 0:
            self.insert_beg(data)
        else:
            new_node = Node(data)
            temp = self.head
            while pos-1:
                temp = temp.next
                pos -= 1
            new_node.next = temp.next
            temp.next = new_node

    def delete(self, data):
        temp = self.head
        while temp.next.data != data:
            temp = temp.next
        prev = temp
        temp = self.head
        while temp.data != data:
            temp = temp.next
        prev.next = temp.next

    def size(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        print(count)

    def display(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def clear(self):
        self.head = None


if __name__ == "__main__":
    L1 = LinkedList()
    L1.append(45)
    L1.append(3)
    L1.insert_beg(2)
    L1.insert_beg(4)
    L1.insert_at(0, 1)
    L1.insert_at(3, 44)
    L1.append(90)
    L1.delete(4)
    L1.delete(3)
    L1.display()
    L1.size()
    L1.clear()
    L1.size()
