import cv2 as cv
import numpy as np



hayStack_img = cv.imread('1.png', cv.IMREAD_REDUCED_COLOR_2)
needle_img = cv.imread('test_sandstone.png', cv.IMREAD_REDUCED_COLOR_2)

result = cv.matchTemplate(hayStack_img,needle_img,cv.TM_SQDIFF_NORMED)

threshold = 0.106
locations = np.where(result <= threshold)
locations = list(zip(*locations[::-1]))



if locations:
    print('found needle')
    
    needle_w = needle_img.shape[1]
    needle_h = needle_img.shape[0]
    line_color = (0,255,0)
    line_type = cv.LINE_4
    
    
    
    for loc in locations:
        top_left = loc
        bottom_right = (top_left[0] + needle_w, top_left[1] + needle_h)
        
        cv.rectangle(hayStack_img,top_left,bottom_right,line_color,line_type)
        
    cv.imshow('Matches',hayStack_img)
    cv.waitKey()
    
    
else:
    print('not needle found')