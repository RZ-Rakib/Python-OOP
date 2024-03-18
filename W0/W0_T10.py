import re

user_input = input("Insert word: ")
search_word = input("Insert search term: ")

search_term = re.escape(search_word)
search = re.search(search_term, user_input)

if search is not None:
    print(f"Search term '{search_term}' do appear in word '{user_input}'")
else:
    print(f"Search term '{search_term}' doesn't appears in word '{user_input}'")
