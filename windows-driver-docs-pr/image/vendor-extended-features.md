---
title: Vendor-Extended Features
author: windows-driver-content
description: Vendor-Extended Features
ms.assetid: 8063622e-efc4-4940-893f-2916bf297d12
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Vendor-Extended Features


## <a href="" id="ddk-vendor-extended-features-si"></a>


This section discusses vendor-extended features a PTP device can support the following and how to expose these extensions:

[Exposing the Vendor Extensions of Your PTP Camera](exposing-the-vendor-extensions-of-your-ptp-camera.md)

[Vendor-Extended Properties](vendor-extended-properties.md)

[Vendor-Extended Events](vendor-extended-events.md)

[Vendor-Extended Commands](vendor-extended-commands.md)

Vendor-extended properties and events must be listed in the **DeviceData** INF file entry and the events must be provided a name in the **Events** INF file entry (see [INF files for WIA devices](inf-files-for-wia-devices.md) for more information). An entry listing the vendor extension ID is required. This must match the **VendorExtensionID** field in the DeviceInfo dataset. An example of the other entries is shown here and described in the following sections.

```
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

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Vendor-Extended%20Features%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


