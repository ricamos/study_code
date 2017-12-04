import urllib.request # https://stackoverflow.com/questions/45634187/i-keep-getting-http-error-400-bad-request-from-urlopen

# 1 Read the text
path = "../docs/"
file_name = "movie_quotes.txt"
def read_text():
    quotes = open(path+file_name)
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)

# 2 Check text for curse words
def check_profanity(text_to_check):
    connection = urllib.request.Request('http://www.wdylike.appspot.com/?q='+ urllib.request.quote(text_to_check))
    with urllib.request.urlopen(connection) as response:
        output = str(response.read()).strip().split("'")[1]
    print("\n")
    if "true" in output:
        print('Profanity Alert!!')
    elif 'false' in output:
        print('This document has no curse words!')

read_text()