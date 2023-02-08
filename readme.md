stores == locations
 post /location {name: ""}
 get /location
 get /location/location_name
 get /location/location_name/device
 post /location/location_name/device {name: "", device_type: ""}
items == devices

allow clients to create locations
create devices with in a location
retreive list of all locations and there devices
retreive a location and its devices
retreive list of devices in a location