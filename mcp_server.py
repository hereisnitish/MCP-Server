import httpx
from mcp.server import FastMCP

# Initialize the server
mcp = FastMCP("Nitish's Server")

# Define the tool with parameters and proper return format
@mcp.tool(
    name="get_bmi",
    description="Calculate the BMI of a person given their height and weight",
    parameters={
        "height": {"type": "float", "description": "Height of the person in centimeters"},
        "weight": {"type": "float", "description": "Weight of the person in kilograms"}
    }
)
def get_bmi(height: float, weight: float) -> dict:
    """
    Args:
        height (float): Height of the person in centimeters
        weight (float): Weight of the person in kilograms

    Returns:
        dict: BMI of the person in MCP-compatible format
    """
    height_m = height / 100  # Convert cm to meters
    bmi = weight / (height_m ** 2)
    return {
        "content": [{"type": "text", "text": str(bmi)}]
    }

if __name__ == "__main__":
    mcp.run()

# from typing import Any
# import httpx
# from mcp.server.fastmcp import FastMCP

# # Initialize FastMCP server
# mcp = FastMCP("weather")

# # Constants
# NWS_API_BASE = "https://api.weather.gov"
# USER_AGENT = "weather-app/1.0"


# async def make_nws_request(url: str) -> dict[str, Any] | None:
#     """Make a request to the NWS API with proper error handling."""
#     headers = {
#         "User-Agent": USER_AGENT,
#         "Accept": "application/geo+json"
#     }
#     async with httpx.AsyncClient() as client:
#         try:
#             response = await client.get(url, headers=headers, timeout=30.0)
#             response.raise_for_status()
#             return response.json()
#         except Exception:
#             return None

# def format_alert(feature: dict) -> str:
#     """Format an alert feature into a readable string."""
#     props = feature["properties"]
#     return f"""
# Event: {props.get('event', 'Unknown')}
# Area: {props.get('areaDesc', 'Unknown')}
# Severity: {props.get('severity', 'Unknown')}
# Description: {props.get('description', 'No description available')}
# Instructions: {props.get('instruction', 'No specific instructions provided')}
# """


# @mcp.tool()
# async def get_alerts(state: str) -> str:
#     """Get weather alerts for a US state.

#     Args:
#         state: Two-letter US state code (e.g. CA, NY)
#     """
#     url = f"{NWS_API_BASE}/alerts/active/area/{state}"
#     data = await make_nws_request(url)

#     if not data or "features" not in data:
#         return "Unable to fetch alerts or no alerts found."

#     if not data["features"]:
#         return "No active alerts for this state."

#     alerts = [format_alert(feature) for feature in data["features"]]
#     return "\n---\n".join(alerts)

# @mcp.tool()
# async def get_forecast(latitude: float, longitude: float) -> str:
#     """Get weather forecast for a location.

#     Args:
#         latitude: Latitude of the location
#         longitude: Longitude of the location
#     """
#     # First get the forecast grid endpoint
#     points_url = f"{NWS_API_BASE}/points/{latitude},{longitude}"
#     points_data = await make_nws_request(points_url)

#     if not points_data:
#         return "Unable to fetch forecast data for this location."

#     # Get the forecast URL from the points response
#     forecast_url = points_data["properties"]["forecast"]
#     forecast_data = await make_nws_request(forecast_url)

#     if not forecast_data:
#         return "Unable to fetch detailed forecast."

#     # Format the periods into a readable forecast
#     periods = forecast_data["properties"]["periods"]
#     forecasts = []
#     for period in periods[:5]:  # Only show next 5 periods
#         forecast = f"""
# {period['name']}:
# Temperature: {period['temperature']}°{period['temperatureUnit']}
# Wind: {period['windSpeed']} {period['windDirection']}
# Forecast: {period['detailedForecast']}
# """
#         forecasts.append(forecast)

#     return "\n---\n".join(forecasts)


# if __name__ == "__main__":
#     # Initialize and run the server
#     mcp.run(transport='stdio')