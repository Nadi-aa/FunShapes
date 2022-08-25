import cv2
from google.colab.patches import cv2_imshow #use this if you are using colab

im = cv2.imread("/content/chihiro.jpg")  #path
cv2_imshow(im)

gray_im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
in_im = 255 - gray_im
blur_im = cv2.GaussianBlur(in_im, (21,21), 0)
in_blur = 255 - blur_im

line_art = cv2.divide(gray_im, in_blur, scale=256.0)

cv2_imshow(line_art) 
