---
title: Installing HID clients
author: windows-driver-content
description: This section describes the following requirements for installing HIDClass devices in Microsoft Windows.
ms.assetid: 080992B1-AB36-4BA1-BF44-7CF0C9F4EEE3
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Installing HID clients


This section describes the following requirements for installing HIDClass devices in Microsoft Windows.

-   Vendors must use the [*hardware IDs*](https://msdn.microsoft.com/library/windows/hardware/ff556288#wdkgloss-hardware-id) for top-level collections that are designated as *vendor hardware ID formats* in [HIDClass Hardware IDs for Top-Level Collections](hidclass-hardware-ids-for-top-level-collections.md).

-   Vendor-supplied drivers for parent input devices (installed below the HID class driver in driver stacks for HIDClass devices) must supply the hardware information that the HID class driver uses to generate hardware IDs for top-level collections. (Note that the system-provided drivers for HIDClass devices do this automatically.)

-   In Windows Vista and later versions of Windows, vendors can enable the selective suspend feature for USB HID devices. This feature is defined in Revision 2.0 of the *Universal Serial Bus Specification.* For more information about how Windows supports the USB selective suspend feature, see [USB Selective Suspend](https://msdn.microsoft.com/library/windows/hardware/ff540144).

There are no other HIDClass-specific requirements for installing HIDClass devices. For more information about how to install devices, see [Device Installation Overview](https://msdn.microsoft.com/library/windows/hardware/ff549455).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhid\hid%5D:%20Installing%20HID%20clients%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


