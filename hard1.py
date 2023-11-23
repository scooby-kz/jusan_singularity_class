class library():
    books = []

    def add_book(self, book):
        self.books.append(book)
        print (f'{book} was added to library')

    def show_lib(self):
        return self.books

    def search_book(self, line):
        for el in self.books:
            if line in el or line in el.values():
                return f'найдена книга {el}'

mylib = library()
mylib.add_book({"JK" : "Harry Potter"})
mylib.add_book({"Tolkien" : "Rings"})

print(mylib.show_lib())
print(mylib.search_book("Rings"))