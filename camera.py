import time
import cv2
import numpy as np
from imutils.video import WebcamVideoStream
import PoseModule as pm
from PoseModule import PoseDetector

detector = PoseDetector()

class VideoCamera(object):
    
    def __init__(self):
        self.stream=WebcamVideoStream(src=0).start()

    def __del__(self):
        self.stream.stop()
    
    def get_frame(self,pTime,l_title,amin,amax,count,dir):
        if l_title == 'Push Ups':
            # Capture the video frame by frame
            image=self.stream.read()
            frame = cv2.resize(image, (1280, 720))
            frame = detector.findPose(frame, draw = False)
            lmList = detector.findPosition(frame, draw = False)
            angle = detector.findAngle(frame,12,14,16)

            if(angle < amin):
                amin = angle

            if(angle > amax):
                amax = angle
            
            #Interpolate angle
            per = np.interp(angle, (70, 160), (0, 100))
            bar = np.interp(angle, (70, 160), (620, 150))

            print(angle, per)
            #Count
            if per == 100:
                if dir == 0:
                    if count != 0:
                        count += 0.5
                    dir = 1
            if per == 0:
                if dir == 1:
                    count += 0.5
                    dir = 0

            #Draw
            cv2.rectangle(frame, (0, 630), (120, 720), (0, 255, 0), cv2.FILLED)
            cv2.putText(frame, f'{int(count)}', (40, 700), cv2.FONT_HERSHEY_PLAIN, 4, (0, 0, 255), 2)

            cv2.rectangle(frame, (1200, 150), (1220, 620), (0, 255, 0), 2)
            cv2.rectangle(frame, (1200, int(bar)), (1220, 620), (0, 0, 255), cv2.FILLED)
            cv2.putText(frame, f'{int(per)}%', (1180, 100), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)

            # fps calc
            cTime = time.time()
            fps = 1 / (cTime - pTime)
            pTime = cTime
            # fps show
            cv2.putText(frame, f'{int(fps)}fps', (40, 50), cv2.FONT_HERSHEY_PLAIN, 1.5, (255, 0, 0), 2)
            #encode
            ret,jpeg=cv2.imencode('.jpg',frame)
            data=[]
            data.append(jpeg.tobytes())
            return data,pTime,l_title,amin,amax,count,dir


        elif l_title == 'Squats':
            image=self.stream.read()
            frame = cv2.resize(image, (1280, 720))
            frame = detector.findPose(frame, draw = False)
            lmList = detector.findPosition(frame, draw = False)
            angle = detector.findAngle(frame,24,26,28)

            if(angle < amin):
                amin = angle

            if(angle > amax):
                amax = angle

            #Interpolate angle
            per = np.interp(angle, (40, 165), (0, 100))
            bar = np.interp(angle, (40, 165), (620, 150))

            print(angle, per)
            #Count
            if per == 100:
                if dir == 0:
                    if count != 0:
                        count += 0.5
                    dir = 1
            if per == 0:
                if dir == 1:
                    count += 0.5
                    dir = 0


            #Draw
            cv2.rectangle(frame, (0, 630), (120, 720), (0, 255, 0), cv2.FILLED)
            cv2.putText(frame, f'{int(count)}', (40, 700), cv2.FONT_HERSHEY_PLAIN, 4, (0, 0, 255), 2)

            cv2.rectangle(frame, (1200, 150), (1220, 620), (0, 255, 0), 2)
            cv2.rectangle(frame, (1200, int(bar)), (1220, 620), (0, 0, 255), cv2.FILLED)
            cv2.putText(frame, f'{int(per)}% ', (1180, 100), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)

            # fps calc
            cTime = time.time()
            fps = 1 / (cTime - pTime)
            pTime = cTime
            # fps show
            cv2.putText(frame, f'{int(fps)}fps', (40, 50), cv2.FONT_HERSHEY_PLAIN, 1.5, (255, 0, 0), 2)
            #encode
            ret,jpeg=cv2.imencode('.jpg',frame)
            data=[]
            data.append(jpeg.tobytes())
            return data,pTime,l_title,amin,amax,count,dir
            

        else:
            image=self.stream.read()
            frame = detector.findPose(image)
            lmList = detector.findPosition(frame)
            # fps calc
            cTime = time.time()
            fps = 1 / (cTime - pTime)
            pTime = cTime
            # fps show
            cv2.putText(frame, str(int(fps)), (50, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
            ret,jpeg=cv2.imencode('.jpg',frame)
            data=[]
            data.append(jpeg.tobytes())
            return data,pTime,l_title,amin,amax,count,dir
                

