print('This program converts KM to MILES');

dist = float( input('Enter the distance in kilometres : '));
miles = dist/1.609344 ;

print('The distance in KM is :',dist,'&', 'distance in miles is :',round(miles, 4));
