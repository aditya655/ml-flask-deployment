import pickle 


cv = pickle.load(open("model/cv.pkl", "rb"))
clf = pickle.load(open("model/clf.pkl", "rb"))

def model_predict(email):

  if not email:
    return None

  
  

  tokenized_email = cv.transform([email])

  prediction = clf.predict(tokenized_email)

  return 1 if prediction[0] == 1 else -1
