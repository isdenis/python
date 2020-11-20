word = input("Введите несколько слов: ")
word_split = word.split()
word_split_limit = []

for a in word_split:
    word_split_limit.append(a[:10])

for b in enumerate(word_split_limit):
    print(b)
