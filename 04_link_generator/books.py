def get_book_from_file(file):
    try:
        with open(file, 'r', encoding='utf-8') as rfile:
            return rfile.readlines()
    except FileNotFoundError as ferr:
        print("Pliku nie znaleziono:", ferr)

def get_books_list(link):
    books_list = get_book_from_file('books.txt')
    for i in range(len(books_list)):
        print(f"{i} - {books_list[i]}")
    book_id = int(input('Wybierz pozycję: '))
    in_url = str(link).replace('${book_title_form_file}', books_list[book_id])
    return in_url