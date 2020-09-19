from ...core.language import Language
from ...pipeline.tokenize import Tokenize

class EN(Language):
    def __init__(self, processors, options):
        """init arabic lass

        Args:
            processors (list): define processing processors
            options (dict): processors options
        """
        super().__init__('en', processors)
        self.register_pipeline('tokenize', Tokenize(options))
