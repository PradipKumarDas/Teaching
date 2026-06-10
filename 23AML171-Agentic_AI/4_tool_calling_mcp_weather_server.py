# MCP SERVER FOR EVALUATION OF ARITHMETIC EXPRESSIONS

from mcp.server.fastmcp import FastMCP      # Provides interfaces to build a light-weight MCP server in Python

# Initializes an MCP server that provides a tool to get weather information for a given location.
WEATHER_MCP = FastMCP(
    name="weather-mcp-server",
    host="0.0.0.0",
    port=8002,
    streamable_http_path="/mcp",
)


@WEATHER_MCP.tool()
def weather(location: str) -> str:
    """
    Returns weather information for a location.
    It is a dummy implementation that always returns the same temperature for any location.
    Production implementations would typically call an external weather API to get real data.
    
    Parameters:
    location (str): The location for which to get the weather information.
    
    Returns:
    str: A string containing the weather information for the specified location.
    """

    temperature = "28°"
    return f"The current temperature in {location} is {temperature}C."

if __name__ == "__main__":
    WEATHER_MCP.run(transport="streamable-http")