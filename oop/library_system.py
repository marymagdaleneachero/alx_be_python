class Book:
    def __init__(self, title:str, author:str):
        self.title = title
        self.author = author

class Ebook(Book):
    def __init__(self, title:str, author:str, file_size:int):
        super().__init__(title,author)
        self.file_size = file_size

class PrintBook(Book):
    def __init__(self, title:str, author:str, page_count:int):
        super().__init__(title,author)
        self.page_count = page_count


