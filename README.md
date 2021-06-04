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

## Demo
The pictures bellow represent a model of a city by a 30 by 30 grid with pollutiion clusters and
5 bus lines.
![non interpolated](https://theorycorner.com/static/img/0-bcflow.png)
![interpolated](https://theorycorner.com/static/img/1-bcflow.png)
![1](https://theorycorner.com/static/img/2-bcflow.png)
![2](https://theorycorner.com/static/img/3-bcflow.png)
![3](https://theorycorner.com/static/img/4-bcflow.png)
![4](https://theorycorner.com/static/img/5-bcflow.png)
![5](https://theorycorner.com/static/img/6-bcflow.png)
![6](https://theorycorner.com/static/img/gif.gif)
