# FPGA_Scope
In SMD-soldering there are a lot of very tiny parts with even smaller solder pads. If you really want to solder these parts, you need some sort of magnification. Commonly, a digital microscope is used here. The goal of this repo is to build something like this with an inexpensive FPGA-DevKit - specifically the CYC 1000 from Trenz Electronics

## Hardware
As stated, the main Chip/DevKit is the Cyclone 10 LP from Altera on the CYC1000.
In addition to this there is the daugtherboard that connects the camera to the FPGA aswell as an HDMI-port.

## Software
For using the scope there will be 2 possible ways
1. There is the obvious HDMI-Port poking out fron the dautherboard. This will be a HDMI-Source that streams the videofeed to any monitor you'd like.
2. In Addition to this you can connect the FPGA via USB to your PC and run the python file in ./software in order to use it "on the fly". I also would like to add some machine vision features like part detections or
   component-marker-enhancement. This will preferably run on the FPGA or on your local PC. I can't really tell you since this is all WIP...

## Further Links
- [CYC1000 Wiki](https://wiki.trenz-electronic.de/display/PD/TEI0003+Resources)
- [LeFlow](https://github.com/danielholanda/LeFlow)
- [DearPyGUI] (https://dearpygui.readthedocs.io/en/latest/)
