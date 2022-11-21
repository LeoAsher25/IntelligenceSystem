import json
import requests
def predict_diabetes(BMI, Age, Glucose):
    url = 'http://192.168.43.85:8000/diabetes/v1/predict'
    data = {"BMI":BMI, "Age":Age, "Glucose":Glucose}
    data_json = json.dumps(data)
    headers = {'Content-type':'application/json'}
    response = requests.post(url, data=data_json, headers=headers)
    result = json.loads(response.text)
    return result
if __name__ == "__main__":
    BMI = input('BMI?')
    Age = input('Age?')
    Glucose = input('Glucose?')
    predictions = predict_diabetes(BMI,Age,Glucose) 
    if predictions["prediction"] == 1:
        print("Diabetic")
    else: 
        print("Not Diabetic")
    print("Confidence: " + predictions["confidence"] + "%")