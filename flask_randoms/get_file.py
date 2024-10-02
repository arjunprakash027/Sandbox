from flask import Flask,request

app = Flask(__name__)

@app.route('/get_file',methods=['POST'])
def get_file():
    files = request.files['file']
    data = request.form['name']
    print(data)
    print(files.read())
    return "File received"


if __name__ == '__main__':
    app.run(debug=True)
