from flask import Flask, request, render_template
import os
app = Flask(__name__)

g = [{"id": "sanshiro", "name": "三四郎"}, {
    "id": "sorekara", "name": "それから"}, {"id": "mon", "name": "門"}]


@app.route('/')
def index():
    return render_template('index.html', g=g)


@app.route('/novel', methods=['GET'])
def novel():
    name = request.args.get('name')
    filepath = './novel/' + name
    if os.path.exists(filepath) == False:
        return "File not found"
    if os.path.isfile(filepath) == False:
        return "Not a file"
    body = open(filepath, 'r').read()
    return render_template('novel.html', title=name, body=body)


if __name__ == '__main__':
    app.run(debug=True)
