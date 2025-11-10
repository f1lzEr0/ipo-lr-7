#Kisel Artyom
import json

file1 = open("stars.json", "r+", encoding = "utf-8")
opened = json.load(file1)
end = False
while(end == False):
      print("1)Вывести все записи \n" \
            "2)Вывести запись по полю \n" \
            "3)Добавить запись \n" \
            "4)Удалить запись по полю \n" \
            "5)Выйти из программы")
      menu = int(input())
      if menu == 1:
            for field in opened:
                  print("-".center(50,"-"))
                  print("id:",field["id"])
                  print("name:",field["name"])
                  print("constellation:",field["constellation"])
                  print("is_visible:",field["is_visible"])
                  print("radius:", field["radius"])
                  print("-".center(50,"-"))
      elif menu == 2:
            num = int(input("Какую запись вы хотите вывести?: "))
            for field in opened:
                  if field["id"] == num:
                        print("-".center(50,"-"))
                        print("id:",field["id"])
                        print("name:",field["name"])
                        print("constellation:",field["constellation"])
                        print("is_visible:",field["is_visible"])
                        print("radius:", field["radius"])
                        print("-".center(50,"-"))
                        break
                  elif field["id"] == len(opened):
                        print("Запись не найдена".center(50,"-"))
      elif menu == 3:
            name = input("Введите общее название звезды: ")
            constelation = input("Введите название созвездия: ")
            is_visible = input("Видно ли звезду без телескопа (Да/Нет): ")
            if is_visible == "Да":
                  is_visible = True
            elif is_visible == "Нет":
                  is_visible = False
            else:
                  is_visible = "Не указано"
            radius = input("Введите солнечный радиус звезды: ")
            field_id = len(opened)+1
            new_note = {"id":field_id,
                        "name":name,
                        "constellation":constelation,
                        "is_visible":is_visible,
                        "radius":radius}
            opened.append(new_note)
            file1.close
            file_1 = open("stars.json", "w", encoding = "utf-8").close
            file1 = open("stars.json", "r+", encoding = "utf-8")
            json.dump(opened, file1, ensure_ascii=False,indent=4)
      elif menu == 4:
            for_delete = int(input("Какую запись удалить?: "))
            for index,field in enumerate(opened):
                  if field["id"] == for_delete:
                        opened.pop(index)
                        file1.close
                        file_1 = open("stars.json", "w", encoding = "utf-8").close
                        file1 = open("stars.json", "r+", encoding = "utf-8")
                        json.dump(opened, file1, ensure_ascii=False,indent=4)
                        break
                  elif field["id"] == len(opened):
                        print("Запись не найдена".center(50,"-"))
      elif menu == 5:
            end = True
            file1.close
            print("Программа завершена".center(100,"-"))