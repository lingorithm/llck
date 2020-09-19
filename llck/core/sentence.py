from ..utils.linked_list import Node, LinkedList

class Sentence(Node):
    """
    This class represent a sentence
    """
    def __init__(self, sentence):
        """init a Sentence class

        Args:
            sentence (str): sentence data
        """
        super().__init__(sentence)
        self._index = 0

    @property
    def tokens(self):
        """tokens proparty for a sentence

        Returns:
            list: List of tokens for this sentence
        """
        return self._tokens 

    @tokens.setter
    def tokens(self, tokens):
        """Set the linked list of a token

        Args:
            tokens (list): list of tokens (Token)
        """
        self._tokens = LinkedList(tokens)
