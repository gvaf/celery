import requests
import json

a = requests.get("http://0.0.0.0:5555/api/workers")
print(a.status_code)
print(json.dumps(a.json(), indent=4))


print("======================================")

a = requests.get("http://0.0.0.0:5555/api/tasks")
print(a.status_code)
print(json.dumps(a.json(), indent=4))


print("======================================")

a = requests.post("http://0.0.0.0:5555/api/task/send-task/myapp.tasks.process_resize", data="""{"args": ["flower.png"] }""")
doc = a.content
resp = json.loads(doc)
task_id = resp['task-id']
print(doc)

print("======================================")

a = requests.get(f"http://0.0.0.0:5555/api/task/result/{task_id}")
print(a.status_code)
print(a.content)

