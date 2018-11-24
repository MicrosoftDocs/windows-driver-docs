---
title: Geolocation sample driver file list
description: The source file of the geolocation driver sample includes the following categories of files.
ms.assetid: 8A9A1102-921B-40FF-94F2-FA9E3C1CE662
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Geolocation sample driver file list

> [!IMPORTANT] 
> This documentation and the geolocation driver sample for Windows 8.1 has been deprecated.

The source file of the geolocation driver sample includes the following categories of files.

-   General files that are common to a UMDF sensor driver.
-   Sensor-specific files that are provided to demonstrate support for a simulated geolocation sensor.

The following table describes the general files that are common to a UMDF sensor driver.

| File name                          | Contents                                                                                                                                                                                                                   |
|------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Device.cpp                         | Contains an implementation of the CMyDevice member functions. This includes the **OnPrepareHardware** method which creates and initializes the sensor class extension.                                                     |
| Device.h                           | Contains a definition for the CMyDevice class.                                                                                                                                                                             |
| Dllsup.cpp                         | Contains the driver DLL’s entry point (DLLMain).                                                                                                                                                                           |
| Driver.cpp                         | Contains an implementation of the CMyDriver member functions. This includes the **OnDeviceAdd** method that creates an instance of the CMyDevice class (see description of Device.cpp).                                    |
| Driver.h                           | Contains a definition of the CMyDriver class.                                                                                                                                                                              |
| Internal.h                         | Contains local type definitions for the sample driver.                                                                                                                                                                     |
| Makefile.inc                       | Required to build an .INF file.                                                                                                                                                                                            |
| Queue.cpp                          | Contains an implementation of the CMyQueue member functions. This includes the **CreateInstance** method, which creates an instance of the I/O queue for the device.                                                       |
| Queue.h                            | Contains a definition of the CMyQueue class.                                                                                                                                                                               |
| Resource.h                         | Contains definitions consumed by SensorsGeolocationSample.h.                                                                                                                                                               |
| Sensor.cpp                         | Contains an implementation of the CSensor member functions. This includes the methods that return lists of supported properties and data fields and the methods that set writable properties and data fields.              |
| Sensor.h                           | Contains a definition of the CSensor class.                                                                                                                                                                                |
| SensDDI.cpp                        | Contains an implementation of the ISensorDriver callback interface in the CSensorDdi class. The sensor class extension calls methods in this interface to retrieve supported data such as objects, properties, and events. |
| SensorManager.cpp                  | Contains an implementation of the CSensorManager class. The methods in this class, as the name implies, manage the sensor device: starting it, stopping it, retrieving the device state, and so on.                        |
| SensorManager.h                    | Contains the definition of the CSensorManager class.                                                                                                                                                                       |
| SensorsGeolocationDriverSample.def | Declares the module parameters.                                                                                                                                                                                            |
| SensorsGeolocationDriverSample.htm | Contains a high-level description of the sample driver.                                                                                                                                                                    |
| SensorsGeolocationDriverSample.idl | Contains the necessary definitions for the driver’s COM component.                                                                                                                                                         |
| SensorsGeolocationDriverSample.inf | Contains the information that Windows Setup requires when you install the in-box driver on x86 and amd64 computers.                                                                                                        |
| SensorsGeolocationDriverSample.rc  | Contains definitions for resources that the driver requires, such as file type, file description string, file version, and original file name.                                                                             |
| Sources                            | Contains a series of macro definitions that are recognized by the Build utility                                                                                                                                            |

 

The following table lists the files that support the simulated geolocation sensor that is supported by the sample driver.

|                 |                                                                                                                                                                             |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| File name       | Contents                                                                                                                                                                    |
| Geolocation.cpp | Contains an implementation of the CGeolocation class. The methods in this class initialize the simulated sensor, retrieve readable properties, and set writable properties. |
| Geolocation.h   | Contains the definition of the CGeolocation class                                                                                                                           |

 

## Related topics
[The Sensors Geolocation Driver Sample](sensors-geolocation-driver-sample.md)  



