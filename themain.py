from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    email = request.form.get("email")
    password = request.form.get("password")

    print("Email:", email)
    print("Password:", password)

    return f"Welcome {email}"

if __name__ == "__main__":
    app.run(debug=True)