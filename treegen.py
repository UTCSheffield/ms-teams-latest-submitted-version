import os
import tkinter as tk
from tkinter import ttk


class DirectoryTree:
   def __init__(self, root_path):
       self.root_path = root_path
       self.tree = {}


   def generate_tree(self):
       self.tree = self._generate_tree(self.root_path)


   def _generate_tree(self, path):
       tree = {}
       for item in os.listdir(path):
           item_path = os.path.join(path, item)
           if os.path.isdir(item_path):
               tree[item] = self._generate_tree(item_path)
           else:
               tree[item] = None
       return tree


   def display_tree(self):
       self._display_tree(self.tree)


   def _display_tree(self, tree, level=0):
       for item, subtree in tree.items():
           if subtree:
               print('  ' * level + f'[{item}]')
               self._display_tree(subtree, level + 1)
           else:
               print('  ' * level + f'{item}')


class DirectoryTreeGUI(tk.Tk):
   def __init__(self):
       super().__init__()
       self.title('Flood-Directory Tree Viewer')
       self.configure(bg='#1a1a1a')
       self.label = tk.Label(self, text='Enter directory path:', bg='#1a1a1a', fg='#ff6600')
       self.label.pack()
       self.entry = tk.Entry(self, width=50)
       self.entry.pack()
       self.button = tk.Button(self, text='Show Directory Tree', command=self.show_tree, bg='#33cc33', fg='#1a1a1a')
       self.button.pack()
       self.tree = ttk.Treeview(self, style='Custom.Treeview')
       self.tree.pack()
       self.style = ttk.Style()
       self.style.configure('Custom.Treeview', background='#1a1a1a', foreground='#ffffff', fieldbackground='#1a1a1a')


   def show_tree(self):
       dir_path = self.entry.get()
       if os.path.isdir(dir_path):
           dir_tree = DirectoryTree(dir_path)
           dir_tree.generate_tree()
           dir_tree.display_tree()
           self.generate_tree(dir_path, '')
       else:
           self.tree.insert('', 'end', text='Invalid directory path')


   def generate_tree(self, dir_path, parent_node):
       for item in os.listdir(dir_path):
           item_path = os.path.join(dir_path, item)
           if os.path.isdir(item_path):
               node = self.tree.insert(parent_node, 'end', text=item, open=False)
               self.generate_tree(item_path, node)
           else:
               self.tree.insert(parent_node, 'end', text=item)




if __name__ == '__main__':
   app = DirectoryTreeGUI()
   