class Book():
    name=''
    author=''
    date=''

    def info(self):
        print(self.name,self.author,self.date,sep='\n')

harrypotter = Book()
harrypotter.name='Harry Potter'
harrypotter.author='JJ Rowling'
harrypotter.date='2000'

harrypotter.info()