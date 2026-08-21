from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def home():
  text = ""

  if request.method == "POST":
    text = request.form.get("content")
  return render_template("index.html",text=text)

if __name__ == "__main__":
  app.run(debug=True)