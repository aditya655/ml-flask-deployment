from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

cv = pickle.load(open("model/cv.pkl", "rb"))
clf = pickle.load(open("model/clf.pkl", "rb"))


@app.route("/predict", methods=["POST"])
def home():
  email = request.form.get("content")

  tokenized_email = cv.transform([email])

  prediction = clf.predict(tokenized_email)


  return render_template("index.html",prediction=prediction[0], email=email)

if __name__ == "__main__":
  app.run(debug=True)