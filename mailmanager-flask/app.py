from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        print(request.form.getlist("move_msg"))
        # print(request.form("optA2"))

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)