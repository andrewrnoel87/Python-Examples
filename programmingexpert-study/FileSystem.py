class FileSystem:
    def __init__(self):
        self.root = Directory("/")

    def create_directory(self, path):
        FileSystem._validate_path(path)

        before_last_node, new_directory_name = FileSystem.parse_node_path(path)
        
        new_directory = Directory(new_directory_name)  # create a new directory

        before_last_node.add_node(new_directory)  # add new directory as a child of the before_last_node

    def create_file(self, path, contents):
        FileSystem._validate_path(path)

        before_last_node, new_file_name = FileSystem.parse_node_path(path)
        
        new_file = File(new_file_name)  # Create a new file
        new_file.write_contents(contents)  # Write the contents to the file

        before_last_node.add_node(new_file)  # Add the file node to the direct parent directory node

    def read_file(self, path):
        FileSystem._validate_path(path)

        before_last_node, file_name = FileSystem.parse_node_path(path)

        if not isinstance(before_last_node, Directory):  # make sure before_last_node is a Directory
            raise ValueError(f"{before_last_node.name} isn't a directory.")
        
        if file_name not in before_last_node.children:  # make sure file_name is a child of before_last_node
            raise ValueError(f"File not found: {file_name}.")

        return before_last_node.children[file_name].contents

    def delete_directory_or_file(self, path):
        FileSystem._validate_path(path)

        before_last_node, node_to_delete_name = FileSystem.parse_node_path(path)

        if not isinstance(before_last_node, Directory):  # make sure before_last_node is a Directory
            raise ValueError(f"{before_last_node.name} isn't a directory.")
        
        if node_to_delete_name not in before_last_node.children:  # make sure node_to_delete_name is a child of before_last_node
            raise ValueError(f"File not found: {node_to_delete_name}.")
        
        before_last_node.delete_node(node_to_delete_name)

    def size(self):
        size = 0
        nodes = [self.root]
        while len(nodes) > 0:
            current_node = nodes.pop()
            if isinstance(current_node, Directory):  # if the current_node is a Directory add its children to the list of nodes we are checking for files
                children = list(current_node.children.values())  # make a list of nodes out of the current_node's children. The children's values are nodes.
                nodes.extend(children)  # adding the children list to the node list
                continue
            if isinstance(current_node, File):
                size += len(current_node)  # if the current_node is a File add its len to the size
        return size

    def __str__(self):
        return f"*** FileSystem ***\n" + self.root.__str__() + "\n***"
    
    @staticmethod
    def _validate_path(path):
        if not path.startswith("/"):
            raise ValueError("Path should start with `/`.")
        
    def parse_node_path(self, path):  # returns the node before the node we are adding and the name of the new node

        path_node_names = path[1:].split("/")  # Take the path string, skip the first element which should be a /, and split the string by /'s, return the list
        middle_node_names = path_node_names[:-1]  # The node names except the last one
        new_node_name = path_node_names[-1]  # The last node name, which is the new one we are creating

        before_last_node = self._find_bottom_node(middle_node_names)  # Get the node before the node you are adding

        if not isinstance(before_last_node, Directory):  # make sure before_last_node is a Directory
            raise ValueError(f"{before_last_node.name} isn't a directory.")
        return before_last_node, new_node_name


    def _find_bottom_node(self, node_names):
        current_node = self.root
        for node_name in node_names:
            if not isinstance(current_node, Directory):  # Make sure the current node is a directory
                raise ValueError(f"{current_node.name} isn't a directory.")
            
            if node_name not in current_node.children:  # make sure the node_name is a child of the current_node
                raise ValueError(f"Node not found: {node_name}.")
            
            current_node = current_node.children[node_name]  # move to the next node

        return current_node
            
class Node:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name} ({type(self).__name__})"


class Directory(Node):
    def __init__(self, name):
        super().__init__(name)
        self.children = {}

    def add_node(self, node):
        self.children[node.name] = node

    def delete_node(self, name):
        del self.children[name]

    def __str__(self):
        string = super().__str__()

        children_strings = []
        for child in list(self.children.values()):
            child_string = child.__str__().rstrip()
            children_strings.append(child_string)

        children_combined_string = indent("\n".join(children_strings), 2)
        string += "\n" + children_combined_string.rstrip()
        return string


class File(Node):
    def __init__(self, name):
        super().__init__(name)
        self.contents = ""

    def write_contents(self, contents):
        self.contents = contents

    def __len__(self):
        return len(self.contents)

    def __str__(self):
        return super().__str__() + f" | {len(self)} characters"


def indent(string, number_of_spaces):
    spaces = " " * number_of_spaces
    lines = string.split("\n")
    indented_lines = [spaces + line for line in lines]
    return "\n".join(indented_lines)

