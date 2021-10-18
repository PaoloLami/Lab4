import RPi.GPIO as GPIO
import cgi
import cgitb # optional, for better exception handling
cgitb.enable() # optional
ledPin = 17
GPIO.setmode(GPIO.BCM) # choose pin numbering convention (alt = BOARD)
GPIO.setwarnings(False) # ignore warnings due to multiple scripts at same time
GPIO.setup(ledPin, GPIO.OUT)
# Begin generation of web page showing current state:
print ('Content-type:text/html\n\n') # blank line = end of headers
print ('<html>')
print ('<head>')
print ('<title>LED switch test</title>')
print ('<meta http-equiv="refresh" content="30">') # update every 30 sec
print ('</head>')
print ('<body>')
print ('<div style="width:600px;background:#AAAAFF;border:1px;textalign:center">')
print ('<br>')
print ('<font size="3" color="black" face="helvetica">')
print ('<b>LED switch</b>')
print ('<br><br>')
# look at POST data for either 'on' or 'off' button names, using
# "if ('on' in form)" instead of data.getvalue() since we have 2 different
# button names (unlike prior example with a single button name & 2 values):
form = cgi.FieldStorage() # get POST data
if ('on' in form):
  GPIO.output(ledPin, 1)
elif ('off' in form) :
  GPIO.output(ledPin, 0)
# display current LED state to user:
if GPIO.input(ledPin):
  print ('<font color="red"> LED IS ON')
else:
  print ('<font color="black"> LED IS OFF')

print ('<font color="black">')
print ('<br><br>')
# Create the buttons to change LED state. Use 'target="_blank"
# to open in a new window if desired:
print ('<form action="/cgi-bin/led.py" method="POST" target="_self">')
print ('<input type="submit" name="on" value="Turn LED ON" />')
print ('<input type="submit" name="off" value="Turn LED OFF" />')
print ('</form>')
print ('<br>')
print ('</body>')
print ('</html>')