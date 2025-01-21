import csv
import json
import random


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
    book_distribution = {}

    for book in books:
        user = random.choice(users)
        user_id = user["_id"]

        if user_id in book_distribution:
            book_distribution[user_id]['books'].append(book)
        else:
            book_distribution[user_id] = {
                "user_info": user,
                "books": [book]
            }

    output = []
    for user_id, data in book_distribution.items():
        user_info = data['user_info']
        distributed_books = data['books']
        output.append({
            "user": {
                "_id": user_info["_id"],
                "name": user_info["name"],
                "age": user_info["age"],
                "gender": user_info["gender"],
            },
            "books": distributed_books
        })

    return output


distributed_users = distribute_books(books, users)
with open('result.json', 'w', encoding='utf-8') as result_file:
    json.dump(distributed_users, result_file, ensure_ascii=False, indent=4)

json_result = json.dumps(distributed_users, ensure_ascii=False, indent=4)

print(json_result)

for user in distributed_users:
    print(f"{user['user']['name']} получит {len(user['books'])} книг.")