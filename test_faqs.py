import requests

def test_faqs_api():
    # URL of your API endpoint
    url = "http://16.171.132.17:8000/api/faqs/"

    # Send GET request to the API
    response = requests.get(url)

    # Assert that the response status code is 200 (OK)
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

    # Check if the response contains the 'faqs' key and it's a list
    data = response.json()
    assert 'faqs' in data, "Response does not contain 'faqs' key"
    assert isinstance(data['faqs'], list), "'faqs' is not a list"

    # Further checks on the FAQ content
    faqs = data['faqs']
    assert len(faqs) > 0, "'faqs' list is empty"

    # Check if each FAQ has the expected keys
    for faq in faqs:
        assert 'question_en' in faq, "FAQ is missing 'question_en'"
        assert 'answer_en' in faq, "FAQ is missing 'answer_en'"
        assert 'question_hi' in faq, "FAQ is missing 'question_hi'"
        assert 'answer_hi' in faq, "FAQ is missing 'answer_hi'"

    # Optional: You can check if the content matches the expected values (example for the first FAQ)
    assert faqs[0]['question_en'] == "What is Django?", "First FAQ question does not match"
    assert faqs[0]['answer_en'] == "Django is a Python-based web framework.", "First FAQ answer does not match"
