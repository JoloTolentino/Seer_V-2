## Author          : Jolo Tolentino
## Project Name    : Quaternion Understanding through PyGame and Matplotlib
## Project Started : February 25,2022

### I investigate the difference between the use of Euler Angles and Quaternions

#Hamilton’s Quaternions

import numpy as np 
import math as m
import matplotlib.pyplot as plt 
import sys



class Vector_Rotation:
    def __init__(self,vector,yaw = None, pitch= None, roll = None):
        if yaw and pitch and roll : 
            self.yaw =   yaw*(np.pi/180)   # Vector_Rotation along the X axis 
            self.pitch = pitch*(np.pi/180) # Vector_Rotation along the Y axis
            self.roll =  roll*(np.pi/180)  # Vector_Rotation along the Z axis
        
        if vector: 
            self.vector = vector

'To understand how to rotate objects using computer graphics we need to understand the importance of Euler Angles/ Tate-Bryan Angles and Quaternions'


class Euler_Angles(Vector_Rotation):

    
    def __init__(self,yaw=None,pitch=None,roll=None,vector=None):
        super().__init__(vector,yaw,pitch,roll)
        if yaw and pitch and roll: 
            self.yaw, self.pitch, self.roll = self.angle2rad(yaw),self.angle2rad(pitch),self.angle2rad(roll)
        if vector: 
            self.vector = np.array(vector).reshape(3,1)

    ### Established Vector_Rotations
    ## the columns represent the Vector_Rotation 
    
    def angle2rad(self,angle):
        return angle*(np.pi/180)

    def Vec_Rotate(self,vector,rotation,angle):
        return  np.dot(rotation(angle),vector)


    def Rot_X(self,yaw):
        yaw = self.angle2rad(yaw)
        return np.matrix([[ 1, 0           , 0       ],
                          [ 0, m.cos(yaw),-m.sin(yaw)],
                          [ 0, m.sin(yaw), m.cos(yaw)]])
            
    def Rot_Y(self,pitch):
        pitch = self.angle2rad(pitch)
        return np.matrix([[ m.cos(pitch), 0, m.sin(pitch)],
                          [ 0           , 1, 0           ],
                          [-m.sin(pitch), 0, m.cos(pitch)]])
            

    def Rot_Z(self,roll): 
        roll = self.angle2rad(roll)
        return np.matrix([[ m.cos(roll), -m.sin(roll), 0 ],
                          [ m.sin(roll), m.cos(roll) , 0 ],
                          [ 0         , 0            , 1 ]])

    def Tate_Bryan(self,matrix): #Vector_Rotation about 3 Axis (X,Y,Z) TATE -BRYAN angles 
        tol = sys.float_info.epsilon * 10
        #try this first
        if abs(matrix.item(0,0))< tol and abs(matrix.item(1,0)) < tol:
            phi = 0
            theta = m.atan2(-matrix.item(2,0), matrix.item(0,0))
            psi = m.atan2(-matrix.item(1,2), matrix.item(1,1))

        #then this 
        else:   
            phi = m.atan2(matrix.item(1,0),matrix.item(0,0))
            sp = m.sin(phi)
            cp = m.cos(phi)
            theta = m.atan2(-matrix.item(2,0),cp*matrix.item(0,0)+sp*matrix.item(1,0))
            psi = m.atan2(sp*matrix.item(0,2)-cp*matrix.item(1,2),cp*matrix.item(1,1)-sp*matrix.item(0,1))
        
        return np.round((phi*180)/np.pi,decimals=2),np.round((theta*180)/np.pi,decimals=2),np.round((psi*180)/np.pi,decimals=2)

    def Eueler(self,matrix): # Rotation between 2 Principal Axises (X,Y,X) .... and all the other permutations 
        phi = m.atan2(matrix.item(1,2),matrix.item(0,2))
        sp = m.sin(phi)
        cp = m.cos(phi)
        theta = m.atan2(cp*matrix.item(0,2)+sp*matrix.item(1,2), matrix.item(2,2))
        psi = m.atan2(-sp*matrix.item(0,0)+cp*matrix.item(1,0),-sp*matrix.item(0,1)+cp*matrix.item(1,1))

        return np.round((phi*180)/np.pi,decimals=2),np.round((theta*180)/np.pi,decimals=2),np.round((psi*180)/np.pi,decimals=2)


## Enter the Unknown 
'Quaternions can represent 3D vector rotation, and is arguably the better option over Euler Angles'
'Due to human nature, we always opt for the easier solution if it would suffice'
'But for our application we need to delve deeper into the 3D spatial mathematics to generate stability'


# resource taken from:
# https://www.euclideanspace.com/maths/geometry/Vector_Rotations/conversions/matrixToQuaternion/index.htm

class Quaternion(Vector_Rotation) :
    
    def __init__ (self,vector = None,yaw = None,pitch = None,roll = None,Vector_Rotation_matrix = None):
        if type(Vector_Rotation_matrix) == np.matrix: 
            self.q = self.RMat2Quat(Vector_Rotation_matrix)
            print(self.q)
        else: 
            super().__init__(vector, yaw, pitch,roll)
            # self.phi,self.theta, self.psi = self.yaw,self.pitch,self.roll

        # assert(vector )
    
    def RMat2Quat(self,Vector_Rotation_Matrix):
        # print(Vector_Rotation_Matrix[0][0])
        trace = Vector_Rotation_Matrix.item(0,0)+ Vector_Rotation_Matrix.item(1,1)+ Vector_Rotation_Matrix.item(2,2)
        
        if trace>0:
            S = np.sqrt(trace+1.0)*2 
            w = 0.25*S 
            x = (Vector_Rotation_Matrix.item(2,1) - Vector_Rotation_Matrix.item(1,2)) /S
            y = (Vector_Rotation_Matrix.item(0,2) - Vector_Rotation_Matrix.item(2,0)) /S
            z = (Vector_Rotation_Matrix.item(1,0) - Vector_Rotation_Matrix.item(0,1)) /S
        
            return w,x,y,z
        elif (Vector_Rotation_Matrix.item(0,0) > Vector_Rotation_Matrix.item(1,1) and (Vector_Rotation_Matrix.item(0,0)> Vector_Rotation_Matrix.item(2,2))):
            S = 2*np.sqrt(1 + Vector_Rotation_Matrix.item(0,0) - Vector_Rotation_Matrix.item(1,1)- Vector_Rotation_Matrix(2,2))*2
            w = (Vector_Rotation_Matrix.item(2,1) - Vector_Rotation_Matrix.item(1,2)) /S
            x = 0.25*S
            y = (Vector_Rotation_Matrix.item(0,1) - Vector_Rotation_Matrix.item(1,0)) /S
            z = (Vector_Rotation_Matrix.item(0,2) - Vector_Rotation_Matrix.item(2,0)) /S

            return w,x,y,z

        elif Vector_Rotation_Matrix.item(1,1) > Vector_Rotation_Matrix.item(2,2):
            S = 2*np.sqrt(1 + Vector_Rotation_Matrix[1][1] - Vector_Rotation_Matrix[0][0]- Vector_Rotation_Matrix[2][2])
            w = (Vector_Rotation_Matrix.item(0,2) - Vector_Rotation_Matrix.item(2,0)) /S
            x = (Vector_Rotation_Matrix.item(0,1) - Vector_Rotation_Matrix.item(1,0)) /S
            y = 0.25*S
            z = (Vector_Rotation_Matrix.item(1,2) - Vector_Rotation_Matrix.item(2,1)) /S

            return w,x,y,z
        
        else:
            S = 2*np.sqrt(1 + Vector_Rotation_Matrix.item(2,2) - Vector_Rotation_Matrix.item(0,0)- Vector_Rotation_Matrix.item(1,1))
            w = (Vector_Rotation_Matrix.item(1,0) - Vector_Rotation_Matrix.item(0,1)) /S
            x = (Vector_Rotation_Matrix.item(0,2) - Vector_Rotation_Matrix.item(2,0)) /S
            y = (Vector_Rotation_Matrix.item(1,2) - Vector_Rotation_Matrix.item(2,1)) /S
            z = 0.25*S

            return w,x,y,z



