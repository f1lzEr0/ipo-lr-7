#Kisel Artyom Вариант3
import json
def star_information():
      print("-".center(50,"-"))
      print("id:",field["id"])
      print("name:",field["name"])
      print("constellation:",field["constellation"])
      print("is_visible:",field["is_visible"])
      print("radius:", field["radius"])
      print("-".center(50,"-"))

def rewrite(file_name):
      file1 = open(file_name, "w", encoding = "utf-8").close
      file1 = open(file_name, "r+", encoding = "utf-8")
      json.dump(opened, file1, ensure_ascii=False,indent=4)

def is_visible_(a):
      ans = {"Да":True,"Нет":False}
      return ans[a] 

def menu():
      switch = 0
      print("1)Вывести все записи \n" \
            "2)Вывести запись по полю \n" \
            "3)Добавить запись \n" \
            "4)Удалить запись по полю \n" \
            "5)Выйти из программы")
      switch = int(input())
      return switch

file1 = open("stars.json", "r+", encoding = "utf-8")
opened = json.load(file1)
while(True):
      switch = menu()
      if switch == 1:
            for field in opened:
                  star_information()
      elif switch == 2:
            num = int(input("Какую запись вы хотите вывести?: "))
            for field in opened:
                  if field["id"] == num:
                        star_information()
                        break
                  elif field["id"] == len(opened):
                        print("Запись не найдена".center(50,"-"))
      elif switch == 3:
            name = input("Введите общее название звезды: ")
            constelation = input("Введите название созвездия: ")
            visibility = input("Видно ли звезду без телескопа (Да/Нет): ")
            try: 
                  is_visible = is_visible_(visibility)
            except: 
                  is_visible = "Не определено"
            radius = input("Введите солнечный радиус звезды: ")
            field_id = len(opened)+1
            new_note = {"id":field_id,
                        "name":name,
                        "constellation":constelation,
                        "is_visible":is_visible,
                        "radius":radius}
            opened.append(new_note)
            rewrite("stars.json")
      elif switch == 4:
            for_delete = int(input("Какую запись удалить?: "))
            for index,field in enumerate(opened):
                  if field["id"] == for_delete:
                        opened.pop(index)
                        rewrite("stars.json")
                        break
                  elif field["id"] == len(opened):
                        print("Запись не найдена".center(50,"-"))
      elif switch == 5:
            file1.close
            print("Программа завершена".center(100,"-"))
            break