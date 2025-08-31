from gensim.models import Word2Vec

# Podaci
with open("podaci.txt", "r", encoding="utf-8") as f:
    data = f.read().splitlines()

import string

# Uklanjanje interpunkcije iz rečenica
data = [sentence.translate(str.maketrans("", "", string.punctuation)) for sentence in data]

# Tokenizacija
data = [sentence.lower().split() for sentence in data]

# Treniranje modela
model = Word2Vec(sentences=data, vector_size=100, window=3, min_count=3, workers=4)

# Primjeri
print("Slične riječi 'vjetar':")
print(model.wv.most_similar("vjetar"))

print("Slične riječi 'temperaturi':")
print(model.wv.most_similar("temperaturi"))

print("\n Vektor riječi 'sunčano':")
print(model.wv["sunčano"])

print("\n Izbaci uljeza: 'proljeće', 'pretežno', 'sunčano'")
print(model.wv.doesnt_match(['proljeće', 'pretežno', 'sunčano']))

print("\n Sličnost 'suhi' i 'zrak':")
print(model.wv.similarity("suhi", "zrak"))

print("\n Sličnost 'jasno' i 'zrak':")
print(model.wv.similarity("jasno", "zrak"))

print("\n Koja riječ je za sunčano kao što je suhi za zrak")
print(model.wv.most_similar(positive=["sunčano", "suhi"], negative=["zrak"], topn=3))

print("\n Postoji li riječ magla?")
print("magla" in model.wv.key_to_index)

print("\n Postoji li riječ dinosaur?")
print("dinosaur" in model.wv.key_to_index)