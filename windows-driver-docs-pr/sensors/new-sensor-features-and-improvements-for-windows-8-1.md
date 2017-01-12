---
title: New sensor features and improvements for Windows 8.1
description: This topic summarizes the new features and improvements for Sensors in WindowsWindows 8.1.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: F52BC6D1-DF67-4DE7-BEEC-D18C2A90B4CF
---

# New sensor features and improvements for Windows 8.1


This topic summarizes the new features and improvements for Sensors in WindowsWindows 8.1.

## Support for HID Devices


Windows 8.1 includes in-box support for any sensor that runs on the HID transport. This support is provided by a HID class driver.

The class driver supports the eleven sensors in the following list:

-   Accelerometer 3D
-   Ambient Light
-   Ambient Temperature
-   Atmospheric Pressure
-   Compass 3D
-   Device Orientation
-   Gyroscope 3D
-   Humidity
-   Inclinometer 3D
-   Presence
-   Proximity

In addition to these eleven sensors, the HID class driver supports a Custom class that a device vendor can use to support any sensor not found in the list.

## Testing sensor functionality with the Sensor Diagnostic Tool


You can use the Sensor Diagnostic Tool to test your sensor driver, firmware, and hardware. This tool is described in [The Sensor Diagnostic Tool](the-sensor-diagnostic-tool.md) topic.

## Sensor driver logic


The new programming guide includes a section that describes driver logic for a sensor device driver. This logic is presented as pseudo code that covers: driver initialization, driver interface, driver updates, device updates, and internal driver methods. You'll find this new section beginning with the [Sensor driver logic](driver-logic--pseudo-code-.md) topic.

## Sensors Geolocation Driver Sample


The geolocation sample driver demonstrates a minimal UMDF driver that emulates a Global Positioning System (GPS) device. This sample driver is described in detail in the new [Programming Guide](programming-guide.md).

The geolocation sample driver also includes code that demonstrates adding support for the Radio Management API. This is described in the [Supporting radio managment](https://msdn.microsoft.com/library/windows/hardware/jj200337) topic.

## Related topics


[Programming Guide](programming-guide.md)

[Sensor driver logic](driver-logic--pseudo-code-.md)

[The Sensor Diagnostic Tool](the-sensor-diagnostic-tool.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bsensors\sensors%5D:%20New%20sensor%20features%20and%20improvements%20for%20Windows%208.1%20%20RELEASE:%20%281/12/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





