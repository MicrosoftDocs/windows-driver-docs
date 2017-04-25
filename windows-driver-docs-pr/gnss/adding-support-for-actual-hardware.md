---
title: Adding support for real hardware to the geolocation driver sample
author: windows-driver-content
description: The geolocation driver sample was provided as a starting point that simulates a GPS device. This topic describes how you can add support for real hardware.
ms.assetid: 0D16C46F-4622-4191-83F2-579FC17DE985
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Adding support for real hardware to the geolocation driver sample


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

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bsensors\sensors%5D:%20Adding%20support%20for%20real%20hardware%20to%20the%20geolocation%20driver%20sample%20%20RELEASE:%20%281/9/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


