
from ..utils.linked_list import LinkedList, Node

class Document(Node):
    """
    This Class represent the document
    """
    def __init__(self, raw):
        """init the document class

        Args:
            raw (str): Represent the raw data for the document
        """
        super().__init__(raw)
    
    @property
    def sentences(self):
        """sentences proparty

        Returns:
            list: List of sentences in the document
        """
        return self._sentences

    @sentences.setter
    def sentences(self, sentences):
        """Set the linked list of sentences

        Args:
            sentences (list): list of Sentence (Sentence)
        """
        self._sentences = LinkedList(sentences)
