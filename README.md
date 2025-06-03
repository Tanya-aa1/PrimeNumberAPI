# Prime Number Checker API

This is a basic **backend API** built using **Flask** that checks whether a given number is a prime number or not.

# Features
1. Accepts a number via a query parameter (num)
2. Returns a JSON response indicating if the number is prime or not
3. Includes basic input validation and error handling

# Logic Used
The app uses a simple isPrime(n) function to check whether the number is divisible by any number between 2 and n-1.

# How to Install Dependencies
```bash
pip install flask
```
# How to Run
1. Clone the Repository (or copy the file)
```bash
git clone https://github.com/Tanya-aa1/PrimeNumberAPI.git
cd PrimeNumberAPI
```
2. Run the flask app
```bash
python app.py
```
The server will start at http://127.0.0.1:5000

# How to Test Endpoint
Once the server is running:
Check if a number is prime

Open your browser or use a tool like Postman and send a GET request to:
```bash
http://127.0.0.1:5000/check?num=7
```
# Sample Outputs
![image](https://github.com/user-attachments/assets/4ca93fc4-bd02-490e-98f4-f57cda8c215a)
![image](https://github.com/user-attachments/assets/85cb5b05-223f-44fa-9d1f-bdc3e81cd511)
