from comp_vision.centroidtracker import CentroidTracker
from comp_vision.trackableobject import TrackableObject
from comp_vision.emotionmodel import EmotionModel
from collections import OrderedDict
import configparser
import cv2
import imutils
import dlib
import numpy as np
import os


class FaceDet:
    def __init__(self):
        self.detector = dlib.get_frontal_face_detector()
        self.recog = EmotionModel(model_image='fer2013.h5')
        self.ctfaces = CentroidTracker(maxDisappeared=30, maxDistance=60)
        self.objects = OrderedDict()
        self.objectsE = OrderedDict()
        self.config = configparser.ConfigParser()
        self.config.read('settings.ini')
        self.brightness = int(self.config.get("Settings", "brightness"))
        self.contrast = float(self.config.get("Settings", "contrast"))
        self.med = 0
        self.writer = None
        self.H = None
        self.W = None 
        self.length = 0
        self.step = 0
        self.cap = None
        self.fps = 0
        self.not_cam = True


    def opnVideo(self,path):
        if path=='0':
            self.not_cam=False
        if self.not_cam:
            self.cap = cv2.VideoCapture(path)
            property_id = int(cv2.CAP_PROP_FRAME_COUNT) 
            self.length = int(cv2.VideoCapture.get(self.cap, property_id))
            self.step = int(self.length / 100) 
        else:
            self.cap = cv2.VideoCapture(0)
        return self.step

    def playVid(self):
        self.cap = cv2.VideoCapture('1.avi')
        while(self.cap.isOpened()):
            ret, frame = self.cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imshow('frame',frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()

    def convert_and_trim_bb(self, image, rect):
        startX = rect.left()
        startY = rect.top()
        endX = rect.right()
        endY = rect.bottom()
        
        startX = max(0, startX)
        startY = max(0, startY)
        endX = min(endX, image.shape[1])
        endY = min(endY, image.shape[0])
        
        w = endX - startX
        h = endY - startY
        
        return [startX, startY, w, h]

    #while True:
    def startCapture(self, path, stop):
        # Read the frame
        _, img = self.cap.read()
        if img is None and stop==False :
            return 'killed'
        elif stop==True:
            self.cap.release()
            cv2.destroyAllWindows()
            return 'done'
        sizes = []
        w = int(self.config.get("Settings", "width"))
        img = imutils.resize(img, width=w)
        img = cv2.convertScaleAbs(img, self.brightness, self.contrast)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        if self.W is None or self.H is None:
            (self.H, self.W) = img.shape[:2]
        
        if self.writer is None and path!=0:
            fourcc = cv2.VideoWriter_fourcc(*"MJPG")
            self.writer = cv2.VideoWriter(path +'.avi', fourcc, 30, (self.W, self.H), True)
            
        # Detect the faces
        results = self.detector(gray, 1)
        faces = [self.convert_and_trim_bb(img, r) for r in results]
        
        for i in range(len(faces)):
            sizes.append(((faces[i][2]*faces[i][3])**0.5)/2)
            faces[i][2]+=faces[i][0]
            faces[i][3]+=faces[i][1] 
        if sizes:
            self.med = int(np.mean(sizes))
        
        self.objects = self.ctfaces.update(faces,img,self.med)

        for face in faces:
            emotion = self.recog.predict_emotion(face, gray)
            cv2.putText(img, emotion, (face[0], face[1]-10),
                cv2.FONT_HERSHEY_PLAIN, 1.5, (255, 0, 0), 2)


        for (objectID, centroid) in self.objects.items():
            cv2.circle(img, (centroid[0], centroid[1]), 4, (0, 255, 0), -1)

        text = "Objects: {}".format(len(self.objects))
        cv2.putText(img, text, (10, self.H - 150),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        if self.writer is not None:
           self.writer.write(img)

        cv2.imshow(path, img)
        self.fps += 1
        if self.fps==self.length:
           return 'done'
                 
        #Stop if escape key is pressed
        
        k = cv2.waitKey(30) & 0xff
        if k==27:
            self.cap.release()
            cv2.destroyAllWindows()
            if self.writer is not None:
                self.writer.release()
            return 'killed'
        return 'ok'
