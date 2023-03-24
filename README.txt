# App Icon Generator

This is a web application that generates custom app icons using the OpenAI API. The user provides a prompt, and the app generates an image based on that prompt.

## Getting Started

To run this app on your local machine, follow these steps:

1. Clone this repository.
2. Create a virtual environment and activate it.
3. Install the required dependencies using `pip install -r requirements.txt`.
4. Create a `.env` file in the root directory and set your OpenAI API key as `OPENAI_API_KEY=<your_api_key>`.
5. Run the app using `python app.py`.
6. Open your web browser and go to `http://localhost:5000`.

## Usage

The web application has three pages:

1. Home page: Displays a brief description of the app and a button to go to the generate page.
2. Generate page: Allows the user to input a prompt and generates an app icon based on that prompt.
3. Customize page: Allows the user to customize the generated app icon and download it in various formats.

## Built With

* Flask - Python web framework
* Vue.js - JavaScript framework
* Bootstrap - Front-end framework
* OpenAI API - API for generating images based on text prompts

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
