import math
print('This program calculates the area and circumference :');
r = float(input('Enter the radius of the circle :'));
a = math.pi*r**2;
c = math.pi*r*2;
print('Area of the circle is :',round(a,2));
print('Circumference of the circle is :',round(c,2));
