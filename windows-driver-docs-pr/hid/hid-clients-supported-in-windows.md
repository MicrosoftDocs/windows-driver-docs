---
title: HID Clients Supported in Windows
author: windows-driver-content
ms.assetid: E6584286-6BF1-40C7-83C1-D07077B13F3E
description: 
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# HID Clients Supported in Windows


Windows supports the following top-level collections:

| **Usage Page** | **Usage** | **Windows 7** | **Windows 8** | **Windows 10** | **Notes** | **Access Mode** |
| --- | --- | --- | --- | --- | --- | --- |
| 0x0001 | 0x0001 - 0x0002 | Yes | Yes | Yes | Mouse class driver and mapper driver | Exclusive |
| 0x0001 | 0x0004 - 0x0005 | Yes | Yes | Yes | Game Controllers | Shared |
| 0x0001 | 0x0006 - 0x0007 | Yes | Yes | Yes | Keyboard / Keypad class driver and mapper driver | Exclusive |
| 0x0001 | 0x000C | No | Yes | Yes | Flight Mode Switch | Shared |
| 0x0001 | 0x0080 | Yes | Yes | Yes | System Controls (Power) | Shared |
| 0x000C | 0x0001 | Yes | Yes | Yes(For both Windows 10 and Windows 10 Mobile) | Consumer Controls | Shared(For both Windows 10 and Windows 10 Mobile) |
| 0x000D | 0x0001 | Yes | Yes | Yes | External Pen Device | Exclusive |
| 0x000D | 0x0002 | Yes | Yes | Yes | Integrated Pen Device | Exclusive |
| 0x000D | 0x0004 | Yes | Yes | Yes | Touchscreen | Exclusive |
| 0x000D | 0x0005 | No | Yes | Yes | Precision Touchpad (PTP) | Exclusive |
| 0x0020 | *Multiple | No | Yes | Yes | Sensors | Shared |
| 0x0084 | 0x004 | Yes | Yes | Yes | HID UPS Battery | Shared |
| 0x008C | 0x0002 | No | Yes(Windows 8.1 and later) | Yes | Barcode Scanner (hidscanner.dll) | Shared |


In the preceding table, the access mode for input HID clients is Exclusive to prevent other HID clients from intercepting or receiving global input state when they are not the target recipient of that input. Therefore, for security reasons RIM (Raw Input Manager) opens all such devices exclusively. 

Sharing mode allows multiple applications to access the device. For example, multiple applications can access a barcode scanner to inquire about device capabilities and retrieve statistics. However, retrieving decoded data from a barcode scanner is done in Exclusive mode. Usages are defined by the [USB HID POS Scanner standard specification](https://go.microsoft.com/fwlink/?linkid=830661). 

*Multiple: Sensors usages from 0x00 – 0xFF are segmented for different purposes. For example 0x10 indicates a Biometric sensor; 0x40 indicates a Light sensor. Those allocations are not contiguous. For the list of sensor usages, see  [Review Request 39:HID Usage Table Sensor Page](https://go.microsoft.com/fwlink/?linkid=830659). For information about  sensors usages that are supported in Windows, [HID Sensors Usages](https://go.microsoft.com/fwlink/?linkid=830658).

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhid\hid%5D:%20HID%20Clients%20Supported%20in%20Windows%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


