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
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

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
            while pos - 1:
                temp = temp.next
                pos -= 1
            new_node.next = temp.next
            temp.next = new_node

    def display(self):
        if not self.head:
            return "List is Empty"
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print("\n")

    def size(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count

    def delete(self, data):
        temp = self.head
        prev = self.head
        try:
            while prev.next.data != data:
                prev = prev.next
            while temp.data != data:
                temp = temp.next
            prev.next = temp.next
        except AttributeError:
            self.head = temp.next

    def delete_pos(self, pos):
        if not self.head:
            return "List is Empty"
        temp = self.head
        try:
            count = pos
            count_prev = pos
            temp_prev = self.head
            while count_prev - 1:
                temp_prev = temp_prev.next
                count_prev -= 1
            while count:
                temp = temp.next
                count -= 1
            temp_prev.next = temp.next
        except AttributeError:
            self.head = temp.next

    def search(self, data):
        temp = self.head
        pos = 0
        try:
            while temp.data != data:
                temp = temp.next
                pos += 1
            if temp.data == data:
                print(pos)
        except AttributeError:
            print(-1)

    def get_data(self, pos):
        temp = self.head
        count = 0
        try:
            while count != pos:
                temp = temp.next
                count += 1
            print(temp.data)
        except AttributeError:
            print(-1)

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
    L1.delete_pos(0)
    L1.display()
    L1.search(90)
    L1.get_data(77)
    L1.size()
    L1.clear()
    L1.size()
