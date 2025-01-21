import csv
import json


def read_users_from_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        users = json.load(file)
    return users


def read_books_from_csv(file_path):
    books = []
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            books.append(row)
    return books


file_path_users = 'users.json'
file_path_books = 'books.csv'

books = read_books_from_csv(file_path_books)
users = read_users_from_json(file_path_users)


def distribute_books(books, users):
    num_books = len(books)
    num_users = len(users)

    base_count = num_books // num_users
    remainder = num_books % num_users

    book_index = 0
    for i, user in enumerate(users):
        count_for_user = base_count + (1 if i < remainder else 0)
        user['books'] = books[book_index:book_index + count_for_user]
        book_index += count_for_user

    return users


distribute_books(books, users)
distributed_users = distribute_books(books, users)
with open('result.json', 'w', encoding='utf-8') as result_file:
    json.dump(distributed_users, result_file, ensure_ascii=False, indent=4)

json_result = json.dumps(distributed_users, ensure_ascii=False, indent=4)

print(json_result)

for user in users:
    print(f"{user['name']} получит {len(user['books'])} книг.")
