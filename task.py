def read_file(name_file: str) -> list:
    with open(name_file, 'r', encoding = 'utf-8') as content:
        lst_elements = [elements.rstrip() for elements in content]
    return lst_elements

def write_file(word: list):
    with open('a_result.txt', 'a', encoding = 'utf-8') as file:
        print(word, file = file)

def double_check_letters(word: str) -> bool:
    for letter in word:
        if word.count(letter) == 2:
            return False
    return True

def word_generation(words: list, letters: list) -> list:   
    words = [word for word in  words if double_check_letters(word)]
    for word in words:
        gener_word = ''.join(map(lambda letter: letter if letter in letters else '', list(word)))
        if gener_word == word:
            write_file(gener_word)
   

words = read_file('a_words.txt')
letters = read_file('a_letters.txt')
word_generation(words, letters)
