from flask import Flask, render_template, request
import json

import logging

# Configure the logger
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Use the logger instead of print






app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/location', methods=['POST'])
def location():
    data = json.loads(request.data)
    latitude = data['latitude']
    longitude = data['longitude']
    logger.info(f'Latitude: {latitude}, Longitude: {longitude}')
    return 'Success'

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)