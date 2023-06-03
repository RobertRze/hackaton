import random
import menu, logic


def main():
    fill_word_result = logic.fill_word()
    count = fill_word_result[0].count('-')
    word = fill_word_result[1]
    if count > 0:
        print(f'Przegrałeś. Słowo do odgadnięcia: {word}')
    else:
        print('Wygłałeś')

main()
