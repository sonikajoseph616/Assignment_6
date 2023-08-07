import json
Indian_States = {
        "Telangana":"Hyderabad",
        "Andhra Pradesh":"Amaravathi",
        "Tamilnadu":"Chennai",
        "Bihar":"Patna",
        "Delhi":"New Delhi",
        "Maharastra":"Mumbai",
        "Karnataka":"Bangalore"}

##OR##

data= json.dumps(Indian_States)
file = open('indian_States.json','w')
file.write(data)
file.close()
