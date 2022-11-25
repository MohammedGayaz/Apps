import requests


def get_question():
    parameters = {
        "amount" : 50,
        "type" : "boolean",
    }
    responce = requests.get("https://opentdb.com/api.php", params=parameters)
    data = responce.json()
    question_data = data["results"]   
    return question_data

