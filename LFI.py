from flask import Flask, request, render_template


app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/")
def start():
    return render_template("index.html")


@app.route("/home", methods=['POST'])
def home():
    filename = request.form['filename']
    if filename == "":
        filename = "default"
    f = open("text/"+filename+".txt",'r')
    read = f.read()
    return render_template("index.html",read = read)
    
    return render_template("index.html",read="Invalid user input!!!")
    i


if __name__ == "__main__":
    app.run(host='0.0.0.0')

