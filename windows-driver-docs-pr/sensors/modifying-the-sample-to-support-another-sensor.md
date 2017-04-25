---
title: Modify the sample to support another sensor
author: windows-driver-content
description: Modify the sample to support another sensor
ms.assetid: E759E022-C1E6-4403-B3DC-82A269E04B93
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bsensors\sensors%5D:%20Modify%20the%20sample%20to%20support%20another%20sensor%20%20RELEASE:%20%281/12/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


