from ast import Try
from posixpath import split
import urllib3.request
import requests
import sys


def url_handling(agr, url):
    if agr == "-u":
        return url
    else:
        return "Syntax error url"


def method_handling(agr, method):
    if agr == "-m":
        return method
    else:
        return "Syntax error method"


def data_handling(arg, data):
    if arg == "-data":
        return data
    else:
        return "Syntax error data"


def handling():
    arg = sys.argv[1:]
    cmd = []

    if "-m" not in arg or "-data" not in arg or "-u" not in arg:
        print("Syntax error")
        return

    if len(arg) < 5 or len(arg) % 2 != 0:
        print("Syntax error")
        return

    for i in range(len(arg)):
        if i % 2 != 0:
            cmd.append((arg[i - 1], arg[i]))

    for i in range(len(cmd)):
        if cmd[i][0] == "-u":
            url = url_handling(cmd[i][0], cmd[i][1])
        elif cmd[i][0] == "-data":
            data = data_handling(cmd[i][0], cmd[i][1])
        elif cmd[i][0] == "-m":
            method = method_handling(cmd[i][0], cmd[i][1])
        else:
            print("Syntax error")
            return
    request_handling(method, data, url)


def request_handling(method, str, url):
    http = urllib3.PoolManager()

    if method == "HEAD":
        try:
            response = http.request(method, url)
            print(response.status)
        except:
            print("An exception occurred")

    elif method == "GET":
        try:
            response = http.request(method, url)
            print(response.data.decode("utf-8"))
        except:
            print("An exception occurred")

    elif method == "POST":
        try:
            data = []
            body = str.split("&")
            for i in range(len(body)):
                data.append(body[i].split("="))
            data_request = {data[i][0]: data[i][1] for i in range(len(data))}
            response = http.request(method, url, fields=data_request)
            print(response.data.decode("utf-8"))
        except:
            print("An exception occurred")

    elif method == "DELETE":
        try:
            if (str == ""):
              response = requests.delete("http://127.0.0.1:8686/")
              print(response)
            else:
              response = requests.delete("http://127.0.0.1:8686/?" + str)
              print(response)
        except Exception as e:
            print("An exception occurred")
            print(e)

    elif method == "PUT":
        try:
            data = []
            body = str.split("&")
            for i in range(len(body)):
                data.append(body[i].split("="))
            data_request = {data[i][0]: data[i][1] for i in range(len(data))}

            response = requests.put("http://127.0.0.1:8686/?" + str, data_request)
            print(response)
        except Exception as e:
            print("An exception occurred")
            print(e)


if __name__ == "__main__":
    handling()
