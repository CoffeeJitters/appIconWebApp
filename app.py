# Import necessary libraries
import os
import requests
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for

# Initialize the Flask app
app = Flask(__name__)

# Load environment variables from the .env file
load_dotenv()

# Define the app's routes
@app.route('/', methods=['GET', 'POST'])
def home():
    """
    Render the home page of the web application.

    GET request: Render the home.html template.
    POST request: Redirect to the generate endpoint.
    """
    if request.method == 'POST':
        return redirect(url_for('generate'))
    return render_template('home.html')

@app.route('/generate', methods=['GET', 'POST'])
def generate():
    """
    Render the generate page of the web application.

    GET request: Render the generate.html template.
    POST request: 
        - Retrieve the prompt text inputted by the user.
        - Send a POST request to the OpenAI API to generate an image based on the prompt.
        - Retrieve the image URL from the API response.
        - Render the result.html template with the generated image URL.
    """
    if request.method == 'POST':
        prompt = request.form['prompt']
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {os.environ["OPENAI_API_KEY"]}',
        }
        data = {
            'model': 'image-alpha-001',
            'prompt': f'{prompt}\n',
            'num_images': 1,
            'size': '256x256',
            'response_format': 'url'
        }
        response = requests.post('https://api.openai.com/v1/images/generations', headers=headers, json=data)
        image_url = response.json()['data'][0]['url']
        return render_template('result.html', image_url=image_url)
    return render_template('generate.html')

@app.route('/customize')
def customize():
    """
    Render the customize page of the web application.

    Render the customize.html template.
    """
    return render_template('customize.html')

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
