import os
import random

import cherrypy

"""
This is a simple Battlesnake server written in Python.
For instructions see https://github.com/BattlesnakeOfficial/starter-snake-python/README.md
"""

import logging
logging.basicConfig(filename='debug.log', level=logging.DEBUG)

moveIndex = 0

class Battlesnake(object):
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def index(self):
        # This function is called when you register your Battlesnake on play.battlesnake.com
        # It controls your Battlesnake appearance and author permissions.
        # TIP: If you open your Battlesnake URL in browser you should see this data
        return {
            "apiversion": "1",
            "author": "plesieur",  # TODO: Your Battlesnake Username
            "color": "#008B8B",  # TODO: Personalize
            "head": "safe",  # TODO: Personalize
            "tail": "hook",  # TODO: Personalize
        }

    @cherrypy.expose
    @cherrypy.tools.json_in()
    def start(self):
        # This function is called everytime your snake is entered into a game.
        # cherrypy.request.json contains information about the game that's about to be played.
        data = cherrypy.request.json

        print("START")
        return "ok"




    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def move(self):
        # This function is called on every turn of a game. It's how your snake decides where to move.
        # Valid moves are "up", "down", "left", or "right".
        # TODO: Use the information in cherrypy.request.json to decide your next move.
        global moveIndex 
        possible_moves = ["up", "right", "down", "left"]





        data = cherrypy.request.json
        
        board = data["board"]
        boardRows = board["height"]
        boardCols = board["width"]

        you = data["you"]

        x = you["body"][0]["x"]
        y = you["body"][0]["y"]

        rv = "false";
        if moveIndex == 0:
          if y+1 >= boardRows:
            rv = "true"
        elif moveIndex == 1:
          if x+1 >= boardCols:
            rv = "true"
        elif moveIndex == 2:
          if y-1 < 0:
            rv = "true"
        else:
          if x-1 < 0:    
            rv = "true"
        
        if (rv == "true"):
          moveIndex += 1
          if (moveIndex >3):
            moveIndex = 0

        logging.debug("moveIndex:"+str(moveIndex))
        move = possible_moves[moveIndex]
        print(f"MOVE: {move}")
        return {"move": move}


    @cherrypy.expose
    @cherrypy.tools.json_in()
    def end(self):
        # This function is called when a game your snake was in ends.
        # It's purely for informational purposes, you don't have to make any decisions here.
        data = cherrypy.request.json

        print("END")
        return "ok"


if __name__ == "__main__":
    server = Battlesnake()
    cherrypy.config.update({"server.socket_host": "0.0.0.0"})
    cherrypy.config.update(
        {"server.socket_port": int(os.environ.get("PORT", "8080")),}
    )
    print("Starting Battlesnake Server...")
    cherrypy.quickstart(server)
