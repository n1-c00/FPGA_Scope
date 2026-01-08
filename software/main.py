import dearpygui.dearpygui as gui
import serial
import serial.tools.list_ports

# Standard baud rates (widely supported)
STANDARD_BAUDS = [1200, 2400, 4800, 9600, 19200, 38400, 57600, 115200]
# High-speed rates (platform/hardware dependent)
HIGH_SPEED_BAUDS = [230400, 460800, 921600, 1000000, 1500000, 2000000]

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

###----callback functions----###


gui.create_context()
#the viewport is the "window" which we create here
gui.create_viewport(title='FPGA_Scope', width=600, height=500)
gui.setup_dearpygui()
#create the main window of the application
with gui.window(tag="Primary Window", width=600, height=500):
    with gui.menu(label="Connection"):
        gui.add_menu_item(label="Start Connection...")

        with gui.menu(label="Port"):
            for item in serial_find_ports():
                gui.add_menu_item(label=item)
        
        with gui.menu(label="Baudrate"):
            gui.add_menu_item(label="Auto")
            for item in STANDARD_BAUDS + HIGH_SPEED_BAUDS:
                gui.add_menu_item(label= str(item))



        


gui.show_viewport()
#set the window as the actual primary window
gui.set_primary_window("Primary Window", True)

#render loop
while gui.is_dearpygui_running():
    # insert here any code you would like to run in the render loop
    # you can manually stop by using stop_dearpygui()
    gui.render_dearpygui_frame()


#cleanup
gui.destroy_context()