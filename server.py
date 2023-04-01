from flask import Flask, render_template, request

app = Flask(__name__)

@app.get("/")
def main():
    return render_template("index.html")


@app.route("/", methods=["GET", "POST"])
def contact_me_info():
    msg_sent = False
    if request.method == "POST":
        if request.form:
            msg_sent = True
    return render_template("index.html", msg_sent=msg_sent)

