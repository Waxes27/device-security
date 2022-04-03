import json
import os


filters = ["WAN","Type","System","product","v4",'mac']


def recursive_finder(json):
    new_json = {}

    def rfind(json):
        for i in json:
            if str(type(i)) == "<class 'dict'>":
                rfind(i)
            else:
                for _filter in filters:
                    if _filter in i:
                        new_json[_filter] = json[i]

        return new_json



    for i in json:
        rfind(json[i])

    return new_json


with open("config/config.json","r") as f:
    new_json = {}
    content = f.read();
    
    data = json.loads(content)
    data_to_write = json.dumps(recursive_finder(data))
    with open("config/config.json","w") as f:
        f.write(data_to_write)

        