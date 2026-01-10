# FPGA_Scope
In SMD-soldering there are a lot of very tiny parts with even smaller solder pads. If you really want to solder these parts, you need some sort of magnification. Commonly, a digital microscope is used here. The goal of this repo is to build something like this with as affordable as possible - specifically the CYC1000 from Trenz Electronics, and an OminVision OV5640 Camera.

## Hardware
As stated, the main Chip/DevKit is the Cyclone 10 LP from Altera on the CYC1000.
For this DevKit, I will be designing a daugtherboard which allows the connection of the OV5640 to the FPGA and also adds an HDMI-Port for streaming the Data to a Display.

## Software
For using the scope there will be two possible ways:
1. There is the obvious HDMI-Port poking out from the dautherboard. This will be a HDMI-Source that streams the videofeed to any monitor you'd like.
2. In Addition to this you can connect the FPGA via USB to your PC and run the python file in ./software in order to use it "on the fly". I also would like to add some machine vision features like part detections or
   component-marker-enhancement. This will preferably run on the FPGA or on your local PC. I can't really tell you since this is all WIP...

## Further Links
- [CYC1000 Wiki](https://wiki.trenz-electronic.de/display/PD/TEI0003+Resources)
- [LeFlow](https://github.com/danielholanda/LeFlow)
- [DearPyGUI](https://dearpygui.readthedocs.io/en/latest/)
