import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "MJfSeYXM4FlckOL4ppBVosB3B3s3jLYq"

while True:
   orig = input("Ubicación de inicio: ")
   if orig == "quit" or orig == "q":
       break  
   dest = input("Destino: ")
   if dest == "quit" or dest == "q":
       break  

   url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
   print("URL: " + (url))
   json_data = requests.get(url).json()
   json_status = json_data["info"]["statuscode"]
   if json_status == 0:
    print("Estado de la API: " + str(json_status) + " = Una llamada de ruta exitosa.\n")
    print("=============================================")
    print("Direcciones desde " + orig + " hasta " + dest)
    print("Duración del viaje:   " + json_data["route"]["formattedTime"])
    print("Kilómetros:      " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))

    if "fuelUsed" in json_data["route"]:
        print("Combustible utilizado (Ltr): " + str("{:.2f}".format((json_data["route"]["fuelUsed"])*3.78)))
    else:
        print("Combustible utilizado (Ltr): Información no disponible")
    print("=============================================")
    for each in json_data["route"]["legs"][0]["maneuvers"]:
        print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
    print("=============================================\n")
