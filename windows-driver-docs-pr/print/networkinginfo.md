---
title: NetworkingInfo
description: NetworkingInfo
ms.assetid: 81c615d4-8a7c-4d28-a3ce-5233899e35cf
ms.date: 11/28/2017
ms.localizationpriority: medium
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

 

 




