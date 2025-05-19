from collections import defaultdict
ru_en = defaultdict(list)

with open("lab12/en-ru.txt", "r", encoding="utf-8") as file:
    for line in file:
        if "-" not in line:
            continue 
        en_word, ru_words = map(str.strip, line.split("-", 1))
        ru_list = [word.strip() for word in ru_words.split(",")]

        for ru_word in ru_list:
            if en_word not in ru_en[ru_word]:
                ru_en[ru_word].append(en_word)

with open("lab12/ru-en.txt", "w", encoding="utf-8") as file:
    for ru_word in sorted(ru_en):
        en_list = ", ".join(sorted(ru_en[ru_word]))
        file.write(f"{ru_word} – {en_list}\n")
