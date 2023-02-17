import argparse


parser = argparse.ArgumentParser()

parser.add_argument('file')
args = parser.parse_args()




def decode_Caesar_cipher(s, n):
    alpha = " ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',.?!"
    s = s.strip()
    text = ''
    for c in s:
        text += alpha[(alpha.index(c) + n) % len(alpha)]
    print(text)


filename = args.file
opened_file = open(filename)
encoded_text = str(opened_file.read())  # read the file into a string
opened_file.close()  # always close the files you've opened

decode_Caesar_cipher(encoded_text, int(-13))
