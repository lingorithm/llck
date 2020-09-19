from .document import Document

class Language:
    """
    This class is used to define the language operation
    """

    def __init__(self, lang, processors = {}):
        """

        Args:
            lang (str): Define the language name based on ISO standered
            processors (dict): process pipeline
        """
        self.lang = lang
        self.processors = processors
        self.pipeline = {}
        self._constents = {}
        # check if custom processors is not registered
        for processor in self.processors:
            pipe = self.processors[processor]
            if not isinstance(pipe, str):
                self.register_pipeline(processor, pipe)

    def process(self, document):
        """Process a raw string

        Args:
            document (str): Represent the data that will be processed

        Returns:
            [Document]: Document class 
        """
        # check if pipeline avilable for this language
        for pipe in self.processors.keys():
            if not pipe in self.pipeline.keys():
                raise Exception(
                    "{0} processor: is not available for {1} language.".format(pipe, self.lang))
                    
        _document = Document(document)
        for processor in self.processors:
            pipe = self.processors[processor]
            if isinstance(pipe, str): 
                _document = self.pipeline[pipe].process(_document)
            elif hasattr(pipe, 'process'):
                _document = pipe.process(_document)
            else:
                _document = pipe(_document)
            
        return _document

    def register_pipeline(self, name, pipe):
        """Register a pipeline to be used in processing

        Args:
            name (str): Represent the name of the pipeline
            pipe (init class): Define the pipeline class with a function process
        """
        if not name in self.pipeline:
            self.pipeline[name] = pipe
        
