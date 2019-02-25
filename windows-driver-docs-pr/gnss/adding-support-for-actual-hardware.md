---
title: Adding support for real hardware to the geolocation driver sample
description: The geolocation driver sample was provided as a starting point that simulates a GPS device. This topic describes how you can add support for real hardware.
ms.assetid: 0D16C46F-4622-4191-83F2-579FC17DE985
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Adding support for real hardware to the geolocation driver sample

> [!IMPORTANT] 
> This documentation and the geolocation driver sample for Windows 8.1 has been deprecated.

The geolocation driver sample was provided as a starting point that simulates a GPS device. This topic describes how you can add support for real hardware.

The revisions and additions needed to support real hardware with the geolocation sample are described briefly in the following table. The table also identifies where you can find more information.

|                                                                                                  |                                                                                                                                                                                                                |
|--------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Revision or Addition                                                                             | More Information                                                                                                                                                                                               |
| Rename the source and header files to reflect the purpose of your new sensor.                    | See the "Customizing the Sample" and the "Adding an Additional Sensor to the Sample" sections of the readme (SensorsGeolocationSample.htm) that is included with the sample sources in the Windows Driver Kit. |
| Replace the geolocation properties with the properties supported by your new sensors.            | See the "Adding an Additional Sensor to the Sample" sections of the readme (SensorsGeolocationSample.htm) that is included with the sample sources in the Windows Driver Kit.                                  |
| Add a module containing the necessary code to support the transport required by your new sensor. | .                                                                                                                                                                                                              |

 

If you are developing a GPS (or other geolocation) sensor and it runs on the HID transport, you can integrate your device with the inbox HID class driver.

The readme file, SensorsGeolocationDriverSample.htm, that ships with the Windows Driver Kit includes instructions for modifying this driver to support a temperature sensor.

**Note**  
If your sensor supports a transport other than HID, you can build on the Geolocation sample and use it as a starting point for your new driver. However, if your sensor supports the HID transport, you should write firmware compatible with the inbox HID class driver.

 

## Related topics
[The Sensors Geolocation Driver Sample](sensors-geolocation-driver-sample.md)  



