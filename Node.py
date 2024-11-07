class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def remove(self, key):
        current = self.head
        if current and current.data == key:
            self.head = current.next
            current = None
            return
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next
        if current is None:
            return
        prev.next = current.next
        current = None

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

# Membuat linked list baru
list = LinkedList()

# Menambahkan node baru di awal linked list
list.add_front(3)
list.add_front(1)
list.add_front(7)

# Menambahkan node baru di akhir linked list
list.add_end(9)
list.add_end(5)

# Menampilkan isi linked list
print("Linked list setelah penambahan:")
list.display()

# Menghapus node dengan nilai 3
list.remove(3)

# Menampilkan isi linked list setelah penghapusan
print("Linked list setelah penghapusan:")
list.display()
