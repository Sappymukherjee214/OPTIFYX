import tkinter as tk
from tkinter import ttk
import requests 
from PIL import Image, ImageTk 
import io

API_KEY = "4bc5be9302ff2767754af50ed3327459"  # Replace with your OpenWeatherMap API key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather_icon(icon_code):
    icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"
    response = requests.get(icon_url)
    img_data = Image.open(io.BytesIO(response.content))
    img = ImageTk.PhotoImage(img_data)
    return img

def get_weather():
    city = city_entry.get()
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        description = data['weather'][0]['description']
        icon_code = data['weather'][0]['icon']
        
        # Update the result window
        result_window = tk.Toplevel(root)
        result_window.title("Weather App")
        result_window.geometry("300x400")
        result_window.configure(bg="white")
        
        # Weather icon
        icon = get_weather_icon(icon_code)
        icon_label = tk.Label(result_window, image=icon, bg="white")
        icon_label.image = icon
        icon_label.pack(pady=20)
        
        # Temperature
        temp_label = tk.Label(result_window, text=f"{temp:.1f}°C", font=("Arial", 36, "bold"), bg="white")
        temp_label.pack()
        
        # Description
        desc_label = tk.Label(result_window, text=description.capitalize(), font=("Arial", 14), bg="white")
        desc_label.pack()
        
        # Location
        location_label = tk.Label(result_window, text=city, font=("Arial", 12), bg="white")
        location_label.pack(pady=10)
        
        # Humidity
        humidity_label = tk.Label(result_window, text=f"Humidity: {humidity}%", font=("Arial", 12), bg="white")
        humidity_label.pack()
    else:
        result_label.config(text="Error: Unable to fetch weather data")

# Create the main window
root = tk.Tk()
root.title("Weather App")
root.geometry("300x150")
root.configure(bg="white")

# Create and pack the title label
title_label = tk.Label(root, text="Weather App", font=("Arial", 16, "bold"), bg="white")
title_label.pack(pady=10)

# Create and pack the input frame
input_frame = tk.Frame(root, bg="white")
input_frame.pack(pady=10)

# City input
city_label = tk.Label(input_frame, text="Enter city name:", bg="white")
city_label.grid(row=0, column=0, padx=5, pady=5)
city_entry = tk.Entry(input_frame)
city_entry.grid(row=0, column=1, padx=5, pady=5)

# Get weather button
get_weather_button = ttk.Button(root, text="Get Weather", command=get_weather)
get_weather_button.pack(pady=10)

# Result label (for error messages)
result_label = tk.Label(root, text="", font=("Arial", 12), bg="white", fg="red")
result_label.pack(pady=10)

# Start the GUI event loop
root.mainloop()