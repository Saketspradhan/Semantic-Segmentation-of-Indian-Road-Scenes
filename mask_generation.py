import sys
import json
from PIL import Image, ImageDraw

    #Semantic Segmentation Mask mask_generation
    #Azure DevOps Link: https://devops.wirin.in/wirin/National%20Dataset
    #Copyright, Wipro Limited 2022

    #The file should be called as follows
    #python3 mask_generation.py RAWIMAGE.png RAWIMAGE_JSON.json output.png 
    #Please pass parameters accordingly

def generate_mask(filename, jsonfile, outputfile):
    img = Image.open(filename)
    drawing = ImageDraw.Draw(img, 'RGBA')
    annotations_data = open(jsonfile)
    json_data = json.load(annotations_data)
    for i in range(len(json_data)):
        xy=[]
        for j in range(len(json_data[i]['vertices'])):
            xy.append((float(json_data[i]['vertices'][j]['x']),float(json_data[i]['vertices'][j]['y'])))
            color=json_data[i]['color']
            color=color[4:len(color)]
            color=color.replace(" ", "")
            color=color.replace("(", "")
            color=color.replace(")", "")
            color=color.replace("0.4", "110")
            colorstuple=tuple(int(x) for x in color.split(","))
        drawing.polygon(xy, fill=colorstuple, outline=colorstuple[0:3]) 
    img.save(outputfile, 'PNG')

if __name__=="__main__":
    # generate_mask(sys.argv[1], sys.argv[2], sys.argv[3])
    generate_mask('2021-02-26-12-07-51_BLR_IND_Frame01060.png', '2021-02-26-12-07-51_BLR_IND_Frame01060.json', 'le_output_3.png')
    
