frase = "A rã arranha a aranha. Nem a aranha arranha a rã. Nem a rã arranha a aranha. Se percebeste, percebeste."
frase = frase.replace(".","")
frase = frase.lower()
frase = frase.split(" ")

print(frase)
words = {}
for palavra in frase :
    if palavra not in words.keys():
        words[palavra] = 1
    else:
        words[palavra] += 1

print(words)
