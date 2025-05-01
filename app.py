from flask import Flask, render_template, request, jsonify
import os
import base64
import datetime

app = Flask(__name__)

# Create a directory to store captured data if it doesn't exist
os.makedirs('captured_data', exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/capture', methods=['POST'])
def capture():
    data = request.json
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Save geolocation data
    if 'lat' in data and 'lon' in data:
        with open(f'captured_data/geolocation_{timestamp}.txt', 'w') as f:
            f.write(f"Latitude: {data['lat']}\n")
            f.write(f"Longitude: {data['lon']}\n")
    
    # Save webcam image if provided
    if 'image' in data:
        # Remove the data URL prefix to get just the base64 data
        image_data = data['image'].split(',')[1]
        with open(f'captured_data/webcam_{timestamp}.jpg', 'wb') as f:
            f.write(base64.b64decode(image_data))
    
    return jsonify({'status': 'success', 'message': 'Data captured successfully'})

@app.route('/consent')
def consent_page():
    return render_template('consent.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)