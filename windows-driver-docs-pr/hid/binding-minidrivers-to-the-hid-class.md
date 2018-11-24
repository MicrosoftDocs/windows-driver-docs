---
title: Binding minidrivers to the HID class
description: This section describes the operation of the system-supplied HID class driver and HID minidrivers, which support devices in the HIDClass device setup class.
ms.assetid: 2B51E205-8EBB-413A-A317-0923FAB77F0E
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Binding minidrivers to the HID class


This section describes the operation of the system-supplied HID class driver and HID minidrivers, which support devices in the HIDClass [device setup class](https://msdn.microsoft.com/library/windows/hardware/ff541509).

The HID class driver provides the interface that upper-level drivers and user-mode applications use to access the HID collections supported by an input device. The HID class driver uses HID minidrivers to access the hardware of an input device. HID minidrivers abstract the operation of the port of bus to which the input device is attached. The HID class driver is an export driver that is linked to HID minidrivers. HID minidrivers bind their operation to the HID class driver by calling [**HidRegisterMinidriver**](https://msdn.microsoft.com/library/windows/hardware/ff539835) to register themselves with the HID class driver.

The combined operation of the HID class driver and a HID minidriver acts as a WDM function driver for an input device and a bus driver for the child devices (HID collections) that the input device supports. This design makes it possible for the HID class driver to operate USB HID devices and non-USB input devices that are attached to ports or buses other than a USB bus. The operational detail of the underlying parent device is transparent to upper-level drivers or user-mode applications.

 

 




