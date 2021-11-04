
class Node:

    def __init__(self, x):
        self.x = x
        self.next = None


class Lista:

    def __init__(self):
        self.init = None

    def append(self, node):

        if self.init is None:
            self.init = node
            return

        node_aux = self.init
        while node_aux.next is not None:
            node_aux = node_aux.next

        node_aux.next = node

    def add(self, node):

        if self.init is None:
            self.init = node
            return

        node.next = self.init
        self.init = node

    def __str__(self):
        str_aux = '['
        node_aux = self.init
        while(node_aux is not None):
            str_aux += str(node_aux.x) + ','
            node_aux = node_aux.next
        str_aux += ']'
        return str_aux


if __name__ == '__main__':
    lista = Lista()
    lista.append(Node(x=5))
    lista.append(Node(x=19))
    print(lista)
    lista.add(Node(x=27))
    print(lista)
    lista.add(Node(x=1))
    print(lista)