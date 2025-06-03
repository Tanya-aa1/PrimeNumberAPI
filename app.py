#importing modules
from flask import Flask, request, jsonify


app = Flask(__name__)

#function to check whether a number is prime
def isPrime(n):
    if n <= 1:
        return False  # 0 and 1 are not prime
    for i in range(2, n):  #checking all numbers from 2 to n-1
        if n % i == 0:
            return False  #if divisible, not prime
    return True  #if no divisors found, it's prime

#api route '/check' that handles GET requests
@app.route('/check', methods=['GET'])
def Prime():
    try:
        #extracting 'num' parameter from query string, ensure it's an integer
        num = request.args.get('num', type=int)

        #if the parameter is missing or invalid, return a 400 Bad Request
        if num is None:
            return jsonify({"error": "Missing or invalid 'num' parameter"}), 400

        #calling the isPrime function to check prime number or not
        result = isPrime(num)

        #returning the result as a JSON response
        return jsonify({
            "number": num,
            "check_prime": result
        })

    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