class Quaternion_Operations:

    def Rotate(self,q1, v1):
        q2 = (0.0,) + v1
        return self.Multiply(self.Multiply(q1, q2), self.Conjugate(q1))[1:]


    def Conjugate(self,quarterion):
        #quarterrions = w,x,y,z and their conjugates are w,-x,-y,-z
        return (quarterion[0],-quarterion[1],-quarterion[2],-quarterion[3])

    # cross product and dot products     
    def Multiply(self,quarterion1,quarterion2):
        w1, x1, y1, z1 = quarterion1
        w2, x2, y2, z2 = quarterion2
        w = w1 * w2 - x1 * x2 - y1 * y2 - z1 * z2
        x = w1 * x2 + x1 * w2 + y1 * z2 - z1 * y2
        y = w1 * y2 + y1 * w2 + z1 * x2 - x1 * z2
        z = w1 * z2 + z1 * w2 + x1 * y2 - y1 * x2
        return w, x, y, z

    def Euler_to_Quaternion(phi, theta, psi):

        qw = np.cos(phi/2) * np.cos(theta/2) * np.cos(psi/2) + np.sin(phi/2) * np.sin(theta/2) * np.sin(psi/2)
        qx = np.sin(phi/2) * np.cos(theta/2) * np.cos(psi/2) - np.cos(phi/2) * np.sin(theta/2) * np.sin(psi/2)
        qy = np.cos(phi/2) * np.sin(theta/2) * np.cos(psi/2) + np.sin(phi/2) * np.cos(theta/2) * np.sin(psi/2)
        qz = np.cos(phi/2) * np.cos(theta/2) * np.sin(psi/2) - np.sin(phi/2) * np.sin(theta/2) * np.cos(psi/2)

        return [qw, qx, qy, qz]

    def Quaternion_to_Euler(quaternion):
        qw,qx,qy,qz = quaternion
        X = m.atan2((2*(qw*qx+qy*qz)), (1-2*(qx*qx+qy*qy))) *(180/np.pi)
        Y = m.asin(1 if 2 * (qw * qy - qz * qx) > 1 else (-1 if 2 * (qw * qy - qz * qx)<-1 else 2 * (qw * qy - qz * qx)))*(180/np.pi)
        Z = m.atan2((2*(qw*qz + qx*qy)),(1-2*(qy*qy+qz*qz)))*(180/np.pi)

        return np.round((X, Y, Z), decimals=2) 



class Plot3D:
    def __init__(self,v1,v2):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.quiver(-1, 0, 0, 3, 0, 0, color='#aaaaaa',linestyle='dashed')
        ax.quiver(0, -1, 0, 0,3, 0,  color='#aaaaaa',linestyle='dashed')
        ax.quiver(0, 0, -1, 0, 0, 3, color='#aaaaaa',linestyle='dashed')
        ax.quiver(0, 0, 0, v1[0], v1[1], v1[2], color='b')
        ax.quiver(0, 0, 0, v2[0], v2[1], v2[2], color='r')
        ax.set_xlim([-1.5, 1.5])
        ax.set_ylim([-1.5, 1.5])
        ax.set_zlim([-1.5, 1.5])
        plt.show()







v1 = (1,0,0)
euler = Euler_Angles()

## Tate-Bryan Angles  ZYX
Rotation_Matrix = euler.Rot_Z(40) * euler.Rot_Y(45) * euler.Rot_X(80)



print(euler.Eueler(Rotation_Matrix))







# 'Comparitive analysis Conversion with Quaternions and Euler Conversion'
print(np.round(Rotation_Matrix, decimals= 2))
print(type(Rotation_Matrix))
quaternion = Quaternion(Vector_Rotation_matrix = Rotation_Matrix)
QueenOfPain = Quaternion_Operations.Quaternion_to_Euler(quaternion.q)
print(QueenOfPain)










# test = Vector_Rotation(v1,30,20,10)




# print(test.yaw)
	
# v1 = (1,0,0)

# phi = m.pi/2
# theta = m.pi/4
# psi = m.pi/2
# q = Quaternion.euler_to_quaternion(phi, theta, psi)

# print(q)

# test = Quaternion(0,0,0)
# #Vector_Rotation based on
# v2 = test.rotate(q,v1)


# # v3 = test.rotate2(q,v1)
# print(np.round(v2, decimals=2))
# # print(np.round(v3, decimals=2))

# import matplotlib.pyplot as plt
  
# 