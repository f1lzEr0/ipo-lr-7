#Kisel Artyom
import json
file1 = open("dump.json","r", encoding = "utf-8")
not_found = False
dump = json.load(file1)
number = int(input("Какую строку вы хотите выбрать?(1 - 733): "))
if number <733 and number>0:
    for arr_qual in dump:
        if arr_qual["pk"] == number and arr_qual["model"] == "data.skill":
            qual = arr_qual["fields"]["title"]
            qual_code = arr_qual["fields"]["code"]
            spec_n = arr_qual["fields"]["specialty"]
            break
    if not_found!=True:
        for arr_spec in dump:
            if arr_spec["pk"] == spec_n and arr_spec["model"] == "data.specialty":
                spec = arr_spec["fields"]["title"]
                spec_code = arr_spec["fields"]["code"]
                c_type = arr_spec["fields"]["c_type"]
        print(" Найдено ".center(50, "="))
        print(f"{qual_code} >> Специальность \"{spec}\", {c_type}" )
        print(f"{spec_code} >> Квалификация \"{qual}\"")
else:
    print(" Не найдено ".center(50, "=")) 
    file1.close()