import cv2
import time
import numpy as np
import handtrackmod as ht
import math 

wcam,hcam=640,480



cap=cv2.VideoCapture(0)
cap.set(3,wcam)
cap.set(4,hcam)
pTime=0

detector=ht.handDetector()



while True:
    ret , img =cap.read()
    width=int(cap.get(3))
    height=int(cap.get(4))
    img=detector.findHands(img)
    lmlist=detector.findPosition(img,draw=False)
    if len(lmlist)!=0:
        #aprint(lmlist[8])
        px,py=lmlist[8][1],lmlist[8][2]
        cx,cy=height//2,width//2

        u=[px,py]
        v=[cx,cy]
    
        dotp=(px*cx)+(py*cy)
        #print(dotp)
        modu=math.sqrt(px**2 + py**2)
        modv=math.sqrt(cx**2 + cy**2)
        #print(modu,modv)
        angle=math.acos(dotp/(modu*modv))
        #print(angle)
        degre=math.degrees(angle)
        print(degre)

        

    img=cv2.circle(img,(width//2,height//2),10,(0,255,0),-1)



    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,(255, 0, 255), 3)
    
    cv2.imshow("frame",img)
    if cv2.waitKey(1)==ord('a'):
        break

cap.release()
cv2.destroyAllWindows()