---
title: Geolocation sample driver file list
author: windows-driver-content
description: The source file of the geolocation driver sample includes the following categories of files.
ms.assetid: 8A9A1102-921B-40FF-94F2-FA9E3C1CE662
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bsensors\sensors%5D:%20Geolocation%20sample%20driver%20file%20list%20%20RELEASE:%20%281/9/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


