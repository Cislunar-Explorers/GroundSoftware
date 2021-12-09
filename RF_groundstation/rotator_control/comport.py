import serial
import time
import os 
from time import sleep

# Necessary Comm Port information (need to check syntax)
port = "COM3"
baud = 9600
# loop variable
loop = 1

print ("Enter 1 to stop rotation.")
print ("Enter 2 to obtain rotator status.")
print ("Enter 3 to quit program.")

#Open serial port
ser = serial.Serial(port, baud, timeout = 0)

while loop == 1:

   #take azimuth input
   print (" ")
   input_variable = input ("Enter azimuth: ")
   az = int(input_variable)

   if az == 1:
      # Build stop command
      out = chr(87)+chr(0)+chr(0)+chr(0)+chr(0)+chr(0)+chr(0)+chr(0)+chr(0)+chr(0)+chr(0)+chr(15)+chr(32)
      x = ser.write(out)    
      # Allow for controller response with wait time
      sleep (0.75)

      data = ser.read(9999)
	  # once all 12 characters are received, decode location.
      if len(data) >= 12:
         s1 = ord(data[1].encode('latin-1'))
         s2 = ord(data[2].encode('latin-1'))
         s3 = ord(data[3].encode('latin-1'))
         s4 = ord(data[4].encode('latin-1'))
         s5 = ord(data[5].encode('latin-1'))
         s6 = ord(data[6].encode('latin-1'))
         s7 = ord(data[7].encode('latin-1'))
         s8 = ord(data[8].encode('latin-1'))
         s9 = ord(data[9].encode('latin-1'))
         s10 = ord(data[10].encode('latin-1'))
         azs = s1*100 + s2*10 + s3 + s4/10
         els = s6*100 + s7*10 + s8 + s9/10
	 # Account for 360 degree shift
         azs = azs - 360
         els = els - 360
		 
	
   elif az == 2:
      # Build the status command word.
      out = chr(87)+chr(0)+chr(0)+chr(0)+chr(0)+chr(0)+chr(0)+chr(0)+chr(0)+chr(0)+chr(0)+chr(31)+chr(32)
      x = ser.write(out)
      # Wait for answer from controller
      sleep (0.75)

      data = ser.read(9999)
      #/dev/print len(data)
      # once all 12 characters are received, decode location.
      if len(data) >= 12:
         s1 = ord(data[1].encode('latin-1'))
         s2 = ord(data[2].encode('latin-1'))
         s3 = ord(data[3].encode('latin-1'))
         s4 = ord(data[4].encode('latin-1'))
         s5 = ord(data[5].encode('latin-1'))
         s6 = ord(data[6].encode('latin-1'))
         s7 = ord(data[7].encode('latin-1'))
         s8 = ord(data[8].encode('latin-1'))
         s9 = ord(data[9].encode('latin-1'))
         s10 = ord(data[10].encode('latin-1'))
         azs = s1*100 + s2*10 + s3 + s4/10
         els = s6*100 + s7*10 + s8 + s9/10
         # Since the controller sends the status based on 0 degrees = 360
         # remove the 360 here
         #print (s1,s2,s3,s4,s5,s6,s7,s8,s9,s10)
         azs = azs - 360
         els = els - 360
         print ("Rotator currently at %3d " %(azs)+ "Degrees Azimuth and %3d " %(els) + "Degrees Elevation")
         print ("Azimuth multiplier is %3d "%(s5)+ "  Elevation Multiplier is %3d "%(s10))

         
   elif az == 987:
      # Program is ending so escape the loop.
      loop = 0

   else:    # assuming proper azimuth and elevation input
            
            #test azimuth range
      if (az >= 0 and az < 361):
         loop1 = 0
         # Now it is time to get the Elevation 
         while loop1 == 0:
           input_variable = input("Enter Elevation: ")
           el = int(input_variable)
           # Test elevation range
           if (el >= 0 and el < 180):
              loop1 = 1
              #Convert Azimuth and Elevation to number required by controller
              az = az + 360
              el = el + 360
              
              az = az * 10
              el = el * 10

              azm = str(az)
              elm = str(el)
              if len(azm) == 3:
                 azm = "0" + azm
              if len(elm) == 3:
                 elm = "0" + elm
  
              # Build message to be sent to controller
              
              out = chr(87) + azm + chr(10)+elm + chr(10)+chr(47)+chr(32)

              #Send message to Controller
              x = ser.write(out)
              # Wait for answer from controller
              sleep (0.75)

              data = ser.read(9999)
		 
           else:   
              print ("Invalid Elevation")
      else:   
         print ("Invalid Azimuth")
              		
ser.close()


