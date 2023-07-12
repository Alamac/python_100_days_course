import requests
from datetime import datetime

USERNAME = "USERNAME"
TOKEN = "TOKEN"


pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/test"
put_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/test/20230712"
delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/test/20230712"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# graph_params = {
#     "id": "test",
#     "name": "Test Graph",
#     "unit": "hours",
#     "type": "float",
#     "color": "ajisai"
# }

headers = {
    "X-USER-TOKEN": TOKEN
}


# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)

# print(response.text)

# pixel_params = {
#     "date": datetime.now().strftime("%Y%m%d"),
#     "quantity": "2"
# }

# response = requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)
# print(response.text)

# put_pixel_params = {
#     "quantity": "5"
# }

# response = requests.put(url=put_pixel_endpoint, json=put_pixel_params, headers=headers)
# print(response.text)

response = requests.delete(url=delete_pixel_endpoint, headers=headers)
print(response.text)