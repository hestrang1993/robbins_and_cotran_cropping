import cv2
from variables import src_img_list, xi, xf, yi, yf, dst_img_root
# from display_image import display_image
from get_file_path_stem import get_file_path_stem
from create_safe_filename import clean_filename

len = len(src_img_list)
i = 0
for img_path in src_img_list:
    img = cv2.imread(img_path, cv2.IMREAD_COLOR)
    copy_img = img.copy()
    test_img_cropped = copy_img[yi:yf, xi:xf]
    filename = f"{get_file_path_stem(img_path)}.png"
    filename = clean_filename(filename)
    filename = filename.lower()
    filename = f"{dst_img_root}//{filename}"
    cv2.imwrite(filename, test_img_cropped)
    i += 1
    print(f"{(i/len)*100}% complete")
