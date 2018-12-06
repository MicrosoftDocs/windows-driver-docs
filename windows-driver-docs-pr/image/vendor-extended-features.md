---
title: Vendor-Extended Features
description: Vendor-Extended Features
ms.assetid: 8063622e-efc4-4940-893f-2916bf297d12
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Vendor-Extended Features





This section discusses vendor-extended features a PTP device can support the following and how to expose these extensions:

[Exposing the Vendor Extensions of Your PTP Camera](exposing-the-vendor-extensions-of-your-ptp-camera.md)

[Vendor-Extended Properties](vendor-extended-properties.md)

[Vendor-Extended Events](vendor-extended-events.md)

[Vendor-Extended Commands](vendor-extended-commands.md)

Vendor-extended properties and events must be listed in the **DeviceData** INF file entry and the events must be provided a name in the **Events** INF file entry (see [INF files for WIA devices](inf-files-for-wia-devices.md) for more information). An entry listing the vendor extension ID is required. This must match the **VendorExtensionID** field in the DeviceInfo dataset. An example of the other entries is shown here and described in the following sections.

```INF
[DeviceData]
VendorExtID=0x12345678
PropCode="0xD001,0xD002,0xD003"
PropCodeD001="0x00009802,Vendorproperty1"
PropCodeD002="0x00009803,Vendorproperty2"
PropCodeD003="0x00009804,Vendorproperty3"
EventCode="0xC001,0xC002"
EventCodeC001={191D9AE7-EE8C-443c-B3E8-A3F87E0CF3CC}
EventCodeC002={8162F5ED-62B7-42c5-9C2B-B1625AC0DB93}

[Events]
EventCodeC001="Vendorevent1",{191D9AE7-EE8C-443c-B3E8-A3F87E0CF3CC},*
EventCodeC002="Vendorevent2",{8162F5ED-62B7-42c5-9C2B-B1625AC0DB93},*
```

**Note**   In INF files for WIA devices, vendor property names must be a single word, with no spaces, and comprised of only alphanumeric values.

 

 

 




