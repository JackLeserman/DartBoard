import cv2

def blue_mask(filename):
    ## convert to hsv
    img = cv2.imread(filename)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    ## mask of green (36,25,25) ~ (86, 255,255)
    # mask = cv2.inRange(hsv, (36, 25, 25), (86, 255,255))
    mask = cv2.inRange(hsv, (87, 44, 97), (109, 255,255))

    ## slice the green
    imask = mask>0
    green = np.zeros_like(img, np.uint8)
    green[imask] = img[imask]

    ## save 
    cv2.imwrite("blue_mask.png", green)

def getSSIM():
    imageA = cv2.imread('alpha.png')
    imageB = cv2.imread('beta.png')
    grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
    grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
    (score, diff) = ssim(grayA, grayB, full=True)
    diff = (diff * 255).astype("uint8")
    return score

def getSSIM2(imageA, imageB):
    grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
    grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
    (score, diff) = ssim(grayA, grayB, full=True)
    diff = (diff * 255).astype("uint8")
    return score

def diffy():
        blur = (5,5)
        grey1 = cv2.imread("p1.png",0)
        grey2 = cv2.imread("p2.png",0)
        grey2 = cv2.blur(grey2,blur)
        grey1 = cv2.blur(grey1,blur)
        #normalize
        grey1 = cv2.equalizeHist(grey1)
        grey2 = cv2.equalizeHist(grey2)
        clahe = cv2.createCLAHE(20,(10,10))
        #clahe
        grey1 = clahe.apply(grey1)
        grey2 = clahe.apply(grey2)
        #diff
        diff = cv2.subtract(grey2,grey1) + cv2.subtract(grey1,grey2)
        ret2,dif_thred = cv2.threshold(diff,50,255,cv2.THRESH_BINARY)
        cv2.imshow("Difference", dif_thred)
        cv2.waitKey(0)

def getDifferenceLayer():
    #open images
    imageA = cv2.imread("p1.png")
    imageB = cv2.imread("p2.png")
    #convert to grayscale
    grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
    grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
    print(grayA.shape)
    print(grayB.shape)

    #find difference
    diff = cv2.subtract(grayA,grayB)
    #BnW mask
    ret, mask = cv2.threshold(diff, 0, 255,cv2.THRESH_BINARY_INV |cv2.THRESH_OTSU)

    cv2.imshow("Difference", mask)
    cv2.waitKey(0)

#diffy()
getDifferenceLayer()