from flask import Flask, jsonify, request
import random
import string

app = Flask(__name__)

# Generate a random 4-digit PIN
def generate_pin():
    pin = ''.join(random.choices(string.digits, k=4))
    return pin

@app.route('/generate_pin', methods=['POST'])
def generate_pin_api():
    data = request.get_json()
    username = data.get('username', '')
    pin = generate_pin()
    print(f"created with PIN: {pin}")
    # JSON format
    return jsonify({"username": username, "pin": pin})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)