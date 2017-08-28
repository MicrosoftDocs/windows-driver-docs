---
title: The driver sample file list
author: windows-driver-content
description: The following source files are in the src\SPB\SpbAccelerometer folder and are used to build the SpbAccelerometer.sys and SpbAccelerometer.inf files.
ms.assetid: 48965F7F-1396-4E08-974B-3613684FAA6E
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# The driver sample file list


The following source files are in the src\\SPB\\SpbAccelerometer folder and are used to build the SpbAccelerometer.sys and SpbAccelerometer.inf files.

|                         |                                                                                                                                                                          |
|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| File                    | Description                                                                                                                                                              |
| AccelerometerDevice.cpp | Device-level methods to configure sensor, set properties, and query data.                                                                                                |
| Adxl345.h               | Device's register set definition and defines                                                                                                                             |
| ClientManager.cpp       | Implements the driver's client tracking logic, including arbitration of settable properties.                                                                             |
| Device.cpp              | WDF PnP event callbacks and helper methods                                                                                                                               |
| DllMain.cpp             | Driver's entry point and exported functions for providing COM support                                                                                                    |
| Driver.cpp              | WDF driver entry event callbacks and helper methods                                                                                                                      |
| Internal.h              | Common includes                                                                                                                                                          |
| makefile.inc            | Defines custom build actions. Includes the conversion of the .INX file into a .INF file.                                                                                 |
| Queue.cpp               | Implementation of IQueueCallbackDeviceIoControl.                                                                                                                         |
| ReportManager.cpp       | Maintains the driver's report interval.                                                                                                                                  |
| Request.idl             | Defines the request interface for communicating with the sensor device.                                                                                                  |
| SensorDdi.cpp           | Implementation of the sensor driver callback interface, ISensorDriver.                                                                                                   |
| SensorDevice.idl        | Defines the interface between the sensor DDI and the sensor device implementations.                                                                                      |
| sources                 | Lists source files and build options                                                                                                                                     |
| sources.dep             | Defines build dependencies                                                                                                                                               |
| SpbAccelerometer.asl    | Sample ASL file for a peripheral device node. It declares I2C and GPIO interrupt resources. Note that each macro specifies an ACPI path to describe direct dependencies. |
| SpbAccelerometer.ctl    | Declaration of driver's tracing GUID                                                                                                                                     |
| SpbAccelerometer.def    | Declaration of exported functions for providing COM support                                                                                                              |
| SpbAccelerometer.idl    | Driver's library interface file                                                                                                                                          |
| SpbAccelerometer.inx    | Describes the installation of the driver. The build process converts this into a .INF.                                                                                   |
| SpbAccelerometer.rc     | Resource file                                                                                                                                                            |
| SpbRequest.cpp          | Implementation of register-based device accesses via SPB.                                                                                                                |
| Trace.h                 | Sets up WPP tracing.                                                                                                                                                     |

 

## Related topics
[SpbAccelerometer driver sample](spbaccelerometer-driver-sample.md)  

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bsensors\sensors%5D:%20The%20driver%20sample%20file%20list%20%20RELEASE:%20%281/12/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


