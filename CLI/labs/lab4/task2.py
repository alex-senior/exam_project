import string

filepath="CLI/labs/lab4/city.txt"
#part 1
with open(filepath, "r", encoding='utf-8') as file:
    read = file.read()
    print("Кількість символів з пробілами: ", len(read))
with open(filepath, "r", encoding='utf-8') as file:
    read = file.read()
    print("Кількість символів без пробілів: ", len(read.replace(" ", "")))

#part 2
with open(filepath, "r", encoding='utf-8') as file:
    read = file.read().split()
    print("Кількість слів у тексті: ", len(read))
    print("Кількість різних слів: ", len(set(read)))

def count(filepath):
    with open(filepath, "r", encoding='utf-8') as file:
        read = file.read()
        translator = str.maketrans('','', string.punctuation)
        read = read.translate(translator).lower()
        words = read.split()
        unique_words = set(words)
    return len(unique_words)
print("Кількість унікальних слів: ", count(filepath))