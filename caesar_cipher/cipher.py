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

combined_list = (word_list + name_list)
reference_list = [word.lower() for word in combined_list]


def encrypt(plaintext, shift):
  """
  encode plaintext using a shift key
  """
  ciphertext = ""
  for char in plaintext:
    shift_num = shift % 26
    if char.isalpha():
      char_ord = ord(char) + shift_num
      if char.isupper():
        if char_ord < 65:
          char_ord += 26
        elif char_ord > 90:
          char_ord -= 26
      elif char.islower():
        if char_ord < 97:
          char_ord += 26
        elif char_ord > 122:
          char_ord -= 26

      ciphertext += chr(char_ord)
      # print(char_ord)
    else:
      ciphertext += char    
  # print(ciphertext)
  return ciphertext
  

def decrypt(ciphertext, shift):
  """
  decrypt the cipher text using the shift key
  """
  # print(encrypt(ciphertext, (shift * -1)))
  return encrypt(ciphertext, (shift * -1))


def crack(ciphertext):
  """
  decode an encrypted message without the key. use brute force, shift one letter at a time from 1-25 until the message is decoded
  """
  for shift in range(26):
    decrypted_phrase = decrypt(ciphertext, shift)
    test_phrase = decrypted_phrase.split()

    if all(word.lower() in reference_list for word in test_phrase if word.isalpha()):
      return ' '.join(test_phrase)
  
  return ''


if __name__ == "__main__":
  print(encrypt('hello world', 5))
  print(decrypt('mjqqt btwqi', 5))
  print(crack('It was the best of times, it was the worst of times.'))

