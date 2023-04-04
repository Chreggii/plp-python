 ## Small Exercise


## Define a class called book
## everytime it is instantiated, it prints a comment like: 'Hi There!  I am a Book!' 
## The class definition should also take a number as an argument which shows the number of pages and a string for the title
## Define three methods called open, read, close  which print "Open/Read/Close the Book {name of book}"
## Everytime you console print the object, the printed line should contain the book title and the number of pages
## Implement a class named BookReader which can be used as a context manager. In the __enter__ method should open the book and the __exit__ method should close the book.

## Once you are done, run the code below and check if the book are properly opened and closed.

# book = Book(500, 'Harry Potter')
# with BookReader(book) as book:
#     book.read()



class Book:
    def __init__(self, pages,title):
        print('Hi There! I am a Book!')
        self.title = title
        self.pages = pages    

    def __str__(self):
        # return 'Book: ' + self.title + ' with ' + self.pages + 'pages'
        return 'Book: pages'+ str(self.pages) + 'with' + self.title + 'as a title'

    def  open(self):
        print('Open the Book ' + self.title)

    def read(self):
        print('Read the book ' + self.title)       

    def  close(self):
        print('Close the book ' + self.title)



class BookReader():
    def __init__(self, book):
        self.book = book

    def __enter__(self):
        self.book.open()
        return self.book

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.book.close()


book = Book(500, 'Harry Potter')

with BookReader(book) as book:
    book.read()

