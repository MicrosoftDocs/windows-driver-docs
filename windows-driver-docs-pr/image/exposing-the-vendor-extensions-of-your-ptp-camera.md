---
title: Exposing the Vendor Extensions of Your PTP Camera
description: Exposing the Vendor Extensions of Your PTP Camera
ms.assetid: b3a8b70b-c7ac-4e45-97bb-9b58e013100d
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Exposing the Vendor Extensions of Your PTP Camera





A PTP device can support vendor-extended properties, vendor-extended events, and vendor-extended commands.

Vendor-extended properties and events are listed in the **DeviceData** INF file entry (see [INF files for WIA devices](inf-files-for-wia-devices.md) for more information), so the driver is able to handle them. An entry listing the vendor extension ID is required. This must match the VendorExtensionID field in the DeviceInfo dataset. An example of the other entries is shown here and described in the following sections.

```INF
[DeviceData]
VendorExtID=0x12345678
PropCode="0xD001,0xD002,0xD003"
PropCodeD001="0x00009802,VendorProperty1"
PropCodeD002="0x00009803,VendorProperty2"
PropCodeD003="0x00009804,VendorProperty3"
EventCode="0xC001,0xC002"
EventCodeC001={191D9AE7-EE8C-443c-B3E8-A3F87E0CF3CC}
EventCodeC002={8162F5ED-62B7-42c5-9C2B-B1625AC0DB93}
```

 

 




