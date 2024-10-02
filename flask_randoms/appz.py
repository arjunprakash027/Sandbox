from flask import Flask, request

app = Flask(__name__)

@app.route('/api')
def my_api():
    processed = int(request.args.get('variable')) + 25
    return "thank you for sending me: " + str(request.args.get("another_variable")) + "!"

if __name__ == '__main__':
    app.run(debug = True)