---
title: Power management for HID over USB
author: windows-driver-content
description: HID over USB employs USB suspend to power manage a device.
ms.assetid: 7B5E10B0-2EEA-450A-9E21-B60215F60027
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Power management


HID over USB employs USB suspend to power manage a device.

Power is managed primarily in the following two configurations:

1.  Case \#1: The system is in a power managed state (e.g. S3) but the device is armed to wake the system up. E.g. a HID USB keyboard that is armed to wake up a desktop from S3 on key press.
2.  Case \#2: The system is in a running state (e.g. S0) but the device has idled out (no user interaction). E.g. selective suspend a HID USB mouse when no one is using or touching it.

*Case \#1 Provisions*

HID devices don't automatically wake up a system from a low- power state. Only specific HID devices (e.g. Top level collections of keyboards and mice) do this.

If an end user wishes to disarm a device from waking up the system, the user can specify this via the properties/power management tab in device manager.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhid\hid%5D:%20Power%20management%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


