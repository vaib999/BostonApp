import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'crim': 0.02, 
                            'zn': 18.0,
                            'indus': 2.18,
                            'chas': 10.0,
                            'tox': 0.458,
                            'rm': 6.98,
                            'age': 45.2,
                            'dis': 6.34,
                            'rad': 3.0,
                            'tax': 222.0,
                            'ptratio': 18.5,
                            'b': 396.90,
                            'lstat': 2.94,
                            })

print(r.json())
