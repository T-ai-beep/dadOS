import httpx
import os
from datetime import datetime


async def get_weather(city: str = None) -> dict:
    from config import DEFAULT_CITY
    city = city or DEFAULT_CITY
    api_key = os.getenv("WEATHER_API_KEY", "")

    if not api_key:
        return {"error": True, "message": "No weather API key found. Add WEATHER_API_KEY to your .env file."}

    try:
        url = "https://api.openweathermap.org/data/2.5/weather"
        params = {"q": city, "appid": api_key, "units": "metric"}
        async with httpx.AsyncClient() as client:
            response = await client.get(url, params=params, timeout=5.0)
            data = response.json()

        if data.get("cod") != 200:
            return {"error": True, "message": f"City '{city}' not found"}

        return {
            "error": False,
            "city": data["name"],
            "country": data["sys"]["country"],
            "temperature": round(data["main"]["temp"]),
            "feels_like": round(data["main"]["feels_like"]),
            "condition": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"],
            "wind_speed": round(data["wind"]["speed"]),
            "fetched_at": datetime.now().strftime("%H:%M")
        }
    except Exception as e:
        return {"error": True, "message": f"Could not fetch weather: {str(e)}"}


def format_weather(weather: dict) -> str:
    if weather.get("error"):
        return f"[Weather unavailable: {weather['message']}]"
    return (
        f"[Live weather in {weather['city']}, {weather['country']} "
        f"as of {weather['fetched_at']}: "
        f"{weather['temperature']}°C, feels like {weather['feels_like']}°C, "
        f"{weather['condition']}, humidity {weather['humidity']}%, "
        f"wind {weather['wind_speed']} m/s]"
    )
