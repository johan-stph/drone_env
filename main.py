import threading

from djitellopy import Tello
import cv2



def tello_init():
    drone = Tello()
    drone.connect()
    threading.Thread(target=video_stream, args=[drone])
    return drone

def video_stream(drone: Tello):
    print("Video stram started")

    while True:
        img  = drone.get_frame_read().frame
        cv2.imshow("test", img)
        cv2.waitKey(1)

def tello_test():
    drone = tello_init()

    try:
        while True:
            user_input = read_input()
            if user_input == "end":
                end_drone(drone)
                break

            print(drone.send_command_with_return(user_input))

    except KeyboardInterrupt:
        end_drone(drone)
        raise KeyboardInterrupt


def end_drone(drone: Tello):
    drone.land()
    drone.streamoff()




def main():
    tello_test()


def read_input():
    return input("Enter your command? ")






if __name__ == '__main__':
    main()