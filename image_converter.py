import io
from PIL import Image
from flask import make_response

@app.route('/generate', methods=['GET', 'POST'])
def generate():
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
            'size': '1024x1024',
            'response_format': 'image/png'
        }
        response = requests.post('https://api.openai.com/v1/images/generations', headers=headers, json=data)
        image_data = response.content

        # Create a PIL image object from the image data
        image = Image.open(io.BytesIO(image_data))

        # Convert the image to PNG format with a transparent background
        image = image.convert('RGBA')
        new_image = Image.new('RGBA', image.size, (255, 255, 255, 0))
        new_image.paste(image, (0, 0), image)

        # Save the image to a byte stream
        buffer = io.BytesIO()
        new_image.save(buffer, format='PNG')
        image_bytes = buffer.getvalue()

        # Create a response object with the image bytes and the correct content type
        response = make_response(image_bytes)
        response.headers.set('Content-Type', 'image/png')
        response.headers.set('Content-Disposition', 'attachment', filename='app_icon.png')
        return response

    return render_template('generate.html')
