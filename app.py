from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

cv = pickle.load(open("model/cv.pkl", "rb"))
clf = pickle.load(open("model/clf.pkl", "rb"))


@app.route("/", methods=["GET","POST"])
def home():
  text = ""

  if request.method == "POST":
    text = request.form.get("content")
  return render_template("index.html",text=text)

if __name__ == "__main__":
  app.run(debug=True)