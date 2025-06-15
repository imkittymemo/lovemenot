class book:
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages
    def summary(self):
        print(f"{self.title},{self.author},{self.pages}")

b1 = book ("bealive" , "lannara", 7000)
b2 = book ("youbyyou", "isac", 500)


b1.summary()
b2.summary()