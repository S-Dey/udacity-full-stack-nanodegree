from urllib import parse, request


def read_text():
    text_to_read = open("some_text.txt")
    content = text_to_read.read()
    text_to_read.close()
    check_profanity(content)


def check_profanity(text_to_check):
    quoted_query = parse.quote(text_to_check)
    connection = request.urlopen("http://www.wdylike.appspot.com/?q="
                                + quoted_query)
    output = connection.read()
    print(output)
    connection.close()


read_text()
