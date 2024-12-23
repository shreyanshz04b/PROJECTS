import requests
import json
import sys
import re
import webbrowser

red = "\033[31m"
yellow = "\033[93m"
lgreen = "\033[92m"
clear = "\033[0m"
bold = "\033[01m"
cyan = "\033[96m"

print(red + """
 ██████╗ ██████╗  ██████╗ ███████╗██████╗ ███████╗
██╔════╝██╔═══██╗██╔═══██╗██╔════╝██╔══██╗██╔════╝
██║     ██║   ██║██║   ██║█████╗  ██████╔╝█████╗  
██║     ██║   ██║██║   ██║██╔══╝  ██╔══██╗██╔══╝  
╚██████╗╚██████╔╝╚██████╔╝███████╗██║  ██║███████╗
 ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝╚══════╝
                                                 v 2.4
""" + red)
print(lgreen + bold + "         <===[[ coded by @shreyanshhacker ]]===> \n" + clear)
print(yellow + bold + "   <---(( Welcome to OrgTrack ))--> \n" + clear)

def validate_ip(ip):
    ip_pattern = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
    return re.match(ip_pattern, ip)

ip = input(lgreen + bold + "[*] Enter Target IP Address: " + clear).strip()

if not validate_ip(ip):
    print(red + "[~] Invalid IP address. Please enter a valid IPv4 address!" + clear)
    sys.exit(1)

api = "http://ip-api.com/json/"

latitude, longitude = None, None

# please your Google Maps API Key here due to privacy i remove my api 
google_maps_api_key = "YOUR_GOOGLE_MAPS_API_KEY"
places_api_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"

try:
    response = requests.get(api + ip)
    data = response.json()

    if data["status"] != "success":
        print(red + "[~] Unable to fetch details. Check the IP address or try again later." + clear)
        sys.exit(1)

    sys.stdout.flush()
    a = lgreen + bold + "[$]"
    b = cyan + bold + "[$]"
    print(a, "[Victim]:", data.get("query", "N/A"))
    print(red + "<--------------->" + red)
    print(b, "[Country]:", data.get("country", "N/A"))
    print(red + "<--------------->" + red)
    print(a, "[Region]:", data.get("regionName", "N/A"))
    print(red + "<--------------->" + red)
    print(b, "[City]:", data.get("city", "N/A"))
    print(red + "<--------------->" + red)
    print(a, "[ZIP Code]:", data.get("zip", "N/A"))
    print(red + "<--------------->" + red)
    print(b, "[ISP]:", data.get("isp", "N/A"))
    print(red + "<--------------->" + red)
    print(a, "[Organisation]:", data.get("org", "N/A"))
    print(red + "<--------------->" + red)
    print(b, "[AS]:", data.get("as", "N/A"))
    print(red + "<--------------->" + red)
    print(a, "[Latitude]:", data.get("lat", "N/A"))
    print(red + "<--------------->" + red)
    print(b, "[Longitude]:", data.get("lon", "N/A"))
    print(red + "<--------------->" + red)
    print(a, "[Time Zone]:", data.get("timezone", "N/A"))
    print(" " + yellow)

    latitude = data.get("lat", None)
    longitude = data.get("lon", None)

    if latitude and longitude:
        google_maps_url = f"https://www.google.com/maps?q={latitude},{longitude}"
        print(lgreen + f"[*] Open this location in Google Maps: {google_maps_url}" + clear)
        
        # Searching for nearby police stations or cyber centers using Google Places API
        places_params = {
            "location": f"{latitude},{longitude}",
            "radius": 5000,  # Radius in meters (5000 meters = 5 km)
            "type": "police",  # You can change this to other types like 'cyber_cafe', 'cybercrime_center', etc.
            "key": google_maps_api_key
        }

        places_response = requests.get(places_api_url, params=places_params)
        places_data = places_response.json()

        if places_data.get("results"):
            print(lgreen + "\n[*] Nearby Police Stations/Cybercrime Centers:\n" + clear)
            for place in places_data["results"]:
                print(f"{lgreen}[+] {place['name']} - {place['vicinity']}{clear}")
        else:
            print(red + "[~] No nearby police stations or cybercrime centers found." + clear)
    else:
        print(red + "[~] Location coordinates are missing. Unable to open Google Maps." + clear)

except KeyboardInterrupt:
    print("\n" + red + "[~] Terminating. Bye!" + clear)
    sys.exit(0)
except requests.exceptions.ConnectionError:
    print(red + "[~] Check your internet connection!" + clear)
    sys.exit(1)
except Exception as e:
    print(red + f"[~] An unexpected error occurred: {e}" + clear)

if latitude and longitude:
    open_in_browser = input(yellow + "[*] Do you want to open this location in your browser? (y/n): " + clear).strip().lower()
    if open_in_browser == "y":
        webbrowser.open(google_maps_url)
        print(lgreen + "[*] Google Maps opened in your default browser." + clear)
