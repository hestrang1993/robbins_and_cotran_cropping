import cv2
# from variables import dst_img_list
from variables import display_size
from display_image import display_image

# test_img_path = dst_img_list[-23]
test_img_path = "C:\\Users\\harri\\PycharmProjects\\robbins_and_cotran_cropping\\img\\klatt_2014_" \
                "-_robbins_and_cotran_atlas_of_pathology_040.png"

test_img = cv2.imread(test_img_path, cv2.IMREAD_COLOR)

grayscale_img = cv2.cvtColor(test_img, cv2.COLOR_BGR2GRAY)

# threshold_img = cv2.adaptiveThreshold(grayscale_img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
ret, threshold_img = cv2.threshold(grayscale_img, 254, 255, cv2.THRESH_BINARY)

# display_image(threshold_img)

contours, hierarchy = cv2.findContours(threshold_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

print(f"Number of Contours: {str(len(contours))}")

for contour in contours:
    rect = cv2.boundingRect(contour)
    print(cv2.contourArea(contour))
cv2.drawContours(test_img, contours, -1, (0, 255, 0), 10)
test_img = cv2.resize(test_img, display_size)

display_image(test_img)
