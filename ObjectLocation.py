import cv2
from matplotlib import pyplot as plt
import math

class clPoint:
    def __init__(self, x: float, y: float, z: float = 0.0):
        self.x = x
        self.y = y
        self.z = z

    def distance_to(self, other: 'Point') -> float:
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2 + (self.z - other.z)**2)   


image = cv2.imread('tablet.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


cv2.imshow("orig", image)

t=80
ret, thresh = cv2.threshold(gray,t,255,cv2.THRESH_BINARY_INV)
cv2.imshow("filter", thresh)
cv2.waitKey()
# Canny Edge detection
canny = cv2.Canny(thresh, 0, 100)
cv2.imshow("canny", canny)




# Find contours
cnts = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2:]


# Getting the outor points of the object
Xmin = 0
Ymin = 0
Xmax = 0
Ymax = 0

XminCoord = []
YminCoord = []
XmaxCoord = []
YmaxCoord = []

for cont1 in cnts:
	for XYcoordList in cont1:
		
		for l,XYcoord in enumerate(XYcoordList):
			if l < len(XYcoordList) - 1:
				print ('Array: %.2f' %(l))	
				print (XYcoord[0])
				x,y = [0,0]
				try:
					x,y = XYcoord[0]
				except:	
					break
				
					
				if Xmin == 0 and Ymin == 0 and Xmax == 0 and Ymax == 0:
					Xmin = x
					Ymin = y
					Xmax = x
					Ymax = y
					XminCoord = XYcoord[0]
					XmaxCoord = XYcoord[0]
					YminCoord = XYcoord[0]
					YmaxCoord = XYcoord[0]
										
				else:
					if Xmin > x:
						Xmin = x
						XminCoord = XYcoord[0]
					if Xmax < x:
						Xmax  = x
						XmaxCoord = XYcoord[0]
					if Ymin > y:
						Ymin = y
						YminCoord = XYcoord[0]
					if Ymax < y:
						Ymax = y
						YmaxCoord = XYcoord[0]
			
print ("XminCoordX = %.2f XminCoordY = %.2f XmaxCoordX = %.2f XmaxCoordY = %.2f YminCoordX = %.2f YminCoordY = %.2f YmaxCoordX = %.2f YmaxCoordY = %.2f" %(XminCoord[0], XminCoord[1], XmaxCoord[0], XmaxCoord[1], YminCoord[0], YminCoord[1], YmaxCoord[0],YmaxCoord[1]))

#Tolerance of the pixels
pointTolerance = 160
#Points of the pixels
PointVars = [clPoint(XminCoord[0],XminCoord[1],0.0),clPoint(XmaxCoord[0],XmaxCoord[1],0.0),clPoint(YminCoord[0],YminCoord[1],0.0),clPoint(YmaxCoord[0],YmaxCoord[1],0.0)]

PointXmin = clPoint(XminCoord[0],XminCoord[1],0.0)
PointXmax = clPoint(XmaxCoord[0],XmaxCoord[1],0.0) 
PointYmin = clPoint(YminCoord[0],YminCoord[1],0.0) 
PointYmax = clPoint(YmaxCoord[0],YmaxCoord[1],0.0) 

cv2.circle(image,(XminCoord[0],XminCoord[1]), 10, (0,255,0), 5)
cv2.circle(image,(XmaxCoord[0],XmaxCoord[1]), 10, (0,255,0), 5)
cv2.circle(image,(YminCoord[0],YminCoord[1]), 10, (0,255,0), 5)
cv2.circle(image,(YmaxCoord[0],YmaxCoord[1]), 10, (0,255,0), 5)

#Calculating image vectors
vect1 = PointXmin.distance_to(PointXmax)
print ("Internal vector 1: %.2f" %(vect1))
vect2 = PointXmin.distance_to(PointYmax)
print ("Internal vector 2: %.2f" %(vect2))
vect3 = PointXmin.distance_to(PointYmin)
print ("Internal vector 3: %.2f" %(vect3))
vect4 = PointXmax.distance_to(PointYmin)
print ("Internal vector 4: %.2f" %(vect4))
vect5 = PointXmax.distance_to(PointYmax)
print ("Internal vector 5: %.2f" %(vect5))
vect6 = PointYmin.distance_to(PointYmax)
print ("Internal vector 6: %.2f" %(vect6))

