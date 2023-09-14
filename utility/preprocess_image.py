import cv2

def gray_scale(image):
  image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  return image

def hist_equal(image):
  image = cv2.equalizeHist(image)
  return image

def preprocessing(image):
  image = gray_scale(image)
  image = hist_equal(image)
  image = image/255
  return image


