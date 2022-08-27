import phonenumbers
import opencage
import folium
from myphone import number
from phonenumbers import geocoder, PhoneNumber

pepnumber = phonenumbers.parse(number, "CH")
location = geocoder.description_for_number(pepnumber, "en")
print(location)

from phonenumbers import carrier

service_prov = phonenumbers.parse(number, "CH")
print(carrier.name_for_number(service_prov, "en"))



from opencage.geocoder import OpenCageGeocode

# you need to generate your own new key from opencage.com its needed and replace this one.
key = 'cd9670008ec74a658a5889802494bd03'
geocoder=OpenCageGeocode(key)
query=str(location)
results=geocoder.geocode(query)



lat =results[0]['geometry']['lat']
lng =results[0]['geometry']['lng']

print(lng,lat)

myMap= folium.Map(location=[lat,lng],zoom_start=9)
folium.Marker([lat,lng],popup=location).add_to(myMap)

myMap.save("myloocation.html")