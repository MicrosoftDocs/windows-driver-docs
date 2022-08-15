---
title: NetworkingInfo
description: Provides networking information the user or administrator can set to personalize their device.
ms.date: 08/31/2021
---

# NetworkingInfo

Schema Path: \\Printer.DeviceInfo:NetworkingInfo

Node Type: Property

This section deals with data that is associated with the device as a whole. The user or administrator can set much of this data to personalize their device.

NetworkingInfo has two values: **HostName** and **IPAddress**.

## HostName

Schema Path: \\Printer.DeviceInfo:NetworkingInfo.HostName

Node Type: Value

Data Type: BIDI_STRING

Description: A string that contains the current networking HostName of the device. This information might not be available for all devices.

## IPAddress

Schema Path: \\Printer.DeviceInfo:NetworkingInfo.IPAddress

Node Type: Value

Data Type: BIDI_STRING

Description: A string that contains the current TCP/IP address of the device. This address could be in either IPV4 or IPV6 format. This address is an address that the port monitor is currently using to communicate with the print device.
