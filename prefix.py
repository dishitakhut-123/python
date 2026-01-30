#find longest prefix
#input =['flower','flow','flight]
#result=fl
words = ['flower', 'flow', 'flight']

if not words:
    prefix = ""
else:
    prefix = words[0]

    for word in words[1:]:
        while not word.startswith(prefix):
            prefix = prefix[:-1]
            if prefix == "":
                break

print("Longest common prefix:", prefix)
