# Create flask app that returns "Hello World"
import threading
import time
import os
from flask import Flask
app = Flask(__name__)

TIME_TO_SLEEP = 30

@app.route("/")
def hello():
    return "Hello World"

def sleeper():
    print(f"Sleeping for {TIME_TO_SLEEP} seconds")
    time.sleep(TIME_TO_SLEEP)
    print("Exiting")
    os._exit(1)

if __name__ == "__main__":
    threading.Thread(target=sleeper, daemon=True).start()
    app.run(host="0.0.0.0", port=5000)
