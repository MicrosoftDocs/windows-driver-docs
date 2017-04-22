---
title: Minidriver requirements for tablet PCs
author: windows-driver-content
description: Describes the general requirements for vendor-supplied HID minidrivers for pen devices and button devices.
ms.assetid: 89BE7E13-4D46-4265-9522-D5A51999F633
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Minidriver requirements for tablet PCs running on earlier versions of Windows


This section pertains to operating systems prior to Windows 8 and describes the general requirements for vendor-supplied HID minidrivers for pen devices and button devices that are installed on a tablet PC edition system.

This section focuses on pen and button devices.

-   A pen device is integrated with the Tablet PC's LCD display and is used to capture the motion of a pen stylus.
-   A button device supplements the pen device and is used to capture button input. For more information about the Tablet PC, see the Windows XP Tablet PC Edition website

For more information about the Tablet PC, see the [Windows XP Tablet PC Edition](http://go.microsoft.com/fwlink/p/?linkid=275069) website.

For detailed information about system-supplied software that supports the Tablet PC, see the Tablet PC documentation in the Microsoft Windows SDK.

Pen and button devices belong to the HIDClass device setup class. These devices are operated by the system-supplied [HID Client Drivers](hid-client-drivers.md), which is linked to a HID minidriver. In the absence of a system-supplied HID minidriver that supports the hardware interface for a device, a vendor-supplied HID minidriver is required. The devices are operated from user mode by using the system-supplied Tablet PC API, which is described in the Windows SDK documentation.

### Requirements for PC pen devices

A Tablet PC pen device must:

-   Provide a top-level collection whose usage page is Digitizer and whose usage is Pen (see [HID usages](hid-usages.md)).

-   If a Tablet PC does not include a built-in mouse, a Tablet PC pen device must provide a top-level collection whose usage page is Generic Desktop and whose usage is Mouse. The purpose for the Mouse collection is to enable the system mouse cursor. However, the Mouse collection must not generate input reports. Only input from the Pen collection should be used for cursor movement. (If the Tablet PC's operating system starts without an installed mouse device, the system does not display a mouse cursor and does not handle the pen collection as a mouse device.)

-   Report raw data only. The driver must not compensate for linearity, pen tilt, display rotation, or scaling. These transformations are handled by the Tablet PC API. However, the driver must ensure that the pen coordinate system uses the same origin and orientation as that used by the API. For example, the driver must ensure that the origin is at the upper-left corner of a landscape display, that the x-coordinate increases from left to right, and that the y-coordinate increases from top to bottom.

-   If the device is a USB device, a Tablet PC pen device must support the [USB selective suspend feature](https://msdn.microsoft.com/library/windows/hardware/ff540144).

### <a href="" id="ddk-requirements-on-hid-minidrivers-for-tablet-pc-button-devices-kg"></a>Requirements for PC button devices

A Tablet PC button device supplements pen input on a Tablet PC. A button device supports one or more buttons. A button device that is installed on a Tablet PC must:

-   Provide one dedicated button for a Secure Attention Sequence (SAS) (as described in the Microsoft Windows SDK documentation).

-   Generate an event when a button is pressed and another event when that button is released.

-   Report distinct button events for each button, regardless of the number of buttons that are simultaneously pressed or released.

-   Provide a top-level collection whose usage page is Generic Desktop and whose usage is Keyboard (see [HID usages](hid-usages.md)). The Keyboard collection is only used to report SAS button events. When the SAS button is pressed, the following usages must be reported: Left Control, Left Alt, and Delete.

-   Provide a top-level collection whose usage page is Generic Desktop and whose usage is Tablet PC System Controls. Button events are reported by using a button array whose usage page is Button and the usage values range from 1 to the number of buttons.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhid\hid%5D:%20Minidriver%20requirements%20for%20tablet%20PCs%20running%20on%20earlier%20versions%20of%20Windows%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


