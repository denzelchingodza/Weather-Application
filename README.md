How Everything Interacts (System Flow Diagram)
- User → GUI → API layer → External API → GUI → Display → Assets

Step-by-step:
- user enters city name in WeatherWindow
- WeatherWindow calls weather_api.get_weather(city)
- weather_api loads API key from config.json
- weather_api sends HTTPS request using requests
- OpenWeatherMap responds with JSON
- weather_api validates/corrects data
= weather_api returns dict {temp, description, icon}
- GUI updates label text
- GUI loads icon from assets/icons/iconcode.png
- GUI renders everything on screen
- Testing bypasses the GUI entirely:
- test_api.py → calls weather_api directly
- test_util.py → calls conversion helpers directly

This Weather Application allows users to check real-time weather information for any city in the world. The app provides a simple, intuitive interface and displays key weather data clearly.

#Core Features
1. City Search: Enter the name of any city to get current weather information.
2. Weather Details: Displays temperature, humidity, wind speed, and a brief weather description (e.g., sunny, rainy).
3. Dynamic Weather Icons: Visual icons change depending on the current weather condition.
4. Responsive Design: Works on both desktop and mobile devices.
5. Error Handling: Displays a user-friendly message if a city is not found or if the API fails.

How It Works
- User Input: The user types the name of a city into the search bar.
- API Request: The app sends a request to the OpenWeatherMap API (or the chosen weather API) using the provided city name.
- Receive Data: The API returns weather information in JSON format.
- Data Display: The app extracts relevant data (temperature, humidity, wind speed, and description) and updates the UI dynamically.
- Icons & Styling: Based on the weather condition, an appropriate icon or background is displayed to match the current weather (still yet to work and modify this on the GUI)
- Error Handling: If the city is invalid or not found, the app shows an error message without breaking the UI.

This simple workflow ensures users can quickly and reliably get accurate weather updates anywhere in the world.

