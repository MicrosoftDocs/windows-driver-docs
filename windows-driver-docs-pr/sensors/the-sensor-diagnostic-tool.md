---
title: Testing sensor functionality with the Sensor Diagnostic Tool
author: windows-driver-content
description: Use the Sensor Diagnostic Tool to test your driver, firmware, and hardware functionality.
ms.assetid: 447E1348-53BA-4AD4-9010-A6452F46A827
keywords: ["testing sensors", "sensors, testing", "Sensor Diagnostic Tool", "sensor driver, testing", "sensor firmware, testing", "sensor hardware, testing", "sensor events", "sensor, report interval", "sensor, change sensitivity", "report interval", "change sensitivity"]
---

# Testing sensor functionality with the Sensor Diagnostic Tool


Use the Sensor Diagnostic Tool to test your driver, firmware, and hardware functionality.

**Note**  The Sensor Diagnostic Tool is acceptable for testing on Windows 8.1 and earlier operating systems. The tool is now deprecated for Windows 10, so for sensor driver testing and diagnostics on Windows 10 and later operating systems, please use the SensorInfo App from the Windows Store.

 

The tool invokes the Sensor and Location API to test:

-   Data Retrieval
-   Event handling
-   Report intervals
-   Change sensitivity
-   Property retrieval

Instead of writing an application to perform these tests, you can use the Sensor Diagnostic Tool, which ships as part of the Windows Driver Kit (WDK).

For example, if your driver development computer is an x64-based machine, and you installed the WDK to the default location, then you will find the sensor diagnostic tool in the following folder:

*C:\\Program Files (x86)\\Windows Kits\\8.1\\Tools\\x64\\sensordiagnostictool.exe*
Once your sensor or location driver is installed and your hardware is attached to your PC, the tool immediately recognizes and records your device in the list of available sensors.

The following image shows the Sensor Diagnostic Tool startup screen when several sensors are connected to a PC.

![sensor diagnostic tool: startup](images/sdt-startup.png)

In this case, the Sensor Diagnostic Tool detected the presence of a collection of HID sensors as well as a simple device orientation sensor, the Windows Location provider, and a Geolocation Sensor which is supported by the Geolocation driver sample.

## Support for Ambient Light Sensors


The Sensor Diagnostic Tool includes support for ambient light sensors (ALS). The current display brightness is reported in the SB% box in the tool's upper left corner.

However, it's important to note that when the tool retrieves ALS values, it returns these values as (LUX, Offset) pairs. This ordering differs from the Advanced Configuration and Power Interface (ACPI) standard of (Offset, LUX) pairs.

## Related topics
[Testing Sensor Functionality](testing-sensor-functionality.md)  
[Testing Location Functionality](testing-location-functionality.md)  

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bsensors\sensors%5D:%20Testing%20sensor%20functionality%20with%20the%20Sensor%20Diagnostic%20Tool%20%20RELEASE:%20%281/12/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


