import requests
import tkinter as tk

def get_weather(city):
    """Fetches weather data for a given city using the OpenWeatherMap API."""
    api_key = "4bc5be9302ff2767754af50ed3327459"  # Replace with your OpenWeatherMap API key
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"  # Use metric units for temperature

    response = requests.get(url)
    data = response.json()

    if data["cod"] != 200:
        return None

    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    weather_description = data["weather"][0]["description"]
    city_name = data["name"]
    country = data["sys"]["country"]

    return temperature, humidity, weather_description, city_name, country

def display_weather(temperature, humidity, weather_description, city_name, country):
    """Displays the weather data in the GUI."""
    temperature_label.config(text=f"{temperature}°C")
    humidity_label.config(text=f"{humidity}%")
    weather_description_label.config(text=weather_description)
    location_label.config(text=f"{city_name}, {country}")

def fetch_weather():
    """Fetches weather data and displays it in the GUI."""
    city = city_entry.get()
    weather_data = get_weather(city)

    if weather_data:
        display_weather(*weather_data)
    else:
        error_label.config(text="Error: Could not fetch weather data.")

# Create the main window
root = tk.Tk()
root.title("Weather App")
root.geometry("300x200")

# Create labels and entry fields
city_label = tk.Label(root, text="Enter city name:")
city_label.grid(row=0, column=0, padx=5, pady=5)
city_entry = tk.Entry(root)
city_entry.grid(row=0, column=1, padx=5, pady=5)

fetch_button = tk.Button(root, text="Get Weather", command=fetch_weather)
fetch_button.grid(row=1, columnspan=2, padx=5, pady=5)

temperature_label = tk.Label(root, text="")
temperature_label.grid(row=2, column=0, padx=5, pady=5)
humidity_label = tk.Label(root, text="")
humidity_label.grid(row=3, column=0, padx=5, pady=5)
weather_description_label = tk.Label(root, text="")
weather_description_label.grid(row=4, column=0, padx=5, pady=5)
location_label = tk.Label(root, text="")
location_label.grid(row=5, column=0, padx=5, pady=5)

error_label = tk.Label(root, text="", fg="red")
error_label.grid(row=6, columnspan=2, padx=5, pady=5)

# Start the GUI
root.mainloop()