import json
import datetime
import csv
csv_file=open("data.csv", "r")
reader = csv.reader(csv_file)

for row in reader:
    print(row[0])

def handler(event, context):
    data = {
        'output': 'Hello World',
        'timestamp': datetime.datetime.utcnow().isoformat()
    }
    return {'statusCode': 200,
            'body': json.dumps(data),
            'headers': {'Content-Type': 'application/json'}}

