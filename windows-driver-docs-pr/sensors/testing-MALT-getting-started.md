---
title: Getting Started with MALT
description: This topic defines how to upload firmware to the MALT and how to calibrate it using Sensor Explorer.
ms.date: 06/16/2021
ms.localizationpriority: medium
---

# Getting Started with MALT

This topic defines how to upload firmware to the MALT as well as how to calibrate the sensors using Sensor Explorer. We recommended that the PC controlling the microcontroller is also the system or device under test (SUT/DUT).  

## Acquiring the Necessary Files

1. Create a folder named ```MALT``` on your computer's C drive. the filepath should be ```C:\MALT```. We will place all of the necessary files and cloned repositories here.

1. Clone the [busiotools repository](https://github.com/microsoft/busiotools) to your ```MALT``` folder. The filepath should be ```C:\MALT\busiotools```.

2. Clone the [SerialCommand](https://github.com/kroimon/Arduino-SerialCommand) and [SoftI2CMaster](https://github.com/sastorer/SoftI2CMaster) repositories to your ```MALT``` folder. The filepaths should be ```C:\MALT\Arduino-SerialCommand``` and ```C:\MALT\SoftI2CMaster``` respectively.


## Updating the MALT Firmware

The MALT is run by an Arduino which requres firmware to set up and interact with the sensors on the MALT board.

1. Acquire and setup the Arduino command line interface.
    1. Download the latest version of the [arduino-cli](https://arduino.github.io/arduino-cli/latest/installation/#download).
    2. If not done already, add the arduino-cli to your [PATH variable](/windows-server/administration/windows-commands/path).
    3. Run the following from a command prompt:

        ```console
        arduino-cli config init
        arduino-cli core update-index
        ```

2. Add necessary libraries from the Arduino library manager by running the following from a command prompt:

    ```console
    arduino-cli lib install MatrixMath
    arduino-cli lib install AsyncDelay
    ```

3. Identify the COM port assigned to the Arduino by running the following from a command prompt:

    ```console
    arduino-cli board list
    ```

4. Upload the firmware to the Arduino by running the following from a command prompt, and replacing the X in COMX to the COM port number identified in the previous step:

    ```console
    arduino-cli compile --fqbn arduino:avr:mega --port COMX --export-binaries --upload --library C:\MALT\Arduino-SerialCommand --library C:\MALT\SoftI2CMaster C:\MALT\busiotools\sensors\tools\MALT\Code\malt
    ```