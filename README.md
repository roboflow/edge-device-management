# edge_device_management

Interact with Roboflow containers via Flask server routes.

## Installation

Install required packages with `pip3 install -r requirements.txt`.

## Testing performance

Starting up the server with `python3 app.py` turns the Flask server on using port `5000`.

Perform simple POST requests with JSON data in the body via `python3 json_text.py`.
- update the docker image in the JSON body to try different images
- set an FPS_CAP to try different speeds on the Roboflow UDP image

Check if UDP stream works via `python3 client_test.py`
