---
title: New Sensor Features and Improvements for Windows 8.1
description: This topic summarizes the new features and improvements for Sensors in WindowsWindows 8.1.
ms.date: 01/11/2024
---

# New sensor features and improvements for Windows 8.1

This topic summarizes the new features and improvements for sensors in Windows 8.1.

## Support for HID Devices

Windows 8.1 includes in-box support for any sensor that runs on the HID transport. This support is provided by a HID class driver.

The class driver supports the eleven sensors in the following list:

- Accelerometer 3D
- Ambient Light
- Ambient Temperature
- Atmospheric Pressure
- Compass 3D
- Device Orientation
- Gyroscope 3D
- Humidity
- Inclinometer 3D
- Presence
- Proximity

In addition to these eleven sensors, the HID class driver supports a Custom class that a device vendor can use to support any sensor not found in the list.

## Testing sensor functionality with the Sensor Diagnostic Tool

You can use the Sensor Diagnostic Tool to test your sensor driver, firmware, and hardware. This tool is described in [The Sensor Diagnostic Tool](the-sensor-diagnostic-tool.md) topic.

## Sensor driver logic

The new programming guide includes a section that describes driver logic for a sensor device driver. This logic is presented as pseudo code that covers: driver initialization, driver interface, driver updates, device updates, and internal driver methods. You'll find this new section beginning with the [Sensor driver logic](driver-logic--pseudo-code-.md) topic.

## Sensors Geolocation Driver Sample

The geolocation sample driver demonstrates a minimal UMDF driver that emulates a Global Positioning System (GPS) device. This sample driver is described in detail in the new [Programming Guide](../gnss/installing-the-sample-driver.md).

The geolocation sample driver also includes code that demonstrates adding support for the Radio Management API. This is described in the [Supporting radio managment](../gnss/supporting-radio-management.md) topic.

## Related topics

- [Sensor driver logic](driver-logic--pseudo-code-.md)
- [The Sensor Diagnostic Tool](the-sensor-diagnostic-tool.md)
