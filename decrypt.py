import string

def decryption(cipher_txt):
    chars = " " + string.punctuation + string.ascii_letters
    chars = list(chars)
    key = [" ", "X", "^", "$", "C", "W", "S", ";", "%", "(", "<", "s", "j", "T", "e", "a", "!", "u", "D", "E", '"', "*",
           "}", "{", ")", "|", "h", "m", "P", "l", "Y", "O", "J", "M", "[", "y", ":", "i", "g", ".", "r", "n", "x", "V",
           "L", "\\", "#", "b", "R", '"', "q", "A", ",", "K", "I", "d", "B", "U", "G", "&", "`", "c", "-", "H", "=",
           "?", "+", "F", "k", "N", "@", "t", "_", ">", "z", "p", "o", "v", "f", "Z", "~", "/", "Q", "]", "w"]
    decrypted_msg = ""

    for letter in cipher_txt:
        index = key.index(letter)
        decrypted_msg += chars[index]
    return decrypted_msg