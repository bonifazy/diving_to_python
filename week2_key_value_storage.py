"""
put to storage, example:
key_value_storage.py --key key_1 --value 777 --value 3.14 --value 'hello!'
>> 777 3.14 hello!

get from storage, example:
key_value_storage.py --key key_1
>> 777 3.14 hello!
"""


import os
import json  # https://docs.python.org/3/library/json.html
import argparse  # https://docs.python.org/3/howto/argparse.html
# argparse https://habr.com/ru/post/144416
import tempfile  # https://docs.python.org/3/library/tempfile.html


parser = argparse.ArgumentParser()  # parse command line values
parser.add_argument('--key', type=str, dest='key')  # set key argument for work, only one value
parser.add_argument('--value', dest='value', action='append')  # set value arg, maybe > 1 values at once, type = list
args = parser.parse_args()  # get args from command line
key = args.key
value = args.value

data = dict()  # dict of storage data
storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')  # gettempdir is new idea for me

if not os.path.isfile(storage_path):  # first request to storage, new json file
    f = open(storage_path, 'w')
    f.close()
else:  # regular request (not first) to storage
    with open(storage_path) as f:
        if f.read():
            f.seek(0)
            data = json.load(f)  # convert data from json to python dict

if key and value:  # write to storage
    if key in data.keys():
        for i in value:
            if i not in data[key]:  # write new values by existing key
                data[key].append(i)
    else:  # write new key
        data[key] = value
    f = open(storage_path, 'w')
    json.dump(data, f)  # convert data from python dict to json
    f.close()
    for s in data[key][:-1]:  # from Coursera: "Обратите внимание на пробел после запятой."
        print(s, end=', ')
    print(data[key][-1])
elif key and not value and key in data.keys():  # read from storage
    for s in data[key][:-1]:  # from Coursera: "Обратите внимание на пробел после запятой."
        print(s, end=', ')
    print(data[key][-1])
else:  # no arguments in command line
    print(None)
