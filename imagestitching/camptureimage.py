import cv2


def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():  # Check if the web cam is opened correctly
        print("failed to open cam")
        return -1
    else:
        print('webcam open')

    for i in range(6000,10 ** 10):
        success, cv_frame = cap.read()
        if not success:
            print('failed to capture frame on iter {}'.format(i))
            break
        cv2.imshow('click t to save image and q to finish', cv_frame)
        k = cv2.waitKey(1)
        if k == ord('q'):
            print('q was pressed - finishing...')
            break
        elif k == ord('t'):
            print('t was pressed - saving image {}...'.format(i))
            image_path = 'Left_{}.jpg'.format(i)  # i recommend a folder and not to save locally to avoid the mess
            cv2.imwrite(image_path, cv_frame)

    cap.release()
    cv2.destroyAllWindows()
    return


if __name__ == '__main__':
    main()

