import json
import base64


def init():
    f = open("revershell.json","r")
    data = json.load(f)
    f.close()
    return data


current_list = init()

while True:
    lang = input("Language: ").lower()
    if lang == "exit":
        break

    content = open("test.txt","rb").read()

    if lang not in current_list:
        current_list[lang] = [base64.b64encode(content.strip()).decode("utf-8")]
    else:
        current_list[lang].append(base64.b64encode(content.strip()).decode("utf-8"))


# write to file
f = open("revershell.json","w")
json.dump(current_list,f)
f.close()



