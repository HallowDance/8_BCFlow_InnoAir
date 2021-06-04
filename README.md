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
  3.-7. soft prediction of decreased pollution if line is taken to be utilized
fully (i.e, no other traffic on line)

Red represents more pollution, green represents less.

## Demo
The pictures bellow represent a model of a city by a 30 by 30 grid with pollution clusters and
5 bus lines.

[Non-interpolated](https://theorycorner.com/static/img/0-bcflow.png)  
[Interpolated](https://theorycorner.com/static/img/1-bcflow.png)  
[With Line 1](https://theorycorner.com/static/img/0-bcflow.png)  
[With Line 2](https://theorycorner.com/static/img/0-bcflow.png)  
[With Line 3](https://theorycorner.com/static/img/0-bcflow.png)  
[With Line 4](https://theorycorner.com/static/img/0-bcflow.png)  
[With Line 5](https://theorycorner.com/static/img/0-bcflow.png)  

The images above are compiled to a demo gif:


