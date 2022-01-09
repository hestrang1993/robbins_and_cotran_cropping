from create_file_path_list import create_file_path_list

top_left = (187, 224)
top_right = (2313, 224)
bottom_left = (187, 3117)
bottom_right = (2313, 3117)

xi = 0
w = 2550
xf = xi + w
# yi = 224
yi = 200
h = 3000
yf = yi + h

window_width = 3840 // 2
window_height = 2160 // 2

display_ratio = window_height/(h - yi)
display_width = int(display_ratio * w)
display_height = window_height
display_size = (display_width, display_height)

src_img_root = "C:\\Users\\harri\\OneDrive - University of South Florida\\robbins_and_cotran_atlas"

src_img_list = create_file_path_list(src_img_root)

dst_img_root = "C:\\Users\\harri\\PycharmProjects\\robbins_and_cotran_cropping\\img"

dst_img_list = create_file_path_list(dst_img_root)

threshold_img_root = "C:\\Users\\harri\\PycharmProjects\\robbins_and_cotran_cropping\\threshold"
