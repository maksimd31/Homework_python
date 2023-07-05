# 📌 Вспоминаем задачу 3 из прошлого семинара. Мы сформировали текстовый файл с псевдо именами и произведением чисел.
# 📌 Напишите функцию, которая создаёт из созданного ранее файла новый с данными в формате JSON.
# 📌 Имена пишите с большой буквы.
# 📌 Каждую пару сохраняйте с новой строки.


import json

__all__ = ['write_json']


def write_json(filename):
    with (open(filename, "r", encoding="utf-8") as res,
          open("output.json", "w", encoding="utf-8") as j):
        dict_res = dict()
        for item in res:
            key, value = item.replace("\n", "").split((" "))
            dict_res[key.capitalize()] = value
        # json_res =json.dumps(dict_res,indent=1,ensure_ascii=False)
        json.dump(dict_res, j, ensure_ascii=False, indent=1)
        # j.write(json_res)


if __name__ == '__main__':
    filename = 'result.txt'
    write_json(filename)
