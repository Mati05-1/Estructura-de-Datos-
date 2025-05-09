class Node:
    def __init__(self, data: int):
        self.data = data
        self.left_child = None
        self.right_child = None

    def __repr__(self):
        return '({})'.format(self.data)

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def traverse(self, subtree: Node):
        """Recorrido en pre-orden (raíz, izquierda, derecha)"""
        if subtree is not None:
            print(subtree)
            self.traverse(subtree.left_child)
            self.traverse(subtree.right_child)

    def insert(self, value: int):
        """Inserta un valor en el árbol (versión pública)"""
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value: int, subtree: Node):
        """Inserta un valor en el árbol (versión privada recursiva)"""
        if value < subtree.data:
            if subtree.left_child is None:
                subtree.left_child = Node(value)
            else:
                self._insert(value, subtree.left_child)
        elif value > subtree.data:
            if subtree.right_child is None:
                subtree.right_child = Node(value)
            else:
                self._insert(value, subtree.right_child)
        else:
            print('Value already exists in tree...')

    def search(self, key: int) -> bool:
        """Busca un valor en el árbol (versión pública)"""
        if self.root is None:
            return False
        else:
            return self._search(key, self.root)

    def _search(self, key: int, subtree: Node) -> bool:
        """Busca un valor en el árbol (versión privada recursiva)"""
        if key == subtree.data:
            return True
        elif (key < subtree.data) and (subtree.left_child is not None):
            return self._search(key, subtree.left_child)
        elif (key > subtree.data) and (subtree.right_child is not None):
            return self._search(key, subtree.right_child)
        else:
            return False

    def find_min(self, subtree: Node = None) -> Node:
        """Encuentra el nodo con el valor mínimo"""
        if subtree is None:
            if self.root is None:
                return None
            subtree = self.root
        while subtree.left_child is not None:
            subtree = subtree.left_child
        return subtree

    def find_max(self, subtree: Node = None) -> Node:
        """Encuentra el nodo con el valor máximo"""
        if subtree is None:
            if self.root is None:
                return None
            subtree = self.root
        while subtree.right_child is not None:
            subtree = subtree.right_child
        return subtree

    def print_pretty(self):
        """Imprime el árbol de forma visual"""
        if self.root is not None:
            lines, *_ = self._build_tree_string(self.root)
            print("\n" + "\n".join(line.rstrip() for line in lines))
        else:
            print("\nEmpty tree...")

    def _build_tree_string(self, node: Node):
        """Método auxiliar para print_pretty"""
        if node.right_child is None and node.left_child is None:
            line = str(node.data)
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        if node.right_child is None:
            lines, n, p, x = self._build_tree_string(node.left_child)
            s = str(node.data)
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        if node.left_child is None:
            lines, n, p, x = self._build_tree_string(node.right_child)
            s = str(node.data)
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        left, n, p, x = self._build_tree_string(node.left_child)
        right, m, q, y = self._build_tree_string(node.right_child)
        s = str(node.data)
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

    def delete(self, value: int):
        """Elimina un nodo del árbol (versión pública)"""
        if self.root is None:
            print("Tree is empty")
            return
        self.root = self._delete_node(self.root, value)

    def _delete_node(self, subtree: Node, value: int) -> Node:
        """Elimina un nodo del árbol (versión privada recursiva)"""
        if subtree is None:
            return subtree
        
        if value < subtree.data:
            subtree.left_child = self._delete_node(subtree.left_child, value)
        elif value > subtree.data:
            subtree.right_child = self._delete_node(subtree.right_child, value)
        else:
            # Nodo con un solo hijo o sin hijos
            if subtree.left_child is None:
                return subtree.right_child
            elif subtree.right_child is None:
                return subtree.left_child
            
            # Nodo con dos hijos: obtener el sucesor inorden (mínimo en el subárbol derecho)
            temp = self.find_min(subtree.right_child)
            subtree.data = temp.data
            subtree.right_child = self._delete_node(subtree.right_child, temp.data)
        
        return subtree

    def _get_height(self, node: Node) -> int:
        """Calcula la altura del árbol (método privado)"""
        if node is None:
            return 0
        return 1 + max(self._get_height(node.left_child), self._get_height(node.right_child))

    def get_height(self) -> int:
        """Obtiene la altura del árbol (método público)"""
        return self._get_height(self.root)
