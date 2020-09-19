from ...core.language import Language
from .tokenize import ArabicTokenize

class AR(Language):
    def __init__(self, processors, options):
        """init arabic lass

        Args:
            processors (list): define processing processors
            options (dict): processors options
        """
        super().__init__('ar', processors)
        self.register_pipeline('tokenize', ArabicTokenize(options))
