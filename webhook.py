import requests 

user_message = "Can you tell me conversion rate from USD TO INR in current time use the tool for web search" 

request_message = {"message": user_message}

url = "http://localhost:5678/webhook-test/06ed1dfa-071f-472f-9e7a-89bf7bdc2959" 


 

response = requests.post(url, json=request_message)

print(response.status_code)

print(response.json()[0]["output"])



