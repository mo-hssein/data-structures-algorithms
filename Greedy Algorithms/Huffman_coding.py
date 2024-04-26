class Node:
    def __init__(self, char, freq, left=None, right=None) -> None:
        """
        Signature:
        Creates a new node in a Huffman tree.

        Parameters:
        - char (str): The character contained in the node (can be None in internal nodes).
        - freq (int): The frequency or occurrences of the character in the text.
        - left (node[class]): The left child node (default is None).
        - right (node[class]): The right child node (default is None).
        """
        self.ch = char  # The character contained in the node
        self.freq = freq  # The frequency or occurrences of the character in the text
        self.left = left  # The left child node
        self.right = right  # The right child node
