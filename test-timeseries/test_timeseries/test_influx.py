import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

token = os.environ.get("INFLUXDB_TOKEN")
org = "F"
url = "http://localhost:8086"

write_client = InfluxDBClient(url=url, token=token, org=org)

bucket = "F"

write_api = write_client.write_api(write_options=SYNCHRONOUS)

for value in range(5):
    point = (
        Point("measurement1")
        .tag("tagname1", "tagvalue1")
        .field("field1", value)
    )
    write_api.write(bucket=bucket, org="F", record=point)
    time.sleep(1)

print("...Execute a Flux Query")
query_api = write_client.query_api()

query = """from(bucket: "F")
|> range(start: -10m)
|> filter(fn: (r) => r._measurement == "measurement1")"""

tables = query_api.query(query, org="F")

for table in tables:
    for record in table.records:
        print(record)

print("...Execute an Aggregate Query")
query_api = write_client.query_api()

query = """from(bucket: "F")
  |> range(start: -10m)
  |> filter(fn: (r) => r._measurement == "measurement1")
  |> mean()"""
tables = query_api.query(query, org="F")

for table in tables:
    for record in table.records:
        print(record)
