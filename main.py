import boot
import urequests
import json
import machine
import neopixel
import time

#airnowapi setup
API_KEY ='Your Key Goes Here' #Sign up for an API Key at https://docs.airnowapi.org/
ZIP_CODE = 'Your 6 digit zip code' #Enter your zipcode as a string
RADIUS = '1' #Enter the radius in miles as a string
BASE_URL = 'http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&' #

# NeoPixel RGB LED Setup
pixel_pin = machine.Pin(14) #define the pin the led is on
led_number = 12 # how many neopixels are on this pin
np = neopixel.NeoPixel(pixel_pin, led_number)


AQI_palette = [(0,228,0), #GREEN 0-50 GOOD
                (255,255,0), #YELLOW 51-100 MODERATE
                (255,126,0), #ORANGE 101-150 UNHEALTHY FOR SENSITIVE GROUPS
                (255,0,0), #RED 151-200 UNHEALTHY
                (153,0,76), #PURPLE 201-300 VERY UNHEALTHY
                (126,0,35) #MAROON 301-500 HAZARDOUS
                ]



def request_url():
    """takes the variables, (ZIP, KEY, RADIUS) to build an appropriate request URL """
    return(BASE_URL+'zipCode='+ZIP_CODE+'&'+'distance'+RADIUS +'&API_KEY=' + API_KEY)


def check_AQI():
    getresponse = urequests.get(request_url())
    response = getresponse.json()
    current_AQI = response[1]['AQI']
    return(current_AQI)

def find_color(AQI):
    if AQI<=50:
        return(0)
    elif AQI>=51 and AQI<=100:
        return(1)
    elif AQI>=101 and AQI<=150:
        return(2)
    elif AQI>=151 and AQI<=200:
        return(3)
    elif AQI>=201 and AQI<=300:
        return(4)
    elif AQI>=301:
        return(5)
    else:
     retun(none)

def main():
    while True:
        for i in range(led_number):
            try:
                current_AQI = check_AQI()
                print(current_AQI)
                color_index = find_color(current_AQI)
                color = AQI_palette[color_index]
                np[i]=(color)
                np.write()
                time.sleep(60)
            except(OSError, MemoryError) as e: #if the main loop hits a snag the first led blinks red
                while True:
                    np[0] = (20,0,0)
                    np.write()
                    time.sleep(.5)
                    np[0] = (200, 0, 0)
                    np.write()
                    time.sleep(.5)


np.fill((0,25,4))
np.write()
boot.connect()
time.sleep(.5)
np.fill((0,0,0))
np.write()
main()
