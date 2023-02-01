from bs4 import BeautifulSoup
import requests
import csv
from book_info import book_Data
import time


def get_book_codes(book_list):
    book_codes = []
    for book in book_list:
        url = f'https://www.goodreads.com/search?utf8=%E2%9C%93&q={book}&search_type=books'
        response = requests.get(url)
        html_text = response.content

        soup = BeautifulSoup(html_text, 'html.parser')
        link = soup.find('a', class_='bookTitle', href=True)['href']
        b = link.split('/')[3]
        book_code = b.split('?')[0]
        book_codes.append(book_code)
    return book_codes


def get_book_info(book_codes):
    b_list = {}
    for num, b in enumerate(book_codes):
        s = requests.session()
        url = f'https://www.goodreads.com/book/show/{b}'
        response = s.get(url)
        response_text = response.text
        soup = BeautifulSoup(response_text, 'html.parser')
        book = book_Data(soup)
        time.sleep(5)
        try:
            book.get_title()
        except:
            b_list[num] = f'No data was found for {b}'
        else:
            json = {
                'title': book.get_title(),
                'book_ID': b,
                'author(s)': book.get_author(),
                'year_published': book.get_year(),
                'rating': book.get_rating(),
                'rating_count': book.ratings_count(),
                'rating distribution': book.rating_distribution(),
                'genres': book.get_genres(),
                'cover_img': book.book_cover(),
                'url_link': url
                            }
            b_list[num] = json
            s.cookies.clear()
    return b_list


with open("books.csv", 'r') as file:
    csv_reader = csv.reader(file)
    book_list = [book[0] for book in csv_reader]
    b_codes = get_book_codes(book_list=book_list)
    print(b_codes)
    j = get_book_info(book_codes=b_codes)
    print(j)
