import nltk
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download("words", quiet=True)
nltk.download("names", quiet=True)

from nltk.corpus import words, names

word_list = words.words()
name_list = names.words()

print(word_list)

def encrypt(plaintext, shift):
  """
  encode plaintext using a shift key
  """
  ciphertext = ""
  for char in plaintext:
    if char.isalpha():
      shift_num = ord(char) + shift
      if char.isupper():
        shift_num = shift_num % ord('Z') + ord('A') - 1
      else:
        shift_num = shift_num % ord('Z') + ord('A') - 1
      ciphertext += chr(shift_num)
    else:
      ciphertext += char
  return ciphertext


def decrypt(ciphertext, shift):
  """
  decrypt the cipher text using the shift key
  """
  pass


def crack(ciphertext):
  """
  decode an encrypted message without the key. use brute force, shift one letter at a time from 1-25 until the message is decoded
  """
  pass