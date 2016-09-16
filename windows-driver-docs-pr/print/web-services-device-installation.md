---
title: Installing printers that support Web Services for Devices
author: windows-driver-content
description: Installing printers that support Web Services for Devices
MS-HAID:
- 'prtinst\_e7abdba9-4f13-4d31-b43a-29a98e5932e1.xml'
- 'print.web\_services\_device\_installation'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: fb5f043b-bae5-4cb6-95c0-e4e6b9e9d187
keywords: ["Web Services Device Monitor WDK printer"]
---

# Installing printers that support Web Services for Devices


Networked printers that are enabled for Web Services for Devices (WSD) can be discovered and paired through the [Windows.Devices.Enumeration](https://msdn.microsoft.com/library/windows/apps/windows.devices.enumeration.aspx) namespace API.

Once a WSD printer has been paired, the [WSDMON Port Monitor](wsdmon-port-monitor.md) will automatically install the printer.

For an example of device enumeration and pairing that uses **Windows.Devices.Enumeration**, see the [Device enumeration and pairing sample](https://github.com/Microsoft/Windows-universal-samples/tree/master/Samples/DeviceEnumerationAndPairing) on GitHub.

For more information, see the [Enumerate devices over a network](https://msdn.microsoft.com/windows/uwp/devices-sensors/enumerate-devices-over-a-network) article in the Windows SDK documentation.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Installing%20printers%20that%20support%20Web%20Services%20for%20Devices%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


