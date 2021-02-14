places = ["India", "Eiffel Tower", "New York", "Pyrimds of Giza", "libaries", "snow parks"]

print(places)
print(places[0])
i=0
while i < len(places):
    print(places[i].upper())# print item in uppercase
    i+=1
for place in places:
    print(place.upper())# print item in uppercase
i=len(places)
while i > 0:
    print(places[i-1].upper())# print item in uppercase
    i-=1
for i in range(len(places)-1,-1,-1):
    print(places[i].upper())
print(len(places))# how many itens