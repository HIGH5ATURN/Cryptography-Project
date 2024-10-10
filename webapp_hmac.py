from flask import Flask, request, jsonify, render_template
import hmac
import hashlib
import os

app = Flask(__name__)

# Generate a secret key
SECRET_KEY = os.urandom(32)

@app.route('/')
def home():
    return render_template('index.html')  # Make sure this matches your HTML filename

@app.route('/get_secret_key', methods=['GET'])
def get_secret_key():
    return jsonify({'secret_key': SECRET_KEY.hex()})

@app.route('/generate_hmac', methods=['POST'])
def generate_hmac():
    data = request.json.get('data', '')
    hmac_value = hmac.new(SECRET_KEY, data.encode(), hashlib.sha256).hexdigest()
    return jsonify({'hmac': hmac_value})

@app.route('/verify_hmac', methods=['POST'])
def verify_hmac():
    original_hmac = request.json.get('original_hmac', '')
    tampered_data = request.json.get('tampered_data', '')
    
    # Generate expected HMAC for the tampered data
    expected_hmac = hmac.new(SECRET_KEY, tampered_data.encode(), hashlib.sha256).hexdigest()

    # Compare the original HMAC with the expected HMAC
    is_verified = hmac.compare_digest(original_hmac, expected_hmac)

    # Log verification result for debugging
    print(f"Original HMAC: {original_hmac}, Expected HMAC: {expected_hmac}, Verified: {is_verified}")

    return jsonify({'verified': is_verified})

if __name__ == '__main__':
    app.run(debug=True)

