import requests

# Define the endpoint URL and the sentence to be sent
endpoint = 'http://127.0.0.1:5000/api'
sentence = 2

# Encode the sentence as a URL parameter
url_param = {'variable': sentence,
             'another_variable': 25}

# Send the request to the API endpoint with the URL parameter
response = requests.get(endpoint, params=url_param)

# Print the response from the API
print(response.text)