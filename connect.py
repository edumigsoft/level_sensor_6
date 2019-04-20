#
#
#
import const
import network

def do_connect():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print("Connecting to network")
        sta_if.active(True)
        sta_if.connect(const.WIFI_SSID, const.WIFI_PASSWD)
        while not sta_if.isconnected():
            pass
            #print('.')
    #print("\r\n")
    print("Network config: " + str( sta_if.ifconfig()))
    print("\r\n")

    return sta_if.isconnected()
#####################################################################
