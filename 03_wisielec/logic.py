import menu, random, draw

def fill_word():
    number_of_tries = 14
    used_letters = []
    word_list = menu.select_category().split(",")
    word = word_list[random.randint(0, len(word_list) - 1)].strip()
    word_size = len(word)
    mask_word = len(word) * '-'
    print(mask_word)
    mask_word = list(mask_word)
    i = 0
    while mask_word.count('-') > 0 and i < number_of_tries:
        tries_number = number_of_tries - i
        letter = menu.check_letter(mask_word, word, tries_number, used_letters)
        used_letters.append(letter)
        print("Użyte litery: ", used_letters)
        draw.draw(i)
        print(menu.show_word(mask_word))
        if mask_word.count('-') > 0:
            guest_word_result = menu.guess_word(mask_word, word, tries_number)
            mask_word = guest_word_result[0]
            i = number_of_tries - guest_word_result[1]
            print(menu.show_word(mask_word))
            i += 1
    return menu.show_word(mask_word), word