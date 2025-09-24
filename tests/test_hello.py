from hello.hello import get_message

def test_message():
    assert get_message() == "Hello World from Python!"
