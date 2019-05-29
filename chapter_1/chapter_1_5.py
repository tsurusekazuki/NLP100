s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
n_s = s.split()
words = {}
for i, c_s in enumerate(n_s):
    if i == 0 or i == 4 or i == 5 or i == 6 or i == 7 or i == 8 or i == 14 or i == 15 or i == 18:
        words[c_s[0]] = i + 1
    else:
        words[c_s[:2]] = i + 1
print(words)