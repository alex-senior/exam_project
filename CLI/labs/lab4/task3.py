import re

filepath="CLI/labs/lab4/city.txt"
with open(filepath, "r", encoding='utf-8') as file:
    read = file.read()
    words = read.split()
    lenght_word = [len(word) for word in words]
    max_lenght = max(lenght_word)
    min_lenght = min(lenght_word)
    avg_lenght = sum(lenght_word) / len(lenght_word)
    print("Максимальна довжина слова: ", max_lenght, "\nМінімальна довжина слова: ", min_lenght, "\nСередня довжина слова: ", avg_lenght, '\n')
file.close()

with open(filepath, "r", encoding='utf-8') as file:
    text = file.read()
    sentences = re.split(r'(?<=[.!?]) +', text)
    sentence_lengths = [len(sentence) for sentence in sentences]
    max_sentence = max(sentence_lengths)
    min_sentence = min(sentence_lengths)
    avg_sentence = sum(sentence_lengths) / len(sentence_lengths)
    print("Максимальна довжина речення: ", max_sentence, "\nМінімальна довжина речення: ", min_sentence, "\nСередня довжина речення: ", avg_sentence, '\n')
file.close()

with open(filepath, "r", encoding='utf-8') as file:
    city = file.read()
    paragraphs = text.split('\n\n')
    lenght_paragraphs = [len(paragraph) for paragraph in paragraphs]
    max_par = max(lenght_paragraphs)
    min_par = min(lenght_paragraphs)
    avg_par = sum(lenght_paragraphs) / len(lenght_paragraphs)
    print("Максимальна довжина абзацу: ", max_par, "\nМінімальна довжина абзацу: ", min_par, "\nСередня довжина абзацу: ", avg_par)
file.close()