# Ethical Phishing Tool

## Description
This project demonstrates how phishing techniques can be used to capture webcam images and geolocation data. **This tool is intended for ethical purposes only, such as security research and education.**

## Features
- Access the user's webcam using the `getUserMedia()` API
- Capture still images from the webcam feed
- Fetch geolocation data using the `Geolocation API`
- Save data securely on the backend server
- Proper consent system before any data collection
- Organized storage of captured data

## Ethical Considerations
This tool demonstrates techniques used in phishing attacks for educational purposes only. Using similar techniques without explicit consent is:
- Illegal in most jurisdictions
- Unethical and violates personal privacy
- Potentially subject to severe legal penalties

## Technical Details
- Backend: Flask (Python)
- Frontend: HTML, CSS, JavaScript
- Data Storage: Local file system (captured_data directory)

## Setup

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Installation Steps
1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd camphishcreation
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. Install dependencies:
   ```bash
   pip install flask requests opencv-python flask-cors
   ```

4. Create a requirements.txt file:
   ```bash
   pip freeze > requirements.txt
   ```

## Usage
1. Start the application:
   ```bash
   python app.py
   ```

2. Access the application:
   - Open a web browser and navigate to `http://127.0.0.1:5000/consent`
   - Review and accept the consent terms
   - Authorize camera and location access when prompted
   - Captured data will be stored in the `captured_data` directory

## Project Structure
```
camphishcreation/
│
├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
│
├── static/                 # Static assets
│   └── style.css           # CSS styling
│
├── templates/              # HTML templates
│   ├── consent.html        # Detailed consent page
│   └── index.html          # Main application page
│
└── captured_data/          # Directory for storing captured data
    ├── webcam_*.jpg        # Captured webcam images
    └── geolocation_*.txt   # Captured location data
```

## Disclaimer
This tool is for **educational and research purposes only**. The authors are not responsible for any misuse of this tool or similar techniques. Always obtain proper consent before collecting any personal data.

## License
This project is provided for educational purposes only. Use responsibly.