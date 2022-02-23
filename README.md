# SEER - V2

 Assistive Navigation through Monocular Depth Estimation, Object Detection and Object Pose Estimation.
 Estimating Spatial Perception through Computer Vision to Aid Autonomous Systems and the Visually Impaired for Day to Day Applications.


### The Novel Monocular Depth Estimation Solution: 
Spatial Recognition Provides the Visually Impaired and Autonomous Systems the Ability to Recognize Obstacles in their day to day interactions. Depth Maps are not new, although recently, the recent release of MiDas has provided a novel solution to generate Depth Maps. In the past, Stereo-Vision, Lidar solutions were the primary technique 

### The Object Detection Contribution :


### The Angle Orientation Principle : 
 In 3D graphics, we precieve object orientation through Pitch, Yaw and Roll (x,y and z rotation) of an Object. 
 If we were to extract the Euler Angles Of an Object, We are Able to Derive the projected 2D pixel Height of an Object from the 3D Bounding Box thus allowing us predict the distance Estimate.  

### Python Dependencies 
1. OpenCV (Cuda Compiled Optional)
2. MediaPipe 
3. Numpy 
4. Yaml
5. Models Folder with Corresponding Models

### C++ Dependencies 
1. OpenCV (Cuda Compiled Optional)
2. MediaPipe 
3. Models Folder with Corresponding Models

### JavaScript Dependencies


#### Streaming Options Available
- [x] TCP-IP
- [x] UDP

#### Streaming Options Available
- [x] Python API
- JavaScript API
- C++ API

### Project Update 
- [x] Calibration Testing
- [x] Calibration Module
- [x] Configuration Module
- [x] Depth Estimation Module (Required)
- [x] Object Detection Module (Required)
- Pose Estiamtion Module (Optional)
- Cliet-Server Module

### How to run 

1.  Using the command prompt terminal change the directory cd "~/DepthEstimator/src/"
2.  Configure Project first using "config.py" found in the config folder
3.  run the script "server-main.py" with the command "python server-main.py"
