SSID = 'My Network Name' #Enter your Wifi SSID as a string
SSID_PW = 'Secret Password' #enter your WiFi password as a string
def connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(SSID, SSID_PW)
        # while the below while loop is part of the standard recommended approach,
        # I found it could hang the device if run with connect() on boot
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())

def clock():
    from ntptime import settime
    import utime
    settime()
    print('current time:', utime.localtime())

def showip():
    import network
    sta_if = network.WLAN(network.STA_IF)
    print('network config:', sta_if.ifconfig())

# the connect() line can be uncommented if you want the ESP to connect
# to WiFi automatically when it boots. If you uncomment this, be sure
# you have tested it first with your network.
#
# connect()
