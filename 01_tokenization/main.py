import tiktoken

enc = tiktoken.encoding_for_model("gpt-4o")

text= "Hey There! Rachit this side."
tokens = enc.encode(text)
print("tokens",tokens)
# print(enc.decode(tokens))
decoded=enc.decode([25216, 3274, 0, 460, 678, 278, 495, 4307, 13])
print("decoded",decoded)