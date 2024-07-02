import requests
import random
import json
import string
import pytest

#base_url
base_url = "https://gorest.co.in"

#auth_token
auth_token = "Bearer b6281b0333abbe2009e9140362d65f0b69741b292eb502faf0f9d9689e3c3703"

#GETUser
@pytest.mark.regression
def test_get_user():
    url = base_url + "/public/v2/users";
    print("The users url is: " + url)
    headers = {"Authorization": auth_token}
    GetResponse = requests.get(url, headers = headers)
    assert GetResponse.status_code == 200
    response = GetResponse.json();
    pretty_response = json.dumps(response,indent=4)
    print("Json response from GET_USER is: " + pretty_response)


def generate_random_email():
    domains = ["gmail.com", "yahoo.com", "hotmail.com", "example.com"]
    letters = string.ascii_lowercase

    username = ''.join(random.choice(letters) for i in range(8))  # Generates a random username of length 8
    domain = random.choice(domains)

    return f"{username}@{domain}"

@pytest.fixture
def test_post_user():
    url = base_url + "/public/v2/users";
    print("The post users url is: " + url)
    random_email = generate_random_email()
    user_data = {
        "id": 6990278,
        "name": "Devadatt Bhattathiri",
        "email": random_email,
        "gender": "female",
        "status": "active"
    }
    headers = {"Authorization": auth_token}
    postResponse = requests.post(url, headers=headers, data=user_data)
    print(postResponse.status_code)
    assert postResponse.status_code == 201
    responseJson = postResponse.json()
    created_user_id = responseJson['id']
    pretty_response = json.dumps(postResponse.json())
   # print("The created id is: " + created_user_id)
    print("Json response from POST_USER is: " + pretty_response)
    return created_user_id

@pytest.mark.regression
def test_put_user():

    url = base_url + "/public/v2/users";
    print("The PUT users url is: " + url)
    random_email = generate_random_email()
    user_data = {
    "email": random_email,
    "name": "Shantanu RC",
    "gender": "male",
    "status": "active",
    "id": 6940167
    }
    headers = {"Authorization": auth_token}
    putResponse = requests.post(url, headers=headers, data=user_data)
    print(putResponse.status_code)
    assert putResponse.status_code == 201
    pretty_response = json.dumps(putResponse.json())
    print("Json response from PUT_USER is: " + pretty_response)


#DeleteUser
#@pytest.mark.parametrize("user_id")
@pytest.mark.sanity
def test_delete_user(test_post_user):
    url = base_url + f"/public/v2/users/{test_post_user}"
    print("The users url is: " + url)
    headers = {"Authorization": auth_token}
    deleteResponse = requests.delete(url, headers = headers)
    assert deleteResponse.status_code == 204
    print("DELETE DONE")


