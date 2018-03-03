def read_text():
    quotes = open("some_text.txt")
    contents = quotes.read()
    print(contents)
    quotes.close()

read_text()