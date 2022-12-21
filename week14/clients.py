import argparse
import requests
import urllib3.request
import requests


def getArgs(argv=None):
    parser = argparse.ArgumentParser(description='Send request to a server')
    parser.add_argument('-d', '--data',type=str, help='HTTP POST/PUT data')
    requiredNamed = parser.add_argument_group('required named arguments')
    requiredNamed.add_argument('-m', '--method',type=str, help='Specify request method to use: HEAD, GET, POST, PUT, DELETE', required=True)
    requiredNamed.add_argument('-u', '--url',type=str, help='URL to work with', required=True)
    return parser.parse_args(argv)


def handling():
    argvals = None             
    args = getArgs(argvals)
    http = urllib3.PoolManager()

    if args.method == "HEAD":
        try:
            response = http.request(args.method, args.url)
            print(response.status)
        except Exception as e:
            print("The error raised is: ", e)

    elif args.method == "GET":
        try:
            response = http.request(args.method, args.url)
            print(response.data.decode("utf-8"))
        except Exception as e:
            print("The error raised is: ", e)

    elif args.method == "POST":
        try:
            data = []
            body = args.data.split("&")
            if len(body) < 2:
                print("Missing data! \nData must be passed in this format: 'username=?&password=?'")
                return
            
            for i in range(len(body)):
                data.append(body[i].split("="))

            if data[0][0] != "username":
                print("Invalid data! \nData must be passed in this format: 'username=?&password=?'")
                return
            if data[1][0] != "password":
                print("Invalid data! \nData must be passed in this format: 'username=?&password=?'")
                return
            data_request = {data[i][0]: data[i][1] for i in range(len(data))}

            response = http.request(args.method, args.url, fields=data_request)
            print(response.data.decode("utf-8"))
        except Exception as e:
            print("The error raised is: ", e)

    elif args.method == "DELETE":
        try:
            data = []
            if "&" in args.data:
                print("Invalid data! \nData must be passed in this format: 'username=?'")
                return
            
            data.append(args.data.split("="))

            if data[0][0] != "username":
                print("Invalid data! \nData must be passed in this format: 'username=?'")
                return

            response = requests.delete(args.url + "/?" + args.data)
            print(response)
        except Exception as e:
            print("The error raised is: ", e)

    elif args.method == "PUT":
        try:
            data = []
            body = args.data.split("&")
            if len(body) < 2:
                print("Missing data! \nData must be passed in this format: 'username=?&password=?'")
                return
            
            for i in range(len(body)):
                data.append(body[i].split("="))

            if data[0][0] != "username":
                print("Invalid data! \nData must be passed in this format: 'username=?&password=?'")
                return
            if data[1][0] != "password":
                print("Invalid data! \nData must be passed in this format: 'username=?&password=?'")
                return
            data_request = {data[i][0]: data[i][1] for i in range(len(data))}

            response = requests.put(args.url + "/?" + args.data, data_request)
            print(response)
        except Exception as e:
            print("The error raised is: ", e)

    else: 
        print("Method not supported. \nThe available methods are: HEAD, GET, POST, PUT, DELETE")
            

if __name__ == "__main__":
    handling()
