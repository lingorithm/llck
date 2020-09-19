
import re
from ..core.sentence import Sentence
from ..constants.emojis import EMOJIS
from ..core.token import Token

DEFAULT_PUNCTUATIONS = [r'(?<=[0-9]|[^0-9.])(\.)(?=[^0-9.]|[^0-9.]|[\s]|$)', r'\.{2,}',
						r'\!+', r'\:+', r'\?+', r'\,+', r'\(|\)|\[|\]|\{|\}|\<|\>']

DEFAULT_SENTENCE_BOUNDARIES = [
	r'(?<=[0-9]|[^0-9.])(\.)(?=[^0-9.]|[^0-9.]|[\s]|$)', r'\.{2,}', r'\!+', r'\:+', r'\?+']

class Tokenize:
	def __init__(self, options = {}):
		"""init function for tokenize pipeline

		Args:
			options (dict, optional): [description]. Defaults to {}.
		"""
		if 'tokens_boundaries' in options:
			options['tokens_boundaries'] += DEFAULT_PUNCTUATIONS
		else: 
			options['tokens_boundaries'] = DEFAULT_PUNCTUATIONS
		
		if 'sentences_boundaries' in options:
			options['sentences_boundaries'] += DEFAULT_SENTENCE_BOUNDARIES
		else:
			options['sentences_boundaries'] = DEFAULT_SENTENCE_BOUNDARIES

		self.options = options
		
	def __call__(self):
		return self.document

	def tokenize(self, sentence):
		"""tokenize function

		Args:
			sentence (str): string of sentence

		Returns:
			list: list of tokens
		"""
		working_sentence = sentence
		# First deal with possible word splits:
		if self.options.get('join_split_text', True):
			working_sentence = re.sub(r'([a-z]+)('+self.options.get('split_text_char', r'\-')+'[\n])([a-z]+)', r'\g<1>\g<3>', working_sentence)
		# escape
		working_sentence = self.__escape_punctuation(working_sentence)
		working_sentence = self.__escape_emoji(working_sentence)
		# split at any split_characters
		working_sentence = re.sub(
			self.options.get('split_characters', r'\s|\t|\n|\r'), self.options.get('delimiter_token', '<SPLIT>'), working_sentence)
		# split tokens by delimiter
		list_of_token_strings = [x.strip() for x in working_sentence.split(
			self.options.get('delimiter_token', '<SPLIT>')) if x.strip() != ""]
		return list_of_token_strings

	def process(self, document):
		"""Process data using a pipeline

		Args:
			document (Document): Document input data

		Returns:
			Document: document object contains all the data
		"""
		# type check
		if isinstance(document, str):
			print('document needs to be initiated.')
		else:
			self.document = document
					
		# adding sentence delimiter
		working_document = self.__sentences_delimiter()
		sentences = []
		# Split it into list if not empty
		for sent in working_document.split('<SPLIT>'):
			# if sentence is not empty
			if sent.strip() != "":
				# init Sentence class
				sentence = Sentence(sent.strip())
				# tokenize sentence
				sentence.tokens = [Token(token) for token in self.tokenize(sentence.get())]
				# ass to sentences
				sentences.append(sentence)
		# add sentences to documet
		self.document.sentences = sentences
		return self.document
		
	def __sentences_delimiter(self):
		"""it adds split tag after each sentence.

		Returns:
			str: splited document
		"""
		doc = self.document.get()
		# Replace sentence boundaries with delimiter token
		for punct in self.options['sentences_boundaries']:
			doc = re.sub(
				punct, r'\g<0><SPLIT>', doc, flags=re.UNICODE)
		return doc

	def __escape_punctuation(self, sentence):
		"""it adds spaces before and after punctuation

		Args:
			sentence (str): input text

		Returns:
			str: escaped text
		"""
		tokens_boundaries = self.options.get(
			'tokens_boundaries', DEFAULT_PUNCTUATIONS)
		#Escape punctuation
		for punct in tokens_boundaries:
			sentence = re.sub(punct, r" \g<0> ", sentence)
		return sentence

	def __escape_emoji(self, sentence):
		"""it adds spaces before and after emoji
		Args:
			sentence (str): input text

		Returns:
			str: escaped text
		"""
		return re.sub(EMOJIS, r' \g<0> ', sentence)
