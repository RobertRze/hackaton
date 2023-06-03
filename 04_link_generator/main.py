import get_data

link_dict = {'https://helion.pl/': 'https://helion.pl/view/${id_from_user}',
             'https://helion.pl/ksiazki/algorytmy-ilustrowany-przewodnik-aditya-bhargava,algoip.htm#format/d': 'https://helion.pl/view/${id_from_user}/${book_title_form_file}.htm#format/d',
             'https://helion.pl/kategorie/promocja-2za1': 'https://helion.pl/page/${id_from_user}/promocja/promocja-2za1',
             'https://helion.pl/kategorie/programowanie': 'https://helion.pl/page/${id_from_user}/kategorie/programowanie'}



def add_links_to_code(code):
    while True:
        in_link, out_link = get_data.get_link_menu(link_dict, code)
#        out_link = get_data.generate_link(code, url, link_dict)
        get_data.save_link_to_file(in_link, out_link)
        next_link = input("Chcesz dodać kolejny link (t/n)")
        if next_link == 'n':
            return False


def main():
    code = get_data.get_code()
    add_links_to_code(code)



if __name__ == '__main__':
    main()
