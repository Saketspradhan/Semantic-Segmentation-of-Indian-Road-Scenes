import json
import glob
from pathlib import Path
import os
base_path = "C:/Users/hp/Desktop/Projects/WIRIN/"
jsons_path = base_path+"jsons/"

annotations = glob.glob(jsons_path+"*.json")
print(annotations)
# create txt file
temp = base_path+"txts/output.json"
print(temp)
f = open(temp,"w")
output_json = dict()

for i in annotations:
  print(i)
  with open(i, "r") as infile:
    json_object = json.loads(infile.read())
  size = 1976*1452
  # Map all class names to class id
  class_dict = {'road': 1, 'sidewalk': 2, 'building': 3, 'wall': 4, 'fence': 5, 'pole': 6, 'traffic_light': 7, 'traffic_sign': 8, 'vegetation': 9, 'terrain': 10, 'sky': 11, 'person': 12, 'car': 13, 'truck': 14, 'bus': 15, 'train': 16, 'motorcycle': 17, 'bicycle': 18, 'unknown': 19, 'rider': 20, 'tunnel': 21, 'autorickshaw': 22, 'animal': 23, 'rail_track': 24, 'guard_rail': 25, 'miscellaneous_vehicles': 26, 'pillar': 27, 'bridge': 28, 'divider': 29}

  region = []
  # Get class id for this record
  for j in json_object:
    all_x = []
    all_y = []
    if j['selected']:
      label = j['selected'][1]['value']
      print(label)
      if label in class_dict.keys():
        
        class_id = class_dict[label]
        print(label)
        # Get the max and min values from segmented polygon points 
        normalizedVertices = j["vertices"]
        # print(normalizedVertices)
        for k in normalizedVertices:
          all_x.append(float(k['x']))
          all_y.append(float(k['y']))
        region.append({"shape_attributes":{"name":"polygon","all_points_x":all_x,"all_points_y":all_y},"region_attributes":{"class":label}})
      else:
        print(i,label)
  filename = Path(i).stem+".png"
  output_json[filename]={"filename":filename,"size":size,"regions":region}
  print(output_json)
f.write(str(output_json).replace("'", '"'))
f.close()