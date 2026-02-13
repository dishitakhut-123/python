words = ["  Python ", " AI ", "Machine ", " Data "]
def lower(words):
    return words.lower()
def uppercase(words):
    return words.upper().strip()
out1=list(map(lower,words))
out2=list(map(uppercase,words))
print(out1,out2)
