from ..utils.linked_list import Node

class Token(Node):
    """
    This Class represent the token
    """
    def __init__(self, token):
        """init the token class

        Args:
            token (str): Represent the token string 
        """
        super().__init__(token)
        
    def __str__(self):
        """Print as string

        Returns:
            str: token string data
        """
        return self.data

    def lower(self):
        """lower

        Returns:
            str: lower the string 
        """
        return self.data.lower()
        
    @property
    def pos(self):
        """Part of Speech proparty 

        Returns:
            str: POS tag for a token.
        """
        return self._pos

    @pos.setter
    def pos(self, pos):
        """Set POS tag for a token

        Args:
            pos (str): POS Tag
        """
        self._pos = pos
