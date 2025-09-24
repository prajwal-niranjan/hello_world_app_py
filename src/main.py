from flask import Flask
import os
from hello.hello import get_message

app = Flask(__name__)

@app.route("/")
def hello():
    return get_message()

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
