import pickle

with open('z_books.dat', 'rb') as f:
    books_list = pickle.load(f)
    print(books_list)
