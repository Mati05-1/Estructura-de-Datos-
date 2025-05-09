import os
from pathlib import Path

class Node():
    def __init__(self, name: str):
        self.name = name

class Tree(): 
    def __init__(self, name: str):
        self.name = name
        self.children = []

    def insert_child(self, object: any):
        self.children.append(object)

    def get_children(self):
        return self.children

def build_tree(path: str, parent_node: Tree, depth: int = 0, max_depth: int = 20):
    try:
        with os.scandir(path) as entries:
            for entry in sorted(entries, key=lambda e: e.name.lower()):
                if entry.name.startswith('.') or entry.name == __file__:
                    continue
                    
                if entry.is_dir(follow_symlinks=False):
                    dir_node = Tree(entry.name)
                    parent_node.insert_child(dir_node)
                    try:
                        build_tree(entry.path, dir_node, depth + 1, max_depth)
                    except (PermissionError, FileNotFoundError) as e:
                        error_node = Node(f"[Error: {str(e)}]")
                        parent_node.insert_child(error_node)
                else:
                    file_node = Node(entry.name)
                    parent_node.insert_child(file_node)
    except PermissionError as e:
        error_node = Node(f"[Error: {str(e)}]")
        parent_node.insert_child(error_node)

def print_tree(node: any, prefix: str = "", is_last: bool = True):
    if isinstance(node, Tree):
        children = node.get_children()
        for i, child in enumerate(children):
            connector = "└── " if i == len(children) - 1 else "├── "
            print(prefix + connector + child.name)
            if isinstance(child, Tree):
                new_prefix = prefix + ("    " if i == len(children) - 1 else "│   ")
                print_tree(child, new_prefix, i == len(children) - 1)

def main():
    import sys
    
    if len(sys.argv) > 2:
        print("Uso: python directory_tree.py [<path>]")
        sys.exit(1)
    
    path = sys.argv[1] if len(sys.argv) == 2 else "."
    path = os.path.abspath(path)
    
    if not os.path.exists(path):
        print(f"Error: El path '{path}' no existe.")
        sys.exit(1)
    
    # Si es el directorio actual, mostramos solo su contenido
    if os.path.abspath(path) == os.path.abspath("."):
        tree = Tree(".")
    else:
        tree = Tree(os.path.basename(path))
    
    build_tree(path, tree)
    print_tree(tree)

if __name__ == "__main__":
    main()
