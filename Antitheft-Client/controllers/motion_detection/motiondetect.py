from motionvid import sendfile
import picamera
import picamera.array
import time
import os
threshold = 20   # How Much pixel changes
sensitivity = 100 # How many pixels change

def takeMotionImage(width, height):
    with picamera.PiCamera() as camera:
        time.sleep(1)
        camera.resolution = (width, height)
        with picamera.array.PiRGBArray(camera) as stream:
            camera.exposure_mode = 'auto'
            camera.awb_mode = 'auto'
            camera.capture(stream, format='rgb')
            return stream.array

def scanMotion(width, height):
    motionFound = False
    data1 = takeMotionImage(width, height)
    while not motionFound:
        data2 = takeMotionImage(width, height)
        diffCount = 0L;
        for w in range(0, width):
            for h in range(0, height):
                # get the diff of the pixel. Conversion to int
                # is required to avoid unsigned short overflow.
                diff = abs(int(data1[h][w][1]) - int(data2[h][w][1]))
                if  diff > threshold:
                    diffCount += 1
            if diffCount > sensitivity:
                break;
        if diffCount > sensitivity:
            motionFound = True
        else:
            data2 = data1
    return motionFound

def motionDetection():
    count=1
    while True:
        if scanMotion(512, 512):
            print "Motion detected"
            os.system("raspivid -o motiondetectedvideos/video"+str(count)+".h264 -t 10000")
            sendfile("/home/pi/camera_module/motion_detection/motiondetectedvideos")
            count = count+1
if __name__ == '__main__':
    try:
        motionDetection()
    finally:
        print "Exiting Program"

