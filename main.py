from fastmcp import FastMCP
import random
import json

mcp=FastMCP("Simple Calcualtor Server")

@mcp.tool
def add(a:float,b:float):
    """ Add two nos together"""
    return a+b

@mcp.tool
def roll_dice(n_dice:int=1):
    """ Generate a random no between 1 and 6"""
    return [random.randint(1,6) for _ in range(n_dice)]

@mcp.resource("info://server")
def server_info():
    """ Get information about this server"""
    info={
        "name":"Simple Server",
        "version":"1.0.0",
        "tools":["add","roll_dice"]
    }
    return json.dumps(info,indent=2)


# Start the server
if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)

