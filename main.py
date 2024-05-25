def main():
    with open('/home/bogdan18/workspace/books/frankenstein.txt') as file:
        file_contents = file.read()
        # Count Words
        word_count = count_words(file_contents)
        char_counts = count_char(file_contents)
        print_report('frankenstein.txt', word_count, char_counts)
        


def count_words(file_contents):
    words = file_contents.split()
    count = len(words)
    return count



def count_char(file_contents):
    lower_char = file_contents.lower()
    dict1 = {}
    for char in lower_char:
        if char.isalpha():

            if char in dict1:
                dict1[char] =  dict1[char]  + 1
            
            else:
                dict1[char] = 1

    return (dict1)

def print_report(filename, word_count, char_counts):
    char_list = [(char, count) for char, count in char_counts.items()]
    sorted_char_list = sorted(char_list, key=lambda x: x[1], reverse=True)
    # !!!!!!!!!!!!Header!!!!!!!!!!!
    print(f'---Begin report of {filename}---')
    print(f'{word_count} words counted in this file')

    for char, count in sorted_char_list:
        print(f'The {char} character was found {count} times ')
    
    print('---End Report---')

main()

