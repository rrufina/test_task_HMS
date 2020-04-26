# Test Task
## Endpoints:

1. User login:
[/accounts/login/](http://localhost:8000/accounts/login/).

2. User logout: 
[/accounts/login/](http://localhost:8000/accounts/login/).

3. List hotels (only for admin users):
[/hotel/info/hotels/](http://localhost:8000/hotel/info/hotels/).

4. List RoomCategory (only for hotel related users):
[/hotel/info/roomcategories/](http://localhost:8000/hotel/info/roomcategories/).

5. List Rooms (only for hotel related users):
[/hotel/info/rooms/](http://localhost:8000/hotel/info/rooms/).

6. List Bookings (only for hotel related users):
[/hotel/info/bookings/](http://localhost:8000/hotel/info/bookings/).

7. User (only for admin users):
[/hotel/info/users/](http://localhost:8000/hotel/info/users/).

To get access to admin panel you should go [here](http://127.0.0.1:8000/admin)
```
Username: admin
Password: admin12345
```

## Get the source code
Go to the directory you want to see this project in. Now you can get all the source code of this project using git clone command.
```
> git clone https://github.com/rrufina/test_task_HSM
```

## Deployment using Docker
### Change environmental variables
Now you can see example.env with such content inside it:
```
SECRET_KEY=your_django_secret_key_here
```
Put your django secret key here. If you don't have one, you can get it [here](https://djecrety.ir).
### Copy to .env
Now you need to copy the content of example.env to .env file. Use this:
```
> cp example.env .env
```
### Compose up
Now you need build our application, to do this use the following command:
```
> docker-compose up --build -d
```