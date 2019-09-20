import requests
import sys

# fixed constants
baseUrl = "https://techtest.rideways.com/"
suppliers = ["dave", "eric", "jeff"]
cars = {
    'STANDARD' : 4,
    'EXECUTIVE' : 4,
    'LUXURY' : 4,
    'PEOPLE_CARRIER' : 6,
    'LUXURY_PEOPLE_CARRIER' : 6,
    'MINIBUS' : 16,
}

if (len(sys.argv)) < 3:
    print("Error : please enter three values for pickup and dropoff in the pattern; 'pickup-lat,pickup-long' , 'dropoff-lat,dropoff-long' , number-of-passengers")
    sys.exit(0)
else:
    pickup = sys.argv[1]
    dropoff = sys.argv[2]
    passengers = sys.argv[3]

print("-------QUERY INFO-------------")
print("pickup: " + pickup)
print("dropoff: " + dropoff)
print("passengers: " + passengers)
print("------------------------------")

formedUrl = baseUrl + suppliers[0] + "?pickup=" + pickup + "&dropoff=" + dropoff
request = requests.get(formedUrl)
json = request.json()

print("------------------------------")

options = json['options']

sortedOptions = sorted(options, key = lambda i: i['price'], reverse=True)

for option in sortedOptions:
    if (int(cars[option['car_type']]) >= int(passengers)):
        print(option['car_type'] + " - " + str(option['price']))
    else:
        # print("SKIPPED")