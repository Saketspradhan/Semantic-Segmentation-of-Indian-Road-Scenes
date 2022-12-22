import json
import glob
from PIL import Image, ImageDraw
import sys
import os
from pathlib import Path
base_path = "C:/Users/hp/Desktop/Projects/WIRIN/"
json_folder_name = "jsons/"
image_folder_name = "images/"
outputimg_folder_name = "bbout/"
annotations = glob.glob(base_path+json_folder_name+"*.json")

for i in annotations:

  # print(i)
  with open(i, "r") as infile:
    json_object = json.loads(infile.read())
  img = Image.open(base_path+image_folder_name+Path(i).stem+".png")
  # print(base_path+image_folder_name+Path(i).stem+".png")
  drawing = ImageDraw.Draw(img, 'RGBA')
  # Map all class names to class id
  class_dict = {'road': 1, 'sidewalk': 2, 'building': 3, 'wall': 4, 'fence': 5, 'pole': 6, 'traffic_light': 7, 'traffic_sign': 8, 'vegetation': 9, 'terrain': 10, 'sky': 11, 'person': 12, 'car': 13, 'truck': 14, 'bus': 15, 'train': 16, 'motorcycle': 17, 'bicycle': 18, 'unknown': 19, 'rider': 20, 'tunnel': 21, 'autorickshaw': 22, 'animal': 23, 'rail_track': 24, 'guard_rail': 25, 'miscellaneous_vehicles': 26, 'pillar': 27, 'bridge': 28, 'divider': 29}


  # create txt file
  temp = base_path+outputimg_folder_name+Path(i).stem + ".png"
  print("Writing Image: "+temp)
  f = open(temp,"w")
  
  # Get class id for this record
  for j in json_object:
    if j['selected'] and j['selected'][1]['value'] not in ['divider','road','rail_track','guard_rail','pillar','bridge','building','wall','fence','pole','traffic_light','traffic_sign','vegetation','terrain','sky','unknown','tunnel','sidewalk']:
      color = j['selected'][1]['color']
      color=color[4:len(color)]
      color=color.replace(" ", "")
      color=color.replace("(", "")
      color=color.replace(")", "")
      color=color.replace("0.4", "110")
      colorstuple=tuple(int(x) for x in color.split(","))
      # print(label)

      # Get the max and min values from segmented polygon points 
      normalizedVertices = j["vertices"]
      max_x = max([float(v['x']) for v in normalizedVertices])
      max_y = max([float(v['y']) for v in normalizedVertices])
      min_x = min([float(v['x']) for v in normalizedVertices])
      min_y = min([float(v['y']) for v in normalizedVertices])
      
      # print(min_x,min_y,max_x,max_y)
      width = max_x- min_x
      height = max_y - min_y
      center_x = min_x + width/2
      center_y = min_y + height/2
      drawing.rectangle(((min_x,min_y),(max_x,max_y)), fill=colorstuple, outline=colorstuple[0:3]) 

  img.save(temp, 'PNG')
