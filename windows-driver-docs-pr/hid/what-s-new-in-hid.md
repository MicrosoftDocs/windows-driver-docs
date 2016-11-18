---
title: What's New in HID
author: windows-driver-content
description: This topic summarizes the new features and improvements for Human Interface Devices (HID) in Windows 10.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
Search.SourceType: Video
ms.assetid: AA8590B4-AAEA-4D41-972F-38149CE328E2
---

# What's New in HID


This topic summarizes the new features and improvements for Human Interface Devices (HID) in Windows 10.

## HID WinRT API


The [Windows.Devices.HumanInterfaceDevice](https://msdn.microsoft.com/library/windows/apps/xaml/dn263140) API lets a Windows Store app access devices that support the Human Interface Device (HID) protocol.

The following short video describes an end-to-end sample solution for HID that's available for download on the MSDN samples gallery. (This solution includes a sample app created using the new HID WinRT API.)

<iframe src="https://hubs-video.ssl.catalog.video.msn.com/embed/2d4da9fc-c2ea-4933-949d-eb0cff3c9c4e/IA?csid=ux-en-us&MsnPlayerLeadsWith=html&PlaybackMode=Inline&MsnPlayerDisplayShareBar=false&MsnPlayerDisplayInfoButton=false&iframe=true&QualityOverride=HD" width="720" height="405" allowFullScreen="true" frameBorder="0" scrolling="no">End to end solution for HID</iframe>

## Design Guide


The [Design Guide](index.md) has been updated to include some new topics. And also, existing content has been revised where relevant, to show improved HID support in Windows 10. Here are some of the new, and updated topics:

**New topic**

-   [ACPI button device](acpi-button-device.md)

**Updated topics**

-   [HID Transports](hid-transports.md)

-   [HID button drivers](buttons.md)

-   [HID Clients Supported in Windows](hid-clients-supported-in-windows.md)

## <a href="" id="hid-over-i2c"></a>HID Over I²C


The HID protocol originally targeted human interface devices like: keyboards, mice, and joysticks. It was originally developed to run over USB. For Windows 8, Microsoft created a new HID miniport driver that allows devices to communicate over an Inter-Integrated Circuit (I²C) bus.

## Related topics
[Design Guide](index.md)  
[HID Over I2C](hid-over-i2c-guide.md)  

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhid\hid%5D:%20What's%20New%20in%20HID%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


