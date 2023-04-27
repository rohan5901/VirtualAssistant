# Virtual Assistant

This is a virtual assistant built using Python and Tkinter. The assistant can perform various tasks like telling the weather, solving mathematical equations, playing YouTube videos, and reading recent news from Times of India. It can take both voice and text commands.

## Installation

1. Clone this repository or download the ZIP file.
2. Install the required dependencies using pip:
   ```
   pip install -r requirements.txt
   ```
3. Run the `main.py` file to start the virtual assistant:
   ```
   python main.py
   ```

## Usage

Once you have started the virtual assistant, you can interact with it using the GUI or by using voice commands. The GUI provides the following options:

1. Weather - Enter the name of a city to get the current weather information.
2. Calculator - Enter a mathematical expression to solve it.
3. YouTube - Enter a search query to play a YouTube video.
4. News - Get the latest news headlines from Times of India.

You can also use the following voice commands to interact with the virtual assistant:

- "What's the weather in <city>?"
- "Calculate <expression>."
- "Play <query> on YouTube."
- "Read the news."

To use voice commands, click on the "Voice" button in the GUI and speak your command. The assistant will convert your speech to text and execute the corresponding action. 

## Limitations

- The weather information is retrieved from OpenWeatherMap API, which has a limit of 60 calls per minute for the free plan. If you exceed this limit, you may have to wait for some time before making more requests.
- The news headlines are fetched from Times of India RSS feed, which only provides limited information. To read the full news article, you will need to visit the Times of India website.

## Credits

This project was created by Rohan Garg. Feel free to use and modify this code for your own projects. 

If you use any third-party libraries or APIs in your project, make sure to give proper credit to the original authors. 
