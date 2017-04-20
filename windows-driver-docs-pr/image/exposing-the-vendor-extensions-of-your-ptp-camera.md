---
title: Exposing the Vendor Extensions of Your PTP Camera
author: windows-driver-content
description: Exposing the Vendor Extensions of Your PTP Camera
ms.assetid: b3a8b70b-c7ac-4e45-97bb-9b58e013100d
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Exposing the Vendor Extensions of Your PTP Camera


## <a href="" id="ddk-exposing-the-vendor-extensions-of-your-ptp-camera-si"></a>


A PTP device can support vendor-extended properties, vendor-extended events, and vendor-extended commands.

Vendor-extended properties and events are listed in the **DeviceData** INF file entry (see [INF files for WIA devices](inf-files-for-wia-devices.md) for more information), so the driver is able to handle them. An entry listing the vendor extension ID is required. This must match the VendorExtensionID field in the DeviceInfo dataset. An example of the other entries is shown here and described in the following sections.

```
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Exposing%20the%20Vendor%20Extensions%20of%20Your%20PTP%20Camera%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


