import random
from string import ascii_lowercase

from flask import Flask, render_template, request, jsonify, redirect, url_for

from config import config
from models import session, get_color_num_dict, base_board, colors, color_num_dict, get_board, get_boards, \
    create_board, update_base_table

app = Flask(__name__)

num_squares = config['num_squares']


# TODO: export an animtated gif of the progress of a piece
# TODO: fix loading/saving
# TODO: add undo/redo
# TODO: add Eno-like soothing tones when you tap a box
# TODO: make selected color slightly larger
# TODO: dislpay filename
# TODO: allow renaming
# TODO: allow live view of progress via web/app

# not related to the app
# TODO: make simon.averba.ch and put his art up there because he wants to "send it to everybody in the world"
# TODO: make sylvia.averba.ch and put his art up there because he wants to "send it to everybody in the world"
# TODO: make abi.averba.ch and put his art up there because he wants to "send it to everybody in the world"
# TODO: use IFPS for the above



@app.route('/<board_name>')
def main_board(board_name=None):
    return render_template('100_blocks.html',
                           all_boards=get_boards(),
                           board=get_board(name=board_name) or base_board)

@app.route('/')
def main():
    update_base_table()
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
