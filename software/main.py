import array
import dearpygui.dearpygui as gui
import cv2
import numpy as np
import serial
import serial.tools.list_ports

# Standard baud rates (widely supported)
STANDARD_BAUDS = [1200, 2400, 4800, 9600, 19200, 38400, 57600, 115200]
# High-speed rates (platform/hardware dependent)
HIGH_SPEED_BAUDS = [230400, 460800, 921600, 1000000, 1500000, 2000000]

cam = cv2.VideoCapture(0)
video_data = array.array('f')

frame_width = 100
frame_height = 100

serial_baud = None
serial_port = None


def test_baud_rate(port, baudrate):
    """Test if baud rate works with device"""
    try:
        test_ser = serial.Serial(port, baudrate, timeout=1)
        
        # Send test command
        test_ser.write(b'AT\r\n')
        response = test_ser.readline()
        
        test_ser.close()
        
        return len(response) > 0
    except:
        return False

def serial_find_ports():
    available_ports = []
    for port in serial.tools.list_ports.comports():
        available_ports.append(port)

    return available_ports

def serial_find_optimal_baudrate(port, test_bauds=None):
    #Find highest working baud rate
    if test_bauds is None:
        test_bauds = STANDARD_BAUDS + HIGH_SPEED_BAUDS
    
    working_bauds = []
    
    for baud in sorted(test_bauds):
        if test_baud_rate(port, baud):
            working_bauds.append(baud)
    
    return max(working_bauds) if working_bauds else None


def _update_video():
    ###----OpenCV-based Demo with PC-Camera----###
    global video_data
    global frame_width
    global frame_height

    # Capture one frame
    ret, frame = cam.read()

    frame_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

    if ret:
        data = np.flip(frame, 2) #convert from BGR to RGB
        data = data.ravel() #flatten the incoming camera data into a 1d array
        data = np.asarray(data, dtype='f')

        video_data = np.true_divide(data, 255.0)
    else:
        print("Failed to capture image!")

gui.create_context()

_update_video()

with gui.texture_registry():
   gui.add_raw_texture(width=frame_width, height=frame_height, default_value=video_data, format=gui.mvFormat_Float_rgb, tag="video_feed", label="video")

#the viewport is the "window" which we create here
gui.create_viewport(title='FPGA_Scope', width=frame_width+100, height=frame_height+100)
gui.setup_dearpygui()

#create the main window of the application
with gui.window(tag="Primary Window"):
    
    ###----menu bar----###
    with gui.menu_bar(label="top_menu"):
        #ToDo: Add settings for the gui itself (dark-mode, light-mode, ...)
        # with gui.menu(label="Settings"):
        #     ...
        with gui.menu(label="Connection"):
            gui.add_menu_item(label="Start Connection...")

            with gui.menu(label="Port:"):
                for item in serial_find_ports():
                    gui.add_menu_item(label=item)
            with gui.menu(label="Baudrate:"):

                gui.add_menu_item(label="Auto")
                for item in STANDARD_BAUDS + HIGH_SPEED_BAUDS:
                    gui.add_menu_item(label= str(item))

        with gui.menu(label="Machine-Vision"):
            gui.add_menu_item(label="local models:")
            gui.add_menu_item(label="FPGA models:")

        gui.add_menu_item(label="About")
        


    ###----actual video feed----###
    gui.add_image("video_feed")


gui.show_viewport()
#set the window as the actual primary window
gui.set_primary_window("Primary Window", True)

#render loop
while gui.is_dearpygui_running():
    # insert here any code you would like to run in the render loop
    # you can manually stop by using stop_dearpygui()

    #get new data from the camera and update the data for the gui accordingly
    _update_video()
    gui.set_value("video_feed", video_data)
    gui.render_dearpygui_frame()


#cleanup
gui.destroy_context()
cam.release()