import csv
import json


def read_books_from_csv(file_path):
    books = []
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            books.append(row)
    return books


users = [{'name': 'User1', 'books': []},
         {'name': 'User2', 'books': []},
         {'name': 'User3', 'books': []}]

file_path = 'books.csv'

books = read_books_from_csv(file_path)


def distribute_books(books, users):
    num_books = len(books)
    num_users = len(users)

    base_count = num_books // num_users
    remainder = num_books % num_users

    book_index = 0
    for user in users:
        user['books'] = books[book_index:book_index + base_count]
        book_index += base_count

        if remainder > 0:
            user['books'].append(books[book_index])
            book_index += 1
            remainder -= 1

    return users


distributed_users = distribute_books(books, users)

json_result = json.dumps(distributed_users, ensure_ascii=False, indent=4)

print(json_result)
