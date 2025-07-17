# A two-dimensional list with 5 rows and 3 columns
books = [
    ['Attitude', 'John C Maxwell', 10.99],
    ['The Power of Now', 'Eckhart Tolle', 12.99],
    ['Atomic Habits', 'James Clear', 15.99],
    ['The Subtle Art of Not Giving a F*ck', 'Mark Manson', 14.99],
    ['Educated', 'Tara Westover', 13.99]
]

import pickle

with open('z_books.dat', 'wb') as file:
    pickle.dump(books, file)

