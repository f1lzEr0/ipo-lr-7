#Kisel Artyom
books = [{"title":"Десять негритят","Author":"Агата Кристи","year":"1939"},
          {"title":"Крокодил Гена и его друзья","Author":"Эдуард Успенский","year":"1970"},
          {"title":"Отпуск крокодила Гены","Author":"Эдуард Успенский","year":"1974"},
          {"title":"Будь нужным: Семь правил жизни","Author":"Арнольд Шварцнегер","year":"2023"},
          {"title":"Денискины рассказы","Author":"Виктор Драгунский","year":"1990"}]
for number, book in enumerate(books):
    number+=1
    print(f"Книга {number}".center(70,"-"))
    print(f"Название: {book["title"]}, Автор: {book["Author"]}")
    print(book["year"].center(70,"-"),"\n")