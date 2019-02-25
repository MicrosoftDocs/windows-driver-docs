---
title: The driver sample file list
description: The following source files are in the src\SPB\SpbAccelerometer folder and are used to build the SpbAccelerometer.sys and SpbAccelerometer.inf files.
ms.assetid: 48965F7F-1396-4E08-974B-3613684FAA6E
ms.date: 04/20/2017
ms.localizationpriority: medium
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



