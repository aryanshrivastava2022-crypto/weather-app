import requests

API_KEY = "YOUR_API_KEY"

city = input("Enter city name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    city_name = data["name"]
    temperature = data["main"]["temp"]
    weather = data["weather"][0]["description"]

    print("\n🌦️ Weather Information")
    print(f"City: {city_name}")
    print(f"Temperature: {temperature}°C")
    print(f"Condition: {weather}")

else:
    print("❌ City not found or API error.")
