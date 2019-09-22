import requests
import sys
from operator import itemgetter

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
useDave = True
useEric = True
useJeff = True
combinedOptions = []

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

formedUrlDave = baseUrl + suppliers[0] + "?pickup=" + pickup + "&dropoff=" + dropoff
try:
    requestDave = requests.get(formedUrlDave, timeout=2)
    jsonDave = requestDave.json()
except (requests.exceptions.ConnectTimeout,requests.exceptions.ReadTimeout) as e:
    print("Skipping supplier Dave - ")
    print(e)
    useDave = False


formedUrlEric = baseUrl + suppliers[1] + "?pickup=" + pickup + "&dropoff=" + dropoff
try:
    requestEric = requests.get(formedUrlEric, timeout=2)
    jsonEric = requestEric.json()
except (requests.exceptions.ConnectTimeout,requests.exceptions.ReadTimeout) as e:
    print("Skipping supplier Eric - ")
    print(e)
    useEric = False

formedUrlJeff = baseUrl + suppliers[2] + "?pickup=" + pickup + "&dropoff=" + dropoff
try:
    requestJeff = requests.get(formedUrlJeff, timeout=2)
    jsonJeff = requestJeff.json()
except (requests.exceptions.ConnectTimeout,requests.exceptions.ReadTimeout) as e:
    print("Skipping supplier Jeff - ")
    print(e)
    useJeff = False

if useDave:
    if "error" in jsonDave:
        print("Error : Dave supplier api error : " + jsonDave['error'])
        useDave = False
    else:
        optionsDave = jsonDave['options']
        for option in optionsDave:
            option['supplier'] = "Dave"
        combinedOptions = combinedOptions + optionsDave

if useEric:
    if "error" in jsonEric:
        print("Error : Eric supplier api error : " + jsonEric['error'])
        useEric = False
    else:
        optionsEric = jsonEric['options']
        for option in optionsEric:
            option['supplier'] = "Eric"
        combinedOptions = combinedOptions + optionsEric

if useJeff:
    if "error" in jsonJeff:
        print("Error : Jeff supplier api error : " + jsonJeff['error'])
        useJeff = False
    else:
        optionsJeff = jsonJeff['options']
        for option in optionsJeff:
            option['supplier'] = "Jeff"
        combinedOptions = combinedOptions + optionsJeff

print("------------------------------")

pruned = {pruned['car_type']:pruned for pruned in combinedOptions}.values()

prunedSort = sorted(pruned, reverse=True, key=itemgetter("price"))

for option in prunedSort:
    if (int(cars[option['car_type']]) >= int(passengers)):
        print(option['car_type'] + " - " + str(option['supplier']) + " - " + str(option['price']))