# week14

### 1. Simple Web Server + 3. Google Sheet API

- Sau khi chạy file server.py và mở localhost:5000 thì sẽ hiện lên 1 form login:
    ![image.png](./image.png)

- Page `Signup` với option: `View Info` và `Sheet`:<br>
    ![image-5.png](./image-5.png)

- Sqlite DB gồm 3 cột: `username`, `password` và `option`:<br>
    ![image-1.png](./image-1.png)
    - Trường `option` nhận giá trị 1 tương ứng với `View Info` (exercise 1)
    - Giá trị 2 tương ứng `Sheet` (exercise 3)

- `View Info`:<br>
    ![image-2.png](./image-2.png)

- `Sheet`: <br>
    - `Read`:
        ![image-3.png](./image-3.png)
    - `Create`:
        ![image-4.png](./image-4.png)
    - Tương tự với `Update` và `Delete`


### 2. Simple client
- Cú pháp:
```
python clients.py -m <METHOD> -data <DATA> -u <url>
```
- METHOD: GET, POST, HEAD, PUT, DELETE.
- Với POST và PUT, cần cả `username` và `password`
- Với DELETE, chỉ cần `username`
- Ví dụ:
```
 python clients.py -m GET -data "/" -u "127.0.0.1:5000"
```
![image-6.png](./image-6.png)

```
python clients.py -m POST -data "username=admin&password=admin" -u "127.0.0.1:5000"

```
![image-7.png](./image-7.png)
```
python clients.py -m DELETE -data "username=admin" -u "127.0.0.1:5000"

```
![image-8.png](./image-8.png)
```
python clients.py -m PUT -data "username=123&password=123" -u "127.0.0.1:5000"

```
![image-9.png](./image-9.png)

- DB sau khi thực hiện các method trên:<br>
    ![image-10.png](./image-10.png)