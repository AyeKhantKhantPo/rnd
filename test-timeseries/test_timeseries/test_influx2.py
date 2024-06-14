from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

bucket = "my-bucket"

client = InfluxDBClient(url="http://localhost:8086", token="q5EmVUx9NxjC9F781xNd_QhxZrstoVI9fRbOsXnDyofLRFlZczk1SqRKzN3X1vNgib4RY4l2DtAJHS3wPasoaQ==", org="OSS")

write_api = client.write_api(write_options=SYNCHRONOUS)
query_api = client.query_api()

p = Point("my_measurement").tag("location", "Prague").field("temperature", 25.3)

write_api.write(bucket=bucket, record=p)

## using Table structure
tables = query_api.query('from(bucket:"my-bucket") |> range(start: -10m)')

for table in tables:
    print("table",table)
    for row in table.records:
        print("Values",row.values)


## using csv library
csv_result = query_api.query_csv('from(bucket:"my-bucket") |> range(start: -10m)')
print("CSV",csv_result)
val_count = 0
for row in csv_result:
    print("ROW",row)
    for cell in row:
        print("CELL",cell)
        val_count += 1
        