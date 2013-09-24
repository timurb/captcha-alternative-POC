import os
import string

class Tokenizer:

    default_length = 10

    def __init__(self, secret):
      self.tokens = []
      self.secret = self._hex(secret)

    def generate(self, length = default_length):
      '''Generate and store random token'''

      token = self._hex(os.urandom(length))
      self.tokens.append(self.encode(token))
      return token

    def check(self, token):
      '''Check if token is correct (when passed unencrypted)'''
      token = self.encode(token)
      return self.check_encoded(token)

    def check_encoded(self, token):
      '''Check if token is correct (when passed encrypted)'''
      return self.tokens.index(token)

    def encode(self,token):
      '''Encode hex string'''
      result = ""
      for idx,char in enumerate(token):
        result += chr(int(char,16) ^ int((self.secret*100)[idx],16))
      return self._hex(result)

    def _hex(self,s):
      '''Convert string to hex chars'''
      hexnum =""
      for i in s:
        hexnum +=  string.replace(hex(ord(i)),"0x","")  # generate string of random hex digits
      return hexnum
