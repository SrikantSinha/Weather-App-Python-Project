# Weather App

A modern, user-friendly desktop weather application built with Python and Tkinter that provides real-time weather information for any city worldwide.

## Features

- City Search: Search for weather information in any city globally
- Real-Time Data: Live temperature, feels-like temperature, and weather conditions
- Local Time Display: Automatic timezone detection and local time display
- Comprehensive Metrics: Wind speed, humidity, pressure, and visibility
- Modern UI: Clean, professional interface with custom color scheme
- Global Coverage: Supports cities worldwide using OpenWeatherMap API

## Technologies Used

- Python 3.x - Core programming language
- Tkinter - GUI framework
- OpenWeatherMap API - Weather data provider
- Geopy - Geocoding and location services
- TimezoneFinder - Timezone calculations
- Pytz - Timezone handling

## Prerequisites

Before running this application, ensure you have Python 3.7+ installed on your system.

## Installation

1. Clone the repository
```bash
   git clone https://github.com/yourusername/weather-app.git
   cd weather-app
```

2. Install required dependencies
```bash
   pip install -r requirements.txt
```

3. Set up OpenWeatherMap API
   - Sign up for a free API key at OpenWeatherMap
   - Replace the API key in the code (line 31) with your own key

4. Run the application
```bash
   python weather_app.py
```

## Dependencies

Create a requirements.txt file with the following:
```
geopy
timezonefinder
pytz
requests
```

Install all dependencies using:
```bash
pip install -r requirements.txt
```

## Usage

1. Launch the application
2. Enter a city name in the search box (default: Delhi)
3. Click the search icon or press Enter
4. View real-time weather information including:
   - Current temperature
   - Weather condition
   - Feels-like temperature
   - Local time
   - Wind speed
   - Humidity percentage
   - Atmospheric pressure
   - Visibility range

## Project Structure
```
weather-app/
│
├── weather_app.py          # Main application file
├── requirements.txt        # Project dependencies
└── README.md              # Project documentation
```

## Configuration

### API Key Setup

To use your own OpenWeatherMap API key:

1. Open weather_app.py
2. Locate line 31
3. Replace the existing API key with yours:
```python
   api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=YOUR_API_KEY"
```

### Customization

- Window Size: Modify `root.geometry("900x700+300+100")` (line 11)
- Color Scheme: Update background colors in the configuration section
- Default City: Change `textfield.insert(0,"delhi")` (line 64)

## Features in Detail

### Weather Metrics Displayed

- Temperature: Real-time temperature in Celsius
- Feels Like: Perceived temperature based on humidity and wind
- Wind Speed: Current wind speed in km/h
- Humidity: Air moisture percentage
- Pressure: Atmospheric pressure in hPa
- Visibility: Visibility distance in kilometers

### Timezone Intelligence

The app automatically detects the timezone of the searched city and displays the local time, making it perfect for checking weather in different time zones.

## Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Future Enhancements

- 5-day weather forecast
- Weather alerts and notifications
- Multiple city comparison
- Historical weather data
- Dark/Light theme toggle
- Save favorite cities
- Weather map integration

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

Your Name
- GitHub: @yourusername
- LinkedIn: Your Name

## Acknowledgments

- Weather data provided by OpenWeatherMap
- Geocoding services by Geopy

## Contact

For any questions or suggestions, feel free to reach out:
- Email: your.email@example.com
- LinkedIn: Your Profile

---

Made with Python