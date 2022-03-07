# API to list and find books 

# Installation
git clone https://github.com/geeknabil/book.git
cd book
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver


# Routes
http://127.0.0.1:8000/api/books/  to get [GET] all books (paginated 2 books/page) also create [POST] new book.
http://127.0.0.1:8000/api/books/id  to get [GET] specific book by it's id also update [PUT] or delete [DELETE] this book. 
http://127.0.0.1:8000/api/findbook  to get [GET], filter and search books by multiple genres. (to test use Postman or Thunder Client) pass genre params and it's values to request body. 
