from flask import Flask, render_template, request, jsonify
from utils import model_predict

app = Flask(__name__)



@app.route("/")
def home():
  return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
  email = request.form.get("content")

  prediction = model_predict(email)

  return render_template("index.html",prediction=prediction, email=email)

@app.route("/api/predict", methods=["POST"])
def predict_api():
  data = request.get_json()

  if not data or "content" not in data:
    return jsonify({
      "error": "content is required"
    }), 400

  email = data["content"]

  if not isinstance(email,str):
    return jsonify({
      "error": "content must be a string"
    }),400

  if not email.strip():
    return jsonify({
      "error": "content can't be empty"
    }), 400

  prediction =  model_predict(email)

  return jsonify({
    "prediction": prediction,
    "email": email
  })

@app.route("/health", methods=["GET"])
def health():
  return jsonify({
    "status": "ok"
  }),200

if __name__ == "__main__":
  app.run(debug=True)