from http.server import BaseHTTPRequestHandler, HTTPServer
import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib
from w1thermsensor import W1ThermSensor
import threading
import time

sensor = W1ThermSensor()
GpioPins = [17, 18, 27, 22]
mymotor = RpiMotorLib.BYJMotor("MyMotorOne", "28BYJ")

virtualTemp = 69
realTemp = int()


class PutHandler(BaseHTTPRequestHandler):
    # Initialize a variable to store the put request content
    put_content = ""

    def do_PUT(self):
        global virtualTemp
        print("data received!")
        # Get the length of the put request content
        content_length = int(self.headers['Content-Length'])
        # Read the put request content
        put_data = self.rfile.read(content_length)
        # Update the put_content variable with the put request content
        self.put_content = put_data.decode()
        virtualTemp = int(self.put_content)
        # Send a response indicating that the put request was successful
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(str(virtualTemp), "utf8"))
        print(virtualTemp)
        moveMotor()

def run():
    # Set the listening address and port for the server
    server_address = ('192.168.137.142', 8000)
    httpd = HTTPServer(server_address, PutHandler)
    print("Starting server on port 8000...")
    httpd.serve_forever()

def moveMotor():
    global realTemp
    tempF =sensor.get_temperature()
    realTemp = int(tempF * 1.8 + 32)
    print ("virtualTemp = " +str(virtualTemp) +"F realTemp = " + str(realTemp) + "F")
    time.sleep(.1)
    if(virtualTemp<realTemp):
        print("decreasing...")
        mymotor.motor_run(GpioPins , .01, 30, False, False, "full", .05) #decrease
    elif(virtualTemp>realTemp):
        print("increasing...")
        mymotor.motor_run(GpioPins , .01, 30, True, False, "full", .05) #increase
    elif(virtualTemp == realTemp):
        print("just right :)")
        time.sleep(2)
def adjustTemp():
    while True:
        moveMotor()
        time.sleep(15)
temp_thread = threading.Thread(target=adjustTemp)
temp_thread.start()
   
run()
