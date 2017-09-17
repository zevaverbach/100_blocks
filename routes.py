import random
from string import ascii_lowercase

from flask import Flask, render_template, request, jsonify

from models import Board, session

app = Flask(__name__)


@app.route('/')
def main():
    color_label_dict = {'red':'exercise',
                        'blue':'work',
                        'yellow':'admin',
                        'green':'finance',
                        '#2C2416':'',
                        'black':'',
                        '#F98D8D':'',
                        'orange':'',
                        'white': '',
                        '#1a1b29': '',
                        '#000080': '',
                        '#333333':'',
                        '#CF5300': '',
                        '#8B0000': '',
                       }

    colors = list(color_label_dict.keys())
    color_num_dict = {'': 0}
    color_num_dict = {color: str(idx + 1).zfill(2) for idx, color in enumerate(colors)}

    return render_template('100_blocks.html',
                           colors=colors,
                           color_label_dict=color_label_dict,
                           color_num_dict=color_num_dict)


@app.route('/save', methods=['POST'])
def save():
    name = ''
    for i in range(12):
        name += random.choice(ascii_lowercase)
    layout = list(request.get_json().values())[0]
    session.add(Board(layout=layout, name=name))
    session.commit()
    return jsonify(session.query(Board).first().layout)



if __name__ == '__main__':
    app.run(debug=True)
