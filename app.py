#! usr/bin/python3.11

from flask import Flask, render_template, request, url_for, jsonify
from maze import Maze

app = Flask(__name__)

maze = Maze()
character_position = maze.start

@app.route("/")
def index():
    start = {'x': maze.start[0], 'y': maze.start[1]}
    # print(start, maze.start)
    # print(maze.end)
    return render_template("index.html", start=start)

@app.route("/validate_step", methods=['POST'])
def validate_step():
    global character_position
    data = request.get_json()
    new_x = int(data['arg_x'])
    new_y = int(data['arg_y'])

    new_x += character_position[0]
    new_y += character_position[1]
    new_step = (int(new_x), int(new_y))
    if maze.grid[new_step]:
        character_position = (new_x, new_y)
        response = {
            'success' : True,
        }
        if character_position == maze.end:
            response = {
                'success' : True,
                'final' : True,
            }
    else:
        response = {
            'success' : False,
        }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)