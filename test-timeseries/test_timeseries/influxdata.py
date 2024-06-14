from datetime import datetime
from influxdb_client import WritePrecision, InfluxDBClient, Point

with InfluxDBClient(url="http://localhost:8086", token="my-token", org="my-org", debug=False) as client:
    # create a point with my data
    p = Point("my-measurement").tag("location", "Prague").field("temperature", 25.3).time(datetime.utcnow(), WritePrecision.MS)

    # get the write api
    write_api = client.write_api()

    # write using point structure
    write_api.write(bucket="my-bucket", record=p)