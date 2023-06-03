def select_category():
    while True:
        try:
            category = input("""Podaj kategorię:
        1 - kategoria zwierzęta
        2 - owoce
        3 - warzywa: """)
            return read_from_file()[int(category) - 1]
        except ValueError:
            print('Niepoprawna wartość. Spróbuj jeszcze raz')
        except IndexError:
            print("Wartość z poza zakresu. Spróbuj jeszcze raz")

def read_from_file():
    with open('word_list.txt', encoding='utf-8') as wfile:
        return wfile.readlines()


def check_letter(mask_word, word, tries_number, used_letters):
    num = 0
    while num == 0:
        letter = input(f'Liczba prób {tries_number}. Podaj literę: ')
        num = word.count(letter)
        if letter in used_letters:
            print('BYŁO')
        elif num > 0:
            print("Trafione!")
            print_word(mask_word, word, letter)
            return letter
        else:
            print('Nie trafione, spróbuj jeszcze raz')
            return letter
#            return mask_word, letter


def print_word(mask_word, word, letter):
    i = 0
    for i in range(len(word)):
        if word[i] == letter:
            mask_word[i] = letter
    return mask_word

def show_word(mask_word):
    format_word = ''
    for i in range(len(mask_word)):
        format_word += mask_word[i]
        i += 1
    return format_word

def check_word(word, mask_word):
    user_word = input("Podaj słowo: ")
    if word == user_word:
        return word
    else:
        print("Pudło")
        return mask_word

def guess_word(mask_word, word, tries_number):
    guess_word_choice = 'x'
    while guess_word_choice != 't' or guess_word_choice != 'n':
        guess_word_choice = input("Chcesz spóbować odgadąć słowo (t - koszuje 2 próby)? (t/n): ")
        if guess_word_choice == 't':
            return check_word(word, mask_word), tries_number - 2
        elif guess_word_choice == 'n':
            return mask_word, tries_number
        else:
            print('Niepoprawna wartość')
