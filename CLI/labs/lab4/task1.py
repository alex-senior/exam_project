import random

label1 = ["Student", "Cat", "Girl"]
label2 = ["study", "play", "run"]
label3 = ["great", "yet", "good"]

for i in range(5):
    word1 = random.choice(label1)
    word2 = random.choice(label2)
    word3 = random.choice(label3)
    print(f"{word1} {word2} {word3}")