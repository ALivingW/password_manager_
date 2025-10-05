import string

def encryption(msg):
    chars = " " + string.punctuation + string.ascii_letters + string.digits
    chars = list(chars)
    key = [" ", "X", "^", "$", "C", "W", "S", ";", "%", "(", "<", "s", "j", "T", "e", "a", "!", "u", "D", "E", '"', "*","}", "{", ")", "|", "h", "m", "P", "l", "Y", "O", "J", "M", "[", "y", ":", "i", "g", ".", "r", "n", "x", "V","L", "\\", "#", "b", "R", '"', "q", "A", ",", "K", "I", "d", "B", "U", "G", "&", "`", "c", "-", "H", "=","?", "+", "F", "k", "N", "@", "t", "_", ">", "z", "p", "o", "v", "f", "Z", "~", "/", "Q", "]", "w"]
    # encrypt
    cipher_txt = ""

    for letter in msg:
        index = chars.index(letter)
        cipher_txt += key[index]
    return cipher_txt