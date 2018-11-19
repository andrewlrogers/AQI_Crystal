# Air Quality Index Crystal
![gif](https://raw.githubusercontent.com/andrewlrogers/AQI_Crystal/master/AQI_Crystal.gif "A gif showing the crystal in action")
#### About
For the past week smoke and particulate matter from the Camp Fire in Northern California has lingered in San Francisco, creating a hazardous environment. The EPA ranks the air quality with the Air Quality Index, a value that ranges from 0 - 500. San Francisco often stays in the 'good' range of 0-50, but recently was in the 'very-unhealthy' range. School and businesses have been canceling activities and government officials are encouraging residents to shelter indoors and wear a NIOSH N95 mask when outdoors.

As we increasingly deal with the impact of global climate change it seemed appropriate to create a visualization of the AQI, so I can determine if I need to wear a mask before heading outdoors. Fortunately, the EPA has an API for checking the current AQI by zipcode at [airnowapi.org](https://airnowapi.org). Additionally, the EPA has assigned colors for the different ranges and provides [specific hexidecimal color codes](https://docs.airnowapi.org/aq101) for each.

This project checks the AQI at a regular interval and adjusts the color of a series of LEDS. The project is fit inside a selenite crystal lamp because it diffuses the colors and looks really cool.

#### Why Micropython and not Circuit Python?
I explored Circuit Python because I was interested in using the Adafruit Fancy Led library, but ultimately Circuit Python lacked a `urequests` alternative.

## Materials

+ [1 Adafruit Feather HUZZAH with ESP8266](https://www.adafruit.com/product/2821)
+ [1 NeoPixel Ring - 12 x 5050 RGB LED](https://www.adafruit.com/product/1643)
+ [1 Selenite Crystal Lamp](https://www.amazon.com/Selenite-Crystal-Electric-lamp-Cord/dp/B077LD5P5G/ref=asc_df_B077LD5P5G/?tag=hyprod-20&linkCode=df0&hvadid=242019590558&hvpos=1o5&hvnetw=g&hvrand=3662701919086755367&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9031945&hvtargid=aud-466346483690:pla-429162419688&psc=1)
+ Assorted wires and tools including soldering iron

## Assembly
1. Solder wires to NeoPixel Ring
2. Solder wires to Feather HUZZAH
  * Connect ground to ground, 3v to 3v, and Data in to Pin 14
3. Slide into the Selenite Crystal

## Setup and Configuration
1. [Download and install micropython on the Feather HUZZAH](https://learn.adafruit.com/micropython-basics-how-to-load-micropython-on-a-board/)
2. Download or Clone this repository
3. Open `boot.py` and add your `SSID` and `SSID_PW`
4. Request API Access at [airnowapi.org](https://airnowapi.org)
  * Copy your **top secret** API KEY
5. Open `main.py` and add your `API_KEY` and `ZIP_CODE` as a string
6. [Load the code onto the Feather HUZZAH] (https://learn.adafruit.com/micropython-basics-load-files-and-run-code/overview)


## Resources
[airnowapi.org](https://airnowapi.org)
[video trailer on Vimeo](https://vimeo.com/301542921)