#Input data
externalDataPoints = [clPoint(0,0,0),clPoint(1390,0,0),clPoint(1390,1900,0),clPoint(0,1900,0)]


#Calculation of the external vectors
extneralVect1 = 0
extneralVect2 = 0 
extneralVect3 = 0
extneralVect4 = 0
extneralVect5 = 0
extneralVect6 = 0

sourceVectors = []

if len(externalDataPoints) > 0:
	
	l = len(externalDataPoints)
	print ("Amount of externalDataPoints %.2f" %(l))
	if l == 2:
		externalVect1 = externalDataPoints[0].distance_to(externalDataPoints[1])
		sourceVectors.append(externalVect1)
		print ("source vector one added")		
	if l == 3:
		externalVect1 = externalDataPoints[0].distance_to(externalDataPoints[1])
		print ("External vector 1: %.2f" %(externalVect1))
		externalVect2 = externalDataPoints[0].distance_to(externalDataPoints[2])
		print ("External vector 2: %.2f" %(externalVect2))
		externalVect3 = externalDataPoints[1].distance_to(externalDataPoints[2])
		print ("External vector 3: %.2f" %(externalVect3))
		sourceVectors.append(externalVect1)
		sourceVectors.append(externalVect2)
		sourceVectors.append(externalVect3)
		print ("source vector three added")
	if l == 4:
		externalVect1 = externalDataPoints[0].distance_to(externalDataPoints[1])
		print ("External vector 1: %.2f" %(externalVect1))
		externalVect2 = externalDataPoints[0].distance_to(externalDataPoints[2])
		print ("External vector 2: %.2f" %(externalVect2))
		externalVect3 = externalDataPoints[0].distance_to(externalDataPoints[3])
		print ("External vector 3: %.2f" %(externalVect3))
		externalVect4 = externalDataPoints[1].distance_to(externalDataPoints[2])
		print ("External vector 4: %.2f" %(externalVect4))
		externalVect5 = externalDataPoints[1].distance_to(externalDataPoints[3])
		print ("External vector 5: %.2f" %(externalVect5))
		externalVect6 = externalDataPoints[2].distance_to(externalDataPoints[3])
		print ("External vector 6: %.2f" %(externalVect6))
		sourceVectors.append(externalVect1)
		sourceVectors.append(externalVect2)
		sourceVectors.append(externalVect3)
		sourceVectors.append(externalVect4)
		sourceVectors.append(externalVect5)
		sourceVectors.append(externalVect6)
		print ("source vector six added")
else:
	print('Not enough points in the source drawing');

#Match the vectors
imageVectors = [vect1,vect2,vect3,vect4,vect5,vect6]

sortImageVectors = sorted(imageVectors)
sortSourceVectors = sorted(sourceVectors) 

sortSourceMatches = []
for y, sortSourceVector in enumerate(sortSourceVectors):
	sortSourceMatches.append(0)

#check if the vectors match
sourceMatchEvalIndex = 1000
print ("Matching started")
print (sortImageVectors)
print (sortSourceVectors)
for i,sortSourceVector in enumerate(sortSourceVectors):
	print ("To find %.2f" %(i))
	for j,sortImageVector in enumerate(sortImageVectors):
		print ("To find %.2f" %(j))
		if (((sortSourceVector - pointTolerance) <= sortImageVector) and ((sortSourceVector + pointTolerance) >= sortImageVector)):
			sortSourceMatches[i] = 1
			print ("Match found %.2f" %(j))
			if sourceVectors[0] == sortSourceVector:
				sourceMatchEvalIndex = j
print ("Index of vector found %.2f" %(sourceMatchEvalIndex))
				
