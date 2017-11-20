---
title: NetworkingInfo
description: NetworkingInfo
MS-HAID:
- 'autocfg\_23a2ecff-cb08-4cc9-b600-16b40ad03c1a.xml'
- 'print.networkinginfo'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 81c615d4-8a7c-4d28-a3ce-5233899e35cf
---

# NetworkingInfo


Schema Path:\\Printer.DeviceInfo:NetworkingInfo

Node Type:Property

This section deals with data that is associated with the device as a whole. The user or administrator can set much of this data to personalize their device.

NetworkingInfo has two values: **HostName** and **IPAddress**.

### <span id="hostname"></span><span id="HOSTNAME"></span> HostName

Schema Path:\\Printer.DeviceInfo:NetworkingInfo.HostName

Node Type:Value

Data Type:BIDI\_STRING

Description:A string that contains the current networking HostName of the device. This information might not be available for all devices.

### <span id="ipaddress"></span><span id="IPADDRESS"></span> IPAddress

Schema Path:\\Printer.DeviceInfo:NetworkingInfo.IPAddress

Node Type:Value

Data Type:BIDI\_STRING

Description:A string that contains the current TCP/IP address of the device. This address could be in either IPV4 or IPV6 format. This address is an address that the port monitor is currently using to communicate with the print device.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20NetworkingInfo%20%20RELEASE:%20%2811/20/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




