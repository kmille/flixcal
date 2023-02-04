# FLIXTRAIN ics generator

Flixtrain does not give you a .ics file to import. This code generates a ics file with all connections of your order. In order to do so, it uses chromiums cookies and sends a request to flixtrain's backend (https://shop.flixbus.de/booking/success/eventOrder). It's best if your are done with the order and see the summary of your order to run the script (https://shop.flixbus.de/booking/success). After parsing the json, it generats an ics and saves it into your Downloads directory.

```
git clone https://github.com/kmille/flixcal.git
```
