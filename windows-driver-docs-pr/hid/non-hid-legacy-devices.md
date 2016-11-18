---
title: Non-HID legacy devices
author: windows-driver-content
description: This section describes drivers, transports, and filter-drivers for non-HID keyboards and mice. These devices primarily run on the PS/2 transport.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 4726DD47-C22E-4B92-A7BD-EB37BA53496F
---

# Non-HID legacy devices


This section describes drivers, transports, and filter-drivers for non-HID keyboards and mice. These devices primarily run on the PS/2 transport.

This section does not contain information about Sermouse, the Windows system function driver for a serial mouse. Note that the operational constraints that apply to I8042prt do not apply to Sermouse. In addition, upper-level device filter drivers are not used with Sermouse to customize the operation of a serial mouse. Instead, vendors need to install a device-specific function driver for the device. A device-specific function driver and Sermouse can operate at the same time, independent of one another.

## Non-HID driver stack


Windows 8 uses the following driver stack for non-HID keyboard, mouse, and touchpad hardware. The only non-HID Transport supported on Windows 8 is PS2.

![non-hid driver stack](images/non-hid-driver-stack.png)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhid\hid%5D:%20Non-HID%20legacy%20devices%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


