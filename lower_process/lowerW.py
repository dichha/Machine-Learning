#!/usr/bin/python3
import cImage
import csv
comma = ","
for j in range(1,200):
        W = []
        f = cImage.FileImage("training/lower/W/"+str(j)+".gif")
        for row in range(f.getHeight()):
                for col in range(f.getWidth()):
                        p = f.getPixel(col,row)
                        s = (p.getRed()+p.getGreen()+p.getBlue())//3
                        W.append(str(s))
        W.append('W')
        print(comma.join(W))
