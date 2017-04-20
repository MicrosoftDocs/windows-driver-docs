---
title: Binding minidrivers to the HID class
author: windows-driver-content
description: This section describes the operation of the system-supplied HID class driver and HID minidrivers, which support devices in the HIDClass device setup class.
ms.assetid: 2B51E205-8EBB-413A-A317-0923FAB77F0E
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Binding minidrivers to the HID class


This section describes the operation of the system-supplied HID class driver and HID minidrivers, which support devices in the HIDClass [device setup class](https://msdn.microsoft.com/library/windows/hardware/ff541509).

The HID class driver provides the interface that upper-level drivers and user-mode applications use to access the HID collections supported by an input device. The HID class driver uses HID minidrivers to access the hardware of an input device. HID minidrivers abstract the operation of the port of bus to which the input device is attached. The HID class driver is an export driver that is linked to HID minidrivers. HID minidrivers bind their operation to the HID class driver by calling [**HidRegisterMinidriver**](https://msdn.microsoft.com/library/windows/hardware/ff539835) to register themselves with the HID class driver.

The combined operation of the HID class driver and a HID minidriver acts as a WDM function driver for an input device and a bus driver for the child devices (HID collections) that the input device supports. This design makes it possible for the HID class driver to operate USB HID devices and non-USB input devices that are attached to ports or buses other than a USB bus. The operational detail of the underlying parent device is transparent to upper-level drivers or user-mode applications.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhid\hid%5D:%20Binding%20minidrivers%20to%20the%20HID%20class%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


