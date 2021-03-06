import cv2

class CvAnnotator:
    def __init__(self):
        self.window_name = 'CvAnnotator'
        cv2.namedWindow(self.window_name)
        
    def __del__(self):
        cv2.destroyAllWindows()
        
    def show(self, image, rect, text):
        image_with_anot = cv2.rectangle(image, rect, (0,255,0), 2)
        image_with_anot = cv2.putText(image_with_anot,
                                      text, 
                                      (rect[0] + 4, rect[1] + 22),
                                      cv2.FONT_HERSHEY_PLAIN,
                                      1,
                                      (0,255,0),
                                      2,
                                      cv2.LINE_AA)
        cv2.imshow(self.window_name, image_with_anot)
        cv2.waitKey(1)
        
    def show_multiple(self, image, rects, texts):
        for i in range(len(rects)):
            rect = rects[i]
            text = texts[i]
            
            image_with_anot = cv2.rectangle(image, rect, (0,255,0), 2)
            image_with_anot = cv2.putText(image_with_anot,
                                          text, 
                                          (rect[0] + 4, rect[1] + 22),
                                          cv2.FONT_HERSHEY_PLAIN,
                                          1,
                                          (0,255,0),
                                          2,
                                          cv2.LINE_AA)
        
        if len(rects) == 0:
            image_with_anot = cv2.putText(image, 'NO OBJECT', (8, 24),
                                          cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2, cv2.LINE_AA)
        cv2.imshow(self.window_name, image_with_anot)
        cv2.waitKey(1)