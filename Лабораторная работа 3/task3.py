def count_letters(text):
    text = text.lower()
    letter_counts = {}
    order = []

    for char in text:
        if char.isalpha():
            if char not in letter_counts:
                letter_counts[char] = 1
                order.append(char)
            else:
                letter_counts[char] += 1

    return letter_counts, order

def calculate_frequency(letter_counts, order):
    total = sum(letter_counts[char] for char in order)
    frequency = {}
    for char in order:
        frequency[char] = round(letter_counts[char] / total, 2)
    return frequency

main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

counts, order = count_letters(main_str)
freqs = calculate_frequency(counts, order)

for char in order:
    print(f"{char}: {freqs[char]:.2f}")
