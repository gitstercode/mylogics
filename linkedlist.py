class Node(object):
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node
    def get_data(self):
        return self.data
    def set_data(self, d):
        self.data = d
    def get_next_node(self):
        return self.next_node
    def set_next_node(self, n):
        self.next_node=n

class LinkedList(object):
    def __init__(self, r=None):
        self.root=r
        self.size=0

    def get_size(self):
        return self.size

    def prepend(self, d):
        new_node=Node(data=d, next_node=None)
        self.root=new_node
        self.size += 1

    def append(self, d):
        this_node=self.root
        while this_node is not None:
            if this_node.get_next_node() is None:
                new_node=Node(d)
                this_node.set_next_node(new_node)
                self.size+=1
                return d
            else:
                this_node=this_node.get_next_node()

    def remove(self, d):
        this_node=self.root
        prev_node=None
        while this_node:  # Whicle self.root is not None
            if this_node.get_data() == d:
                if prev_node:
                    prev_node.set_next_node(this_node.get_next_node())
                else:
                    # self.root=this_node
                    pass
                self.size -= 1
                return True
            else:
                prev_node=this_node
                this_node=this_node.get_next_node()
        return False
    def find(self,d):
        this_node=self.root
        while this_node:
            if this_node.get_data() ==  d:
                return d
            else:
                this_node=this_node.get_next_node()
        return False

my_list=LinkedList()
my_list.prepend(1)
print my_list.append(2)

print my_list.find(2)
my_list.prepend(5)
my_list.append(9)

print my_list.get_size()

