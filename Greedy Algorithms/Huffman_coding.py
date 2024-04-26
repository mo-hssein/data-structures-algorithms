from heapq import heapify, heappop, heappush


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


    def __lt__(self, other):
        """
        Compares the frequency of this node with the frequency of another node for the purpose of less-than comparison.
    

        Parameters:
        - other : Another Node object to compare with this node.

        Returns:
        - True
        or
        - False
        """
        return self.freq < other.freq


def get_huffman_tree(text):
    """
    Constructs a Huffman tree based on the frequency of characters in the given text.
    time complexity = O(n log n)

    Parameters:
    - text (str): The input text for which the Huffman tree is to be constructed.

    Returns:
    - root (node[class]): The root node of the constructed Huffman tree.
    or
    - root (none): If the Parameter text is empty.
    """
    if len(text) == 0:
        return None

    # Count the frequency of each character in the text
    freq = {ch: text.count(ch) for ch in set(text)}

    # Create nodes for each character-frequency pair and store them in a list
    pq = [Node(k, v) for k, v in freq.items()]

    # Heapify the list to create a min-heap
    heapify(pq)

    # Building the Huffman tree
    while len(pq) > 1:
        left, right = heappop(pq), heappop(pq)
        new_freq = left.freq + right.freq
        heappush(
            pq, Node(None, new_freq, left, right)
        )  # Place the new freq in the tree and adjust the tree again

    # Get the root of the Huffman tree
    root = pq[0]
    return root
