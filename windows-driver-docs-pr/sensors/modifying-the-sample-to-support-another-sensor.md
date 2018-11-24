---
title: Modify the sample to support another sensor
description: Modify the sample to support another sensor
ms.assetid: E759E022-C1E6-4403-B3DC-82A269E04B93
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Modify the sample to support another sensor


The SpbAccelerometer sample shows how to write a driver for the ADXL345 accelerometer. If your driver supports a single sensor (that’s not an accelerometer), you'll revise, or replace, the following files and functionality:

| File                    | Revisions                                                                                                                                                                                                                                                                                                                                                                             |
|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SpbAccelerometer.inx    | Rename the file. Update the device-name strings to reflect the name of your device. (Search and replace instances of “SPB Accelerometer” and “SpbAccelerometer”.) Make sure that hardware identifier in the INF file contains the “ACPI” string.                                                                                                                                      |
| SpbAccelerometer.asl    | Rename the file. Update the \_CRS section so that it specifies the I2C and GPIO resources required by your device.                                                                                                                                                                                                                                                                    |
| Adxl345.h               | Rename the file. If your device is similar to the ADXL345 and supports a set of registers and corresponding read and write operations, modify this file so that it maps to the registers, and operations, supported by your device. If your device does not support registers or read/write operations, remove this file.                                                             |
| AccelerometerDevice.h   | Rename the file. Replace the private methods that correspond to specific ADXL345 functionality with methods that correspond to functionality on your device. For example, if your device does not use registers and interrupts, replace the ReadRegister, WriterRegister, and ConnectInterrupt methods. Replace the private members that no longer reflect your device functionality. |
| AccelerometerDevice.cpp | Rename the file. Remove the methods you’d pulled from the header file and insert the definitions for the new methods that correspond to your device’s functionality.                                                                                                                                                                                                                  |

 

 

 




