from Languages import rus, eng
import keyboard as kb

text = input('Введите текст: ') # Убрать

def translation(text):
    for i in text:
        if i in eng and i not in rus:
            layout = dict(zip(map(ord, eng), rus)) # ENG --> RU
        elif i in rus and i not in eng:
            layout = dict(zip(map(ord, rus), eng)) # RU --> ENG
        return text.translate(layout)

print(translation(text))

