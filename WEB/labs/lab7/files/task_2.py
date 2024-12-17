import matplotlib.pyplot as plt

filename = 'CLI/labs/lab7/files/text.txt'
def count_letters(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
    count = {} 
    for letter in text: 
        if letter.isalpha(): 
            letter = letter.lower() 
            if letter in count: count[letter] += 1 
            else: count[letter] = 1 
    return count

count = count_letters(filename)
letters = list(count.keys()) 
counts = list(count.values())

plt.figure(figsize=(10, 6))
plt.title('Частота появи літер у тексті') 
plt.bar(letters, counts, color='skyblue')
plt.xlabel('Літери') 
plt.ylabel('Частота') 
plt.grid(axis='y')
plt.savefig("gist_letters.png")
plt.show()