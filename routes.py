from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/')
def main():
    color_label_dict = {'red':'exercise',
                        'blue':'work',
                        'yellow':'admin',
                        'green':'finance'}

    colors = list(color_label_dict.keys())
    color_num_dict = {'': 0}
    color_num_dict = {color: idx + 1 for idx, color in enumerate(colors)}

    return render_template('100_blocks.html',
                           colors=colors,
                           color_label_dict=color_label_dict,
                           color_num_dict=color_num_dict)


@app.route('/save/', methods=['POST'])
def save():
    print(vars(request.form))
    return jsonify(vars(request.form))



if __name__ == '__main__':
    app.run(debug=True)
