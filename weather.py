import requests

def get_weather(city):
    api_key = "YOUR_API_KEY" 
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    
    complete_url = base_url + "appid=" + api_key + "&q=" + city
    
    response = requests.get(complete_url)
    
    data = response.json()
    
    if data["cod"] != "404":
        main = data["main"]
        weather = data["weather"][0]
        
        temperature = main["temp"]
        pressure = main["pressure"]
        humidity = main["humidity"]
        description = weather["description"]
        
        temperature_celsius = temperature - 273.15
        
        print(f"City: {city}")
        print(f"Temperature: {temperature_celsius:.2f}°C")
        print(f"Pressure: {pressure} hPa")
        print(f"Humidity: {humidity}%")
        print(f"Description: {description}")
    else:
        print("City not found.")

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)
