# week14

### 1. Simple Web Server
- Sau khi chạy file server.py và mở localhost:5000 thì sẽ hiện lên 1 form login
- Default credentials là: (admin, admin), (123, asd), (asd, asd)



### 2. Simple client
- Client sẽ là dạng một tool request nhỏ với cú pháp
```python
python clients.py -m <METHOD> -data <DATA> -u <url>
```
- Với METHOD: GET, POST, HEAD, PATCH, DELETE.
- Ví dụ:
```python
 python clients.py -m GET -data "/" -u "127.0.0.1:8686"

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.1/css/all.min.css" integrity="sha512-+4zCK9k+qNFUR5X+cKL9EIR+ZOhtIloNl9GIKS57V1MyNsYpYcUrUeQc9vNfzsWfV28IaLL3i96P9sdNyeRssA==" crossorigin="anonymous" />
    <title>Document</title>
    <script type="text/javascript">
      $(document).ready(function(){
        $('#Click_sign_up').click(function() {
          document.getElementById("login_form").style.display = 'none';
          document.getElementById("sign_up_form").style.display = 'block';
        });
        $('#Click_login').click(function() {
          document.getElementById("login_form").style.display = 'block';
          document.getElementById("sign_up_form").style.display = 'none';
        });
      });
    </script>

    .....
```

```python
python clients.py -m POST -data "username=admin&password=admin" -u "127.0.0.1:8686"

....
<div class="container px-4 px-md-5 text-lg-start my-2">
      <div class="row gx-lg-5 align-items-center mb-5">
        <div class="col-lg-6 mb-5 mb-lg-0 position-relative ">
          <div id="radius-shape-1" class="position-absolute rounded-circle shadow-5-strong"></div>
          <div id="radius-shape-2" class="position-absolute shadow-5-strong"></div>
          <div class="card bg-glass" style="width: 800px; height: 900px;">
            <div class="card-body px-4 py-5 px-md-5" id="load">
              <form action="" method="post">
                <button type="submit" id="Logout">Logout</button>
              </form>


<h1>Clients information</h1><br>Ip : 127.0.0.1<br>Port: 54906<br>HTTP Request Method: POST<br>HTTP Request header: Host: 127.0.0.1:8686
Accept-Encoding: identity
Content-Length: 226
Content-Type: multipart/form-data; boundary=38a1ba00bf57b7d0218eeb45ea2e9f71
User-Agent: python-urllib3/1.26.9

<br>HTTP/1.0 200 OK
Server: BaseHTTP/0.6 Python/3.10.4
Date: Tue, 26 Apr 2022 04:51:04 GMT

</div>

....
```

### 3. Google Sheet API

- Sau khi đăng nhập tài khoản isAdmin = 2 sẽ hiện 1 form CRUD.
![Screenshot 2022-04-26 115307](https://i.imgur.com/hVktocU.png)
- Cứ thao tác bình thường thôi.![Screenshot 2022-04-26 115416](https://i.imgur.com/Wpe8iFt.png)


