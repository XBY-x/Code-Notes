
class SinglyNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class SinglyLinkedList:
    def __init__(self, head=None):
        self.head = head
        if not self.head:
            self.length = 0
        else:
            self.length = 1

    def is_empty(self):
        if self.length == 0:
            return True
        else:
            return False

    def append_node(self, node):
        if self.is_empty():
            self.head = node
            self.length += 1
        else:
            cur_node = self.head
            while cur_node.next:
                cur_node = cur_node.next
            cur_node.next = node
            self.length += 1

    def insert_node(self, node, index):
        if index > self.length:
            raise Exception("Index out of range")

        if index == 0:
            node.next = self.head
            self.head = node
            self.length += 1
            return

        pre_node = self.head
        for i in range(index-1):
            pre_node = pre_node.next
        cur_node = pre_node.next
        pre_node.next = node
        node.next = cur_node
        self.length += 1

    def delete_node(self, index):
        if index > (self.length-1):
            raise Exception("Index out of range")

        if index == 0:
            self.head = self.head.next
            self.length -= 1
            return

        pre_node = self.head
        for i in range(index-1):
            pre_node = pre_node.next
        pre_node.next = pre_node.next.next
        self.length -= 1

    def modify_node(self, index, val):
        if index > (self.length-1):
            raise Exception("Index out of range")

        if index == 0:
            self.head.val = val
            return

        cur_node = self.head
        for i in range(index):
            cur_node = cur_node.next
        cur_node.val = val

    def search_node(self, val):
        cur_node = self.head
        index = 0
        if self.length == 0:
            print("List is empty")
            return
        while cur_node:
            if cur_node.val == val:
                print("Found node ", val, ". Index is ", index)
                return
            cur_node = cur_node.next
            index += 1

        print("Not found node ", val)

    def print_list(self):
        cur_node = self.head
        if self.length == 0:
            print("List is empty")
            return
        while cur_node:
            print(cur_node.val)
            cur_node = cur_node.next


if __name__ == '__main__':
    linked_list = SinglyLinkedList()
    empty_flag = linked_list.is_empty()
    print(empty_flag)

    Node1 = SinglyNode(1)
    Node2 = SinglyNode(2)
    Node3 = SinglyNode(3)
    Node4 = SinglyNode(4)
    linked_list.append_node(Node1)
    linked_list.append_node(Node2)
    linked_list.append_node(Node3)
    print('++++++++++++++++++++++++++++')
    # linked_list.insert_node(Node4, 4)
    # linked_list.delete_node(2)
    linked_list.search_node(4)

    linked_list.print_list()
    print("length    ", linked_list.length)
