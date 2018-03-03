import urllib.request as urllib

def read_text():
    text_to_read = open("some_text.txt")
    content = text_to_read.read()
    text_to_read.close()
    check_profanity(content)

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=" + text_to_check)   
    output = connection.read()
    print(output)
    connection.close()

read_text()