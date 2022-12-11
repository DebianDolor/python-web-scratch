from http.server import BaseHTTPRequestHandler, HTTPServer
from sheet import read, create, delete, update
import time
import cgi
import json
import sqlite3 as lite
import re

####################### DATABASE OPERATING #####################################



def checkUser(username, password):
    con = lite.connect("./database/credential.db")
    with con:
        cur = con.cursor()
        cur.execute(
            "SELECT * FROM Users WHERE Username = ? AND Password = ?",
            (username, password),
        )
        rows = cur.fetchall()
        if len(rows) == 1:
            return (len(rows), rows[0][2])
        else:
            return (len(rows), 0)
    cur.close()
    con.close()
    del cur
    del con


def checkExisted(username):
    con = lite.connect("./database/credential.db")
    cur = con.cursor()
    cur.execute("SELECT username FROM Users WHERE Username=?", (username,))
    if cur.fetchone():
        return True
    return False
    cur.close()
    con.close()
    del cur
    del con


def addCredentials(username, password, options):
    con = lite.connect("./database/credential.db")
    insert = (username, password, options)
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Users WHERE Username = ?", (username,))
        rows = cur.fetchall()
        if len(rows) == 0:
            cur.execute("INSERT INTO Users VALUES(? , ? , ?)", insert)

    cur.close()
    con.close()
    del cur
    del con


def deleteUser(username):
    con = lite.connect("./database/credential.db")
    with con:
        cur = con.cursor()
        cur.execute("SELECT username FROM Users WHERE Username=?", (username,))
        if cur.fetchone():
            cur.execute("DELETE FROM Users WHERE Username = ?", (username,))
            return True
        else:
            return False

    cur.close()
    con.close()
    del cur
    del con

def updatePassword(username, password):
    con = lite.connect("./database/credential.db")
    with con:
        cur = con.cursor()
        cur.execute("SELECT username FROM Users WHERE Username=?", (username,))
        if cur.fetchone():
            cur.execute("UPDATE Users SET Password = ? WHERE Username = ?", (password, username,))
            return True
        else:
            return False
    cur.close()
    con.close()
    del cur
    del con

def getOnlyOneParam(url):
    map = re.split("[?&]", url)
    if len(map) <= 1:
        return None
    paramMap = re.split("=", map[1])
    if len(paramMap) <= 1:
        return None
    return paramMap[1]

def getParam(url):
    map = re.split("[?&]", url)
    if len(map) <= 1:
        return None
    username = re.split("=", map[1])
    password = re.split("=", map[2])
    if len(username) <= 1:
        return None
    return username[1], password[1]


#################################################################################


####################### SERVER'S IMPLEMENTATION #################################


class Server(BaseHTTPRequestHandler):
    def validateUser(self, username, password):
        return checkUser(username, password)

    def renderTemplates(self, file):
        try:
            f = open(file).read()
            if f:
                self.send_response(200)
                self.end_headers()
                self.wfile.write(bytes(f, "utf-8"))
            else:
                f = "File not found"
                self.send_error(404, f)
        except:
            f = "File not found"
            self.send_error(404, f)

    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.renderTemplates("./templates/index.html")
            self.path = "/index.html"

        else:
            self.send_response(301)
            self.send_header("Content-type", "text/html")
            self.send_header("Location", "/")
            self.end_headers()
            return

    def do_POST(self):
        form = cgi.FieldStorage(
            fp=self.rfile, headers=self.headers, environ={"REQUEST_METHOD": "POST"}
        )

        if self.path == "/create":
            self.send_response(200)
            self.end_headers()
            if create(form.getvalue("email"), form.getvalue("name")):
                res = {"success": "true"}
                self.wfile.write(bytes(json.dumps(res), "utf-8"))
            else:
                res = {"success": "false"}
                self.wfile.write(bytes(json.dumps(res), "utf-8"))

        if self.path == "/read":
            self.send_response(200)
            self.end_headers()
            sheet = read()
            self.wfile.write(bytes(json.dumps(sheet, indent=3), "utf-8"))

        if self.path == "/delete":
            self.send_response(200)
            self.end_headers()
            if delete(form.getvalue("email")):
                res = {"success": "true"}
                self.wfile.write(bytes(json.dumps(res), "utf-8"))
            else:
                res = {"success": "false"}
                self.wfile.write(bytes(json.dumps(res), "utf-8"))

        if self.path == "/update":
            self.send_response(200)
            self.end_headers()
            if update(form.getvalue("email"), form.getvalue("name")):
                res = {"success": "true"}
                self.wfile.write(bytes(json.dumps(res), "utf-8"))
            else:
                res = {"success": "false"}
                self.wfile.write(bytes(json.dumps(res), "utf-8"))

        if self.path == "/logout":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(bytes("data", "utf-8"))

        if self.path == "/":
            # Login
            if form.getvalue("options") == None:
                username = form.getvalue("username")
                password = form.getvalue("password")

                validate, options = self.validateUser(username, password)

                if validate == 1:
                    if options == 1:  # view info
                        self.send_response(200)
                        self.renderTemplates("./templates/logout.html")
                        output = ""
                        output += "<h1>Clients information</h1><br>"
                        output += (
                            "<strong>IP</strong>: "
                            + str(self.client_address[0])
                            + "<br>"
                        )
                        output += (
                            "<strong>Port</strong>: "
                            + str(self.client_address[1])
                            + "<br>"
                        )
                        output += "<strong>HTTP Request Method: </strong>POST" + "<br>"
                        output += (
                            "<strong>HTTP Request header: </strong>"
                            + str(self.headers)
                            + "<br>"
                        )
                        self.wfile.write(bytes(output, "utf-8"))

                    elif options == 2:  # sheet
                        self.send_response(200)
                        self.renderTemplates("./templates/sheet.html")
                else:
                    self.renderTemplates("./templates/loginFail.html")
            # Signup
            else:
                username_signup = form.getvalue("username_signup")
                password_signup = form.getvalue("password_signup")
                options = form.getvalue("options")

                if checkExisted(username_signup):
                    self.renderTemplates("./templates/signupFail.html")
                else:
                    addCredentials(username_signup, password_signup, options)
                    self.renderTemplates("./templates/index.html")

    def do_DELETE(self):
        username = getOnlyOneParam(self.path)

        # Login
        if deleteUser(username):
            self.send_response(200)
            self.end_headers()
            print("Success")
            return
        else:
            self.send_response(400)
            self.end_headers()
            print("Error")
            return

    def do_PUT(self):
        username, password = getParam(self.path)

        if updatePassword(username, password):
            self.send_response(200)
            self.end_headers()
            print("Success")
            return
        else:
            self.send_response(400)
            self.end_headers()
            print("Error")
            return


#################################################################################


################################## MAIN #########################################


def main():
    HOST_NAME = "localhost"
    PORT = 5000
    httpd = HTTPServer((HOST_NAME, PORT), Server)
    print(time.asctime(), "Start Server - %s:%s" % (HOST_NAME, PORT))
    try:
        httpd.serve_forever()

    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print(time.asctime(), "Stop Server - %s:%s" % (HOST_NAME, PORT))


if __name__ == "__main__":
    main()

#################################################################################
