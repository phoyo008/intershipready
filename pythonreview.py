# start here

message = "welcome to pythonreview"
print(len(message))
print(message[0])
a = 10
b = 3
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b) # modulo

# review list
professors = ["greg", "pablo", "patricia", "debra"]
print(professors[0])
professors.append("leo")
professors.extend(["santiago", "pepe", "juan"])
print(professors)
professors.insert(2, "jose")
print(professors)
professors[3]="diana"
print(professors)
print(professors[3:5]) # access list position 3 to 4
print(professors[:])
print(professors.remove("pepe"))
print(professors)
x= professors.pop(6)
print(x)
print(professors)
print (len(professors))
print(type(professors))
professors.sort()
print(professors)
professors.reverse()
print(professors)

for i in professors:
    print(i.title())


water_data = {  "temperature":[78,89,92],
                "ph":[6.5,6.7,7.5],
                "oxygen":[7.2, 5.6, 3.5]
                }

print(water_data["ph"])
import pandas as pd

df = pd.DataFrame(water_data)
print(df)