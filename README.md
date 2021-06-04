# 8_BCFlow_InnoAir
Modeling public transport lines and air quality - a part of the *InnoAir Challenge: Making Urban Mobility Smarter*


## Requirements
```
python3
numpy
matplotlib
```

## Usage
At the current stage, this is a terminal application. 

In order to start a "simulation", run `evaluateLines.py`. The program will
create 7 images in the `img` folder:
  1. non-interpolated data
  2. interpolated data
  3.-7. soft prediction of decreased pollutiion if line is taken to be utilized
fully (i.e, no other traffic on line)

Red represents more polution, green represents less.
