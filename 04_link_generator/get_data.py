import re, books

link_dict = {'https://helion.pl/': 'https://helion.pl/view/${id_from_user}',
             'https://helion.pl/ksiazki/${book_title_form_file}.htm#format/d': 'https://helion.pl/view/${id_from_user}/algoip',
             'https://helion.pl/kategorie/promocja-2za1': 'https://helion.pl/page/${id_from_user}/promocja/promocja-2za1',
             'https://helion.pl/kategorie/programowanie': 'https://helion.pl/page/${id_from_user}/kategorie/programowanie'}


def get_code():
    while True:
        try:
            id = int(input('Podaj 5 cyfrowy kod: '))
            if len(str(id)) == 5:
                return id
            else:
                print("Kod powinień składać się z 5 cyfr. Spróbuj jeszcze raz")
        except ValueError as verr:
            print("Nieprawidłowa wartość. Spróbuj jeszcze raz")

def get_link():
    url_pattern = "https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,}"
#    url_pattern = "https?:\/\/|http?:\/\/"
    while True:
        in_url = input("Podaj link: ")
        if re.match(url_pattern, in_url):
            return in_url
        else:
            print("Podaj właściwy link")


def get_link_menu(link_dict, code):
    url_pattern = "https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,}"
#    url_pattern = "https?:\/\/|http?:\/\/"
    while True:
        try:
            index = int(input("""Podaj link wejściowy: 
            Strona główna - 0
            Strona produktu - 1
            Strona promocji - 2
            link do kategorii programowanie - 3
            """))
            in_url = list(link_dict.keys())[index]
            if index == 1:
                out_url = books.get_books_list(in_url)
                return in_url, out_url
            if re.match(url_pattern, in_url):
                return in_url, generate_link(code, in_url, link_dict)
            else:
                print("Podaj właściwy link")
        except IndexError:
            print("Wartość z poza zakresu. Spróbuj jeszcze raz")

# print(get_code())


def generate_link(id, link, link_dict):

    for in_url in link_dict:
        if in_url == link:
            out_link_pattern = link_dict[in_url]
            out_link = out_link_pattern.replace('${id_from_user}', str(id))
#            print(f"Link: {out_link}")
            return out_link


def save_link_to_file(in_link, out_link):
    with open('links.txt', 'a', encoding='utf-8') as wfile:
        wfile.write(f"\n {in_link} -- {out_link}")


#print(get_link_menu(link_dict))
#print(generate_link(123, 'https://helion.pl/'))
#print(generate_link(12345, 'https://helion.pl/ksiazki/algorytmy-ilustrowany-przewodnik-aditya-bhargava,algoip.htm#format/d'))
