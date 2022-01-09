import cv2
from variables import display_size

def display_image(img, title=""):
    """
    display_image display an image with a OpenCV window, and close the window if the escape key is pressed.

    Parameters
    ----------
    img : numpy.ndarray
        The input image.
    title : str
        The title of the display window.

    Returns
    -------
    None
    """
    cv2.imshow(title, img)
    cv2.resizeWindow(title, display_size[0], display_size[1])
    while True:
        k = cv2.waitKey(0) & 0xFF
        print(k)
        if k == 27:
            cv2.destroyAllWindows()
            break
