# Defining the Book class
class Book():
    def __init__(self, title, author, pub_date, price, reader, category):
        self.title = title
        self.author = author
        self.pub_date = pub_date
        self.price = price
        self.reader = reader
        self.category = category

# Defining Sub classes 
class Young(Book):
    def __init__(self, title, author, pub_date, price, category=None):
        super().__init__(title, author, pub_date, price, "Young", category)

class Adult(Book):
    def __init__(self, title, author, pub_date, price, category=None):
        super().__init__(title, author, pub_date, price, 'Adult', category)