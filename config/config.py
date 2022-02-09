## Author          : Jolo Tolentino
## Project Name    : SEER-V2
## Project Started : January 25,2022



## Run config.py to Setup Library for SEER-V2

import os

import yaml 
import argparse


BaseDir =  str(os.path.dirname(os.getcwd()))

default_config_file = [
    {
        "model": "model-f6b98070.onnx",
        "model path":  BaseDir+"\models",
        "Camera Config": {
            "Camera Name": "Logitech C270",
            "Focal Length": 30,
            "Field of View" : 55,
            "Sensor Height" : None, 
        },
        # DETECTOR CONFIG
        "Yolo CFG":BaseDir+"\data\Yolo.cfg",
        "Yolo Weights": BaseDir+"\models\Yolo.weights",
        "Yolo Labels": BaseDir+"\data\coco.names",
        # "Image Scale": 
        



        

    }
]








Known_Heights = [
    {
        "Things":{
            "humans":180,
            "bottle":30,
            "dog":70
        }
    }
]


args = argparse.ArgumentParser(description="Settings Configurations for SEER V2 Backend")
args.add_argument("--model",type=str,required=False)
args.add_argument("--FOV",type=int,required=False)
args.add_argument("--FocalLength",type=int,required=False)
# args.add_argument("--SensorHeight", type = int, required = True)

args = args.parse_args()


if args.model:
    default_config_file[0]['model'] = args.model
    print(default_config_file[0]['model'])




with open('config.yaml', 'w') as outfile:
    yaml.dump(default_config_file, outfile, default_flow_style=False)



with open('../data/YAML/heights.yaml', 'w') as outfile:
    yaml.dump(Known_Heights, outfile, default_flow_style=False)
