from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    html="""<link rel="stylesheet" href="static/css/main.css" type="text/css">
    <p class="bg-gray-200">Hello World</p> """
    return html

if __name__=="__main__":
    app.run(debug=True)