import random
from string import ascii_lowercase

from flask import Flask, render_template, request, jsonify, redirect, url_for

from config import config
from models import session, get_color_num_dict, base_board, colors, color_num_dict, get_board, get_boards, \
    create_board

app = Flask(__name__)

num_squares = config['num_squares']



@app.route('/<board_name>')
def main_board(board_name=None):
    return render_template('100_blocks.html',
                           all_boards=get_boards(),
                           board=get_board(name=board_name) or base_board)

@app.route('/')
def main():
    return render_template('100_blocks.html',
                           all_boards=get_boards(),
                           board=base_board)


@app.route('/save', methods=['POST'])
def save():
    layout, board_name = request.get_json().values()
    board = get_board(name=board_name)
    if board is not None:
        board.update(layout)
    else:
        board = create_board(layout, board_name, colors)
    return jsonify(board.layout)



if __name__ == '__main__':
    app.run(debug=True)
