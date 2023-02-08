from flask import Flask, request


app= Flask(__name__)

locations = [
    {
        "name": "Florida",
        "devices": [
            {
                "name": "rtr_edge",
                "device_type": "router"
            }
        ]

    }
]

@app.get("/locations")
def get_locations():
    return {"locations": locations}

@app.post("/locations")
def create_locations():
    location = request.get_json()
    new_location=  {"name": location["name"], "devices": []}
    locations.append(new_location)

    return {"locations": locations}, 201

# @app.post("/devices")
# def create_devices():
#     device_location = request.get_json()
#     for location in locations:
#         if location["name"] == device_location["name"]
#             new_device=  {"name": location["name"], "devices": []}
#     locations.append(new_location)

    return {"locations": locations}, 201

if __name__ == "__main__":
    app.run(debug= True)