#check if the matches are completed
sourceMatchEval = 1
for i, sortSourceMatch in enumerate(sortSourceMatches):
	if sortSourceMatch == 0:
		sourceMatchEval = 0


checkVecIndex = 1000
if sourceMatchEval == 1:
	imageValueToCheck = sortImageVectors[sourceMatchEvalIndex]
	
	for k,imageVector in enumerate(imageVectors):
		if imageValueToCheck == imageVector:
			#found top level xmin xmax
			checkVecIndex = k
			break
			
	calcPointStart = clPoint(0,0,0)
	calcPointEnd = clPoint(0,0,0)
	calcPointVector = 0
	if k == 1:
		calcPointStart = PointXmin
		calcPointEnd = PointXmax
		calcPointVector = PointXmax.distance_to(PointXmin)
	if k == 2:
		calcPointStart = PointXmin
		calcPointEnd = PointYmax
		calcPointVector = PointYmax.distance_to(PointXmin)
	if k == 3:
		calcPointStart = PointXmin
		calcPointEnd = PointYmin
		calcPointVector = PointXmin.distance_to(PointYmin)
	if k == 4:
		calcPointStart = PointXmax
		calcPointEnd = PointYmin
		calcPointVector = PointYmin.distance_to(PointXmax)
	if k == 5:
		calcPointStart = PointXmax
		calcPointEnd = PointYmax
		calcPointVector = PointYmax.distance_to(PointXmax)
	if k == 6:
		calcPointStart = PointYmin
		calcPointEnd = PointYmax
		calcPointVector = PointYmax.distance_to(PointYmin)

	cosAlfa = (calcPointEnd.x - calcPointStart.x)/calcPointStart.distance_to(calcPointEnd)
	radians = math.acos(cosAlfa)
	#sinAlfa = math.sin(radians)
	degrees = radians * (180.0 / math.pi)


	calcPointStartSource = clPoint(0,0,0)
	calcPointEndSource = clPoint(0,0,0)
	calcPointVectorSource = 0
	if k == 1:
		calcPointStartSource = externalDataPoints[0]
		calcPointEndSource = externalDataPoints[1]
		calcPointVectorSource = externalDataPoints[1].distance_to(externalDataPoints[0])
	if k == 2:
		calcPointStartSource = externalDataPoints[0]
		calcPointEndSource = externalDataPoints[2]
		calcPointVectorSource = externalDataPoints[2].distance_to(externalDataPoints[0])
	if k == 3:
		calcPointStartSource = externalDataPoints[0]
		calcPointEndSource = externalDataPoints[3]
		calcPointVectorSource = externalDataPoints[3].distance_to(externalDataPoints[0])
	if k == 4:
		calcPointStartSource = externalDataPoints[1]
		calcPointEndSource = externalDataPoints[2]
		calcPointVectorSource = externalDataPoints[2].distance_to(externalDataPoints[1])
	if k == 5:
		calcPointStartSource = externalDataPoints[1]
		calcPointEndSource = externalDataPoints[3]
		calcPointVectorSource = externalDataPoints[3].distance_to(externalDataPoints[1])
	if k == 6:
		calcPointStartSource = externalDataPoints[2]
		calcPointEndSource = externalDataPoints[3]
		calcPointVectorSource = externalDataPoints[3].distance_to(externalDataPoints[2])

	cosAlfaSource = (calcPointEndSource.x - calcPointStartSource.x)/calcPointVectorSource
	radiansSource = math.acos(cosAlfaSource)
	degreesSource = radiansSource * (180.0 / math.pi)

	rotationAngleDegrees = degrees - degreesSource

	print ("Start point x: %.2f y: %.2f" %(calcPointStart.x,calcPointStart.y)) 
	print ("Degrees %.2f" %(rotationAngleDegrees))
	

	cv2.imshow("output", image)
	cv2.imwrite("result.png", image)
	cv2.waitKey()
	cv2.destroyAllWindows()
else:
	print('No match ...')

