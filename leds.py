#!/usr/bin/python37all
import cgi
data = cgi.FieldStorage()
ledcolor = data.getvalue('option') #gets LED color selected from web page
s1 = data.getvalue('slider1') #gets slider value for the pwn function
if ledcolor == 'r': #if Red LED option is selected
    with open('red_pwm.txt', 'w') as f:
      f.write(str(s1))
if ledcolor == 'b': #if Blue LED option is selected
    with open('blue_pwm.txt', 'w') as f:
      f.write(str(s1))
if ledcolor == 'g': #if Green LED option is selected
    with open('green_pwm.txt', 'w') as f:
      f.write(str(s1))
      
print('Content-type: text/html\n\n')
print('<html>')
print('<form action="/cgi-bin/leds.py" method="POST">')
print('<input type="radio" name="option" value="r"> Red LED <br>')
print('<input type="radio" name="option" value="b"> Blue LED <br>')
print('<input type="radio" name="option" value="g"> Green LED <br>')
print('<input type="range" name="slider1" min="0" max="100" value="%s"><br>' % s1)
print('<input type="submit" value="Change LED brightness">')
print('</form>')
print('Brightness = %s' % s1)
print('</html>')
