import json
file = open('employee.json','r') #change the file path while running the code
data = file.read()
file.close()
user1 = json.loads(data) 
print(user1)
