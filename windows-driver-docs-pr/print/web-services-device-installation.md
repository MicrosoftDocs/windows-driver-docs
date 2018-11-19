---
title: Installing printers that support Web Services for Devices
description: Installing printers that support Web Services for Devices
ms.assetid: fb5f043b-bae5-4cb6-95c0-e4e6b9e9d187
keywords:
- Web Services Device Monitor WDK printer
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Installing printers that support Web Services for Devices


Networked printers that are enabled for Web Services for Devices (WSD) can be discovered and paired through the [Windows.Devices.Enumeration](https://msdn.microsoft.com/library/windows/apps/windows.devices.enumeration.aspx) namespace API.

Once a WSD printer has been paired, the [WSDMON Port Monitor](wsdmon-port-monitor.md) will automatically install the printer.

For an example of device enumeration and pairing that uses **Windows.Devices.Enumeration**, see the [Device enumeration and pairing sample](https://github.com/Microsoft/Windows-universal-samples/tree/master/Samples/DeviceEnumerationAndPairing) on GitHub.

For more information, see the [Enumerate devices over a network](https://msdn.microsoft.com/windows/uwp/devices-sensors/enumerate-devices-over-a-network) article in the Windows SDK documentation.

 

 




