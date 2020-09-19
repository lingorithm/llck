import re
from snowballstemmer import stemmer
from ...core.token import Token
from ...pipeline.tokenize import Tokenize


class ArabicTokenize(Tokenize):
    """
    This class extendes the tokenize pipeline class to be used for arabic
    """
    def __init__(self, options, **kwargs):
        """init class
        """
        options['tokens_boundaries'] = [r'\؟+']
        super().__init__(options, **kwargs)
        self.stemmer = stemmer("arabic")


    def __remove_tatweel(self, text):
        """it removes arabic words extendings ـ 

        Args:
            text (str): input string

        Returns:
            str: output string
        """
        return re.sub(r'\u0640', "", text)

    def __remove_diacrtics(self, text):
        """ it removes arabic diacritics

        Args:
            text (str): input string

        Returns:
            str: output string
        """
        self.diacritics = re.compile(r'[\u0617-\u061A\u064B-\u0652]')
        return re.sub(self.diacritics, "", text)

    def __name_follows(self, token): 
        """split the token based on letters start with

        Args:
            token (str): a word

        Returns:
            list: splited word
        """
        follows = [
            '\u0628',  # ب
            '\u0643',  # ك
            '\u0644',  # ل
            '\u0648',  # و
            '\u062a',  # ت
            '\u0633'
        ]
        stem = stemmer("arabic").stemWord(token)
        for follow in follows:
            if token.startswith(follow) and not stem.startswith(follow):
                token = re.sub(
                    follow, r'\g<0><SPLIT>', token, flags=re.UNICODE)
        return token.split("<SPLIT>")

    def tokenize(self, sentence, *args, **kwargs):
        """overwrite the tokenize funtion

        Args:
            sentence (str): input sentence

        Returns:
            list: list of tokens
        """
        tokens = []
        if self.options.get('remove_tatweel', True):
            sentence = self.__remove_tatweel(sentence)
        if self.options.get('remove_diacritics', False):
            sentence = self.__remove_diacrtics(sentence)

        for t in super().tokenize(sentence, *args, **kwargs):
            temp_tokens = []
            # # لل
            if t.startswith('\u0644\u0644'):
                temp_tokens.append(t[0:1])
                temp_tokens.append(t[1:])
                t = ''
            else:
                tokens += self.__name_follows(t)
            tokens += temp_tokens
        return tokens
