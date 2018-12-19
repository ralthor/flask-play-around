import requests

obj={"c1":[[1,1,1,1]]}
response=requests.post("http://127.0.0.1:5000/predict", json=obj)
print(response.json())