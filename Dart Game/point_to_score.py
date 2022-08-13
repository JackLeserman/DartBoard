import math
center = (322, 241)

#returns distance between two points

def cart_to_polar(point):
    distance = math.dist(center, point)
    angle = math.atan2((center[1] - point[1]),(center[0] - point[0]))
    angle = abs(math.degrees(angle) - 180)
    #print(angle)
    #print(distance, angle)
    return(distance, angle)

def angle_to_score(angle):
    if((351 < angle and angle < 360) or (angle < 9)):
        score = 6
        return score
    if(9 <= angle and angle < 27):
        score = 13
        return score
    if(27 <= angle and angle < 45):
        score = 4
        return score
    if(45 <= angle and angle < 63):
        score = 18
        return score
    if(63 <= angle and angle < 81):
        score = 1
        return score
    if(81 <= angle and angle < 99):
        score = 20
        return score
    if(99 <= angle and angle < 117):
        score = 5
        return score
    if(117 <= angle and angle < 135):
        score = 12
        return score
    if(135 <= angle and angle < 153):
        score = 9
        return score
    if(153 <= angle and angle < 171):
        score = 14
        return score
    if(171 <= angle and angle < 189):
        score = 11
        return score
    if(189 <= angle and angle < 207):
        score = 8
        return score
    if(207 <= angle and angle < 225):
        score = 16
        return score
    if(225 <= angle and angle < 243):
        score = 7
        return score
    if(243 <= angle and angle < 261):
        score = 19
        return score
    if(261 <= angle and angle < 279):
        score = 3
        return score
    if(279 <= angle and angle < 297):
        score = 17
        return score
    if(297 <= angle and angle < 315):
        score = 2
        return score
    if(315 <= angle and angle < 333):
        score = 15
        return score
    if(333 <= angle and angle < 351):
        score = 10
        return score
    return score

#takes in a point, outputs (ring, score)
def get_score(point):

    polar = cart_to_polar(point)
    print(polar)
    dist = polar[0]
    print(dist)
    wedge = angle_to_score(polar[1])
    
    if(0<=dist<=7):
        ring = "be_50"
        score =  50
        return(ring, score)
    
    if(7<dist<=18):
        ring = "be_25"
        score = 25
        return(ring, score)

    if(10<dist<=101):
        ring = "single_1"
        score = wedge
        return(ring, score)
    
    if(101<dist<=111):
        ring = "double"
        score = wedge * 2
        return(ring, score)
    if(111<dist<=168):
        ring = "single_2"
        score = wedge
        return(ring, score)
    
    if(168<dist<=179):
        ring = "triple"
        score = wedge * 3
        return(ring, score)
    
    return("miss", 0)

def score_to_text(score):
    print("score = " + score[1])   
    print("ring = " + score[0]) 
    print("")


    
    