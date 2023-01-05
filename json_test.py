import requests
res = requests.post('http://127.0.0.1:5000/start_container/1/1/1', json={"FPS_CAP":"30", "DOCKER_IMAGE":"roboflow/inference-server:jetson-trt-udp"})

if res.ok:
    print(res.json())
