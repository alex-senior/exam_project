import os

file1 = "11-CE.txt"
file2 = "21-CE.txt"
print(os.getcwd())

#читання файлів
with open(file1, "r") as file:
  print("11-CE:\n", file.read(), "\n")
with open(file2, "r") as file:
  print("21-CE:\n", file.read(), "\n")
file.close()

#функція для перевірки, коли треба вийти з програми
def check(variable):
  match variable:
    case "exit":
      return exit(1)

while True:
  user_method = input("Введіть, що потрібно зробити з файлами: ")
  check(user_method)
  
  #запис даних у файли
  if user_method.startswith("write"):
    choose_num = input("Виберіть номер файлу для запису(1-2): ")
    check(choose_num)
    student = input("Ведіть ім'я студента та його середній бал: ")
    check(student)
    if (choose_num == '1'):
      with open(file1, "w") as file:
        file.writelines(student)
    elif (choose_num == '2'):
      with open(file2, "w") as file:
        file.writelines(student)
    file.close()

  #дозапис даних у файли
  elif user_method.startswith("add"):
    choose_num = input("Виберіть номер файлу для дозапису(1-2): ")
    check(choose_num)
    text = input("Введіть текст для дозапису: ")
    check(text)
    if (choose_num == '1'):
      with open(file1, "a") as file:
        file.writelines("\n" + text)
    elif (choose_num == '2'):
      with open(file2, "a") as file:
        file.writelines("\n" + text)
    file.close()
  
  #пошук файлів у каталозі та даних у файлі
  elif user_method.startswith("find"):
    print(os.listdir("groups"))
    choose_num = input("Виберіть номер файлу для пошуку(11-CE, 21-CE): ")
    check(choose_num)
    info = input("Введіть інформацію, яка вас цікавить: ")
    check(info)
    with open(f"groups/{choose_num}.txt", "r") as file:
      k = file.readlines()
      for index, item in enumerate(k):
        if (info in item):
          print("Інформація знайдена!")
      if(info not in item):
        print("Інформація не знайдена!")
    file.close()
  
  #сортування даних за середнім балом
  elif user_method.startswith("sort"):
    choose_num = input("Виберіть номер файлу для сортування(1-2): ")
    check(choose_num)
    if (choose_num == '1'):
      with open(file1, "r") as file:
        students = list(file.readlines())
        students.sort(key=lambda x: float(x.split()[1]), reverse=True)
        print(students)
    
    elif (choose_num == '2'):
      with open(file2, "r") as file:
        students = list(file.readlines())
        students.sort(key=lambda x: float(x.split()[1]), reverse=True)
        print(students)
  
  elif user_method.startswith("exit"):
    break