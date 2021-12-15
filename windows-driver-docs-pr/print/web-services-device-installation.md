---
title: Installing printers that support Web Services for Devices
description: Installing printers that support Web Services for Devices
keywords:
- Web Services Device Monitor WDK printer
ms.date: 04/20/2017
---

# Installing printers that support Web Services for Devices


Networked printers that are enabled for Web Services for Devices (WSD) can be discovered and paired through the [Windows.Devices.Enumeration](/uwp/api/Windows.Devices.Enumeration) namespace API.

Once a WSD printer has been paired, the [WSDMON Port Monitor](wsdmon-port-monitor.md) will automatically install the printer.

For an example of device enumeration and pairing that uses **Windows.Devices.Enumeration**, see the [Device enumeration and pairing sample](https://github.com/Microsoft/Windows-universal-samples/tree/master/Samples/DeviceEnumerationAndPairing) on GitHub.

For more information, see the [Enumerate devices over a network](/windows/uwp/devices-sensors/enumerate-devices-over-a-network) article in the Windows SDK documentation.

 

