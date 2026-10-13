#!/usr/bin/env python3
alphabet = "abcdefghijklmnopqrstuvwxyz"
result = ""
i = 0
while i < len(alphabet):
    if alphabet[i] != 'e' and alphabet[i] != 'q':
        result += alphabet[i]
    i += 1
print(result)
