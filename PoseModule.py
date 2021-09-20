import math
import cv2
import mediapipe as mp
import time


class PoseDetector():

    def __init__(self, mode = False, upBody = True, smooth = True, detectionCon = 0.5, trackingCon = 0.5):

        self.mode = mode
        self.upBody = upBody
        self.smooth = smooth
        self.detectionCon = detectionCon
        self.trackingCon = trackingCon

        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(self.mode, self.upBody, self.smooth,self.detectionCon, self.trackingCon)
        self.mpDraw = mp.solutions.drawing_utils

    def findPose(self, frame, draw = True):
        #conversion to fit model
        imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # using model for landmarks
        self.results = self.pose.process(imgRGB)

        if(self.results.pose_landmarks):
             if draw:
                 self.mpDraw.draw_landmarks(frame, self.results.pose_landmarks, self.mpPose.POSE_CONNECTIONS)
        return frame

    def findPosition(self, frame, draw = True):
        self.lmList = []
        if (self.results.pose_landmarks):
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h, w, c = frame.shape
                #print(id, lm)
                cx, cy = int(w * lm.x), int(h * lm.y)
                self.lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(frame, (cx, cy), 5, (255, 0, 0), cv2.FILLED)
        return self.lmList

    def findAngle(self, frame, a, b, c, draw = True):
        #landmarks
        a1, a2 = self.lmList[a][1:]
        b1, b2 = self.lmList[b][1:]
        c1, c2 = self.lmList[c][1:]

        #angle
        angle = math.degrees(math.atan2(c1 - b1, c2 - b2) - math.atan2(a1 - b1, a2 - b2))
        if angle < 0:
            angle = angle*(-1)

        #draw
        if draw:
            cv2.line(frame, (a1, a2), (b1, b2), (255, 255, 255), 3)
            cv2.line(frame, (c1, c2), (b1, b2), (255, 255, 255), 3)
            cv2.circle(frame, (a1, a2), 5, (0, 0, 255), cv2.FILLED)
            cv2.circle(frame, (a1,a2), 10, (0, 0, 255), 2)
            cv2.circle(frame, (b1, b2), 5, (0, 0, 255), cv2.FILLED)
            cv2.circle(frame, (b1, b2), 10, (0, 0, 255), 2)
            cv2.circle(frame, (c1, c2), 5, (0, 0, 255), cv2.FILLED)
            cv2.circle(frame, (c1, c2), 10, (0, 0, 255), 2)
            cv2.putText(frame, str(int(angle)), (b1 - 50, b2 - 50), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)

        return angle

def main():
    # define a video capture object
    #vid = cv2.VideoCapture('video/1.mp4')
    vid = cv2.VideoCapture(0)
    pTime = 0
    detector  = PoseDetector()
    while (True):
        # Capture the video frame
        # by frame
        ret, frame = vid.read()
        frame = detector.findPose(frame)
        lmList = detector.findPosition(frame)
        #print(lmList)
        # fps calc
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        # fps show
        cv2.putText(frame, str(int(fps)), (50, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

        # Display the resulting frame
        cv2.imshow('Pose', frame)
        # the 'q' button is set as the
        # quitting button you may use any
        # desired button of your choice
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # After the loop release the cap object
    vid.release()
    # Destroy all the windows
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()