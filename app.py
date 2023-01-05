from flask import Flask, request
import docker

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)

# simple index route for testing operation
@app.route("/")
def hello_world():
    return "Roboflow proxy server running!"

# get list of running containers
@app.route("/status")
def status():
    client = docker.from_env()
    running_containers = client.containers.list()
    try:
        print(running_containers)
        return str(running_containers) if running_containers else "No Containers Running\n"
    except:
        print("Issue getting container status")
        return "Issue getting container status"


# start a container with data
@app.route("/start_container/<project>/<version>/<api_key>", methods=["POST"])
def start(project, version, api_key):
    client = docker.from_env()

    # from body, get image name and ENV details
    try:
        docker_image = request.json["DOCKER_IMAGE"]
        FPS_CAP = request.json["FPS_CAP"] if "FPS_CAP" in request.json else ""
    except:
        print("failed to get json data from body")

    try:
        result = client.containers.run(
            "roboflow/inference-server:jetson-trt-udp",
            detach=True,
            privileged=True,
            devices=["/dev/video0:/dev/video0"],
            network="host",
            device_requests=[
                docker.types.DeviceRequest(device_ids=["all"], capabilities=[["gpu"]])
            ],
            environment=[f"FPS_CAP={FPS_CAP}",f"dataset={project}",f"version={version}",f"api_key={api_key}"],
            mounts=[docker.types.Mount("/cache","roboflow")],
            )
        return str(result)
    except:
        print("Issue starting container")
        return "Issue starting container"


@app.route("/kill_container")
def kill():
    # find all running roboflow containers
    client = docker.from_env()
    running_containers = client.containers.list()
    try:
        for container in running_containers:
            print(type(str(container)))
            if "roboflow" in str(container.image):
                print(f"Found a Roboflow container image: {container.image}")
                container.kill()
                return "container killed"
    except:
        print("Issue killing container")
        return "Issue killing container"

    return "no Roboflow containers found"


# main driver function
if __name__ == "__main__":

    # run() method of Flask class runs the application
    # on the local development server.
    app.run()
