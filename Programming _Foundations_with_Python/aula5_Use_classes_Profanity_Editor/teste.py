import urllib.request

path = "../docs/"
file_name = "movie_quotes.txt"

def read_text():
    quotes = open(path+file_name)
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    req = urllib.request.Request('http://www.wdylike.appspot.com/?q='+ urllib.request.quote(text_to_check))
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
        print(the_page)

read_text()