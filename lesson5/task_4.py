#  установил googletrans через pip install googletrans

from googletrans import Translator

with open("text_4.txt", "r", encoding="utf-8") as translate:
    f = open("text_4_1.txt", "w", encoding="utf-8")
    translator = Translator()
    for line in translate:
        result = translator.translate(line, dest='ru')
        print(result.text)
        print(result.text, file=f)
    f.close()
