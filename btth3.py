from fastapi import FastAPI

app = FastAPI()

books = [
    {
    "id": 1,
    "title": "Python for Beginners",
    "author": "John Doe",
    "category": "programming",
    "year": 2020,
    "is_available": True
    },
    {
    "id": 2,
    "title": "Database Design",
    "author": "Jane Smith",
    "category": "database",
    "year": 2019,
    "is_available": False
    },
    {
    "id": 3,
    "title": "Modern React Web",
    "author": "Dan Abramov",
    "category": "web",
    "year": 2021,
    "is_available": True
    },
    {
    "id": 4,
    "title": "TCP/IP Illustrated",
    "author": "Richard Stevens",
    "category": "network",
    "year": 2015,
    "is_available": False
    },
    {
    "id": 5,
    "title": "Clean Code",
    "author": "Robert C. Martin",
    "category": "programming",
    "year": 2008,
    "is_available": True
    },
    {
    "id": 6,
    "title": "FastAPI Basic",
    "author": "Nguyen Van A",
    "category": "web",
    "year": 2023,
    "is_available": True
    }
]

@app.get('/books/statistics')
def get_statistics():
    available_books = len([book for book in books if book.get('is_available') == True])
    borrowed_books = len(books) - available_books
    
    return {
        'total_books': len(books),
        'available_books': available_books,
        'borrowed_books': borrowed_books,
    }
    
@app.get('/books/categories')
def get_categories():
    list_categories = list(set([book.get('category') for book in books ]))
    
    return list_categories
    
    
@app.get('/books/latest')
def get_book_lastest():
    year_max = max([book.get('year') for book in books ])
    list_books  = []
    for book in books:
        if book.get('year') == year_max:
            list_books.append(book)
            
    return list_books