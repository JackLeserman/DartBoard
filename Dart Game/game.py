import  cv2
def takePic(): 
    cam = cv2.VideoCapture(1)
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, 3840)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 2448)
    cv2.namedWindow("test")
    img_counter = 0
    ret, frame = cam.read()
    frame = cv2.rotate(frame,cv2.ROTATE_180)
    cv2.imwrite('p1.png', frame)

def take2Pics(): 
    cam = cv2.VideoCapture(1)
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, 3840)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 2448)
    ret, frame = cam.read()
    frame = cv2.rotate(frame,cv2.ROTATE_180)
    cv2.imwrite('p1.png', frame) 
    cv2.waitKey(10000)   
    ret, frame = cam.read()
    frame = cv2.rotate(frame,cv2.ROTATE_180)
    cv2.imwrite('p2.png', frame)  


def takePic2(str): 
    cam = cv2.VideoCapture(1)
    #cam.set(cv2.CAP_PROP_FRAME_WIDTH, 3840) #REMOVE??
    #cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 2448) #REMOVE??
    cv2.namedWindow("test")
    img_counter = 0
    ret, frame = cam.read()
    frame = cv2.rotate(frame,cv2.ROTATE_180)
    cv2.imwrite(str, frame)

def live_blue():
    input = cv2.VideoCapture(1)   
    while True:   
        ret, frame = input.read()   
       
        if ret:   
            frame = cv2.rotate(frame,cv2.ROTATE_180)
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            mask_all = cv2.inRange(hsv, (87, 44, 97), (109, 255,255))
            cv2.imshow("video output", mask_all)

        if cv2.waitKey(1) & 0xFF == ord( 'x' ):   
            break

takePic()