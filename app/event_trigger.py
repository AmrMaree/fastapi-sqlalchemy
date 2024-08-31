import requests,json


post = {
  "title": "string",
  "content": "string",
  "userid": 1
}
response = requests.post('http://localhost:8000/users/login/', 
                         data={"username":"amr@gmail.com","password":"123"},
                         headers={'Content-Type': 'application/x-www-form-urlencoded'})

if response.status_code == 200:
    token = json.loads(response.text).get("token")
    print(token)
    if not token:
        print("Failed to retrieve token.")
        exit()


requests.post("http://localhost:8000/posts",json=post,
              headers={
                  'Authorization': f'Bearer {token}',
                  'Content-Type': 'application/json'
              })
