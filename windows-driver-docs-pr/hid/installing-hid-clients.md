---
title: Installing HID clients
description: This section describes the following requirements for installing HIDClass devices in Microsoft Windows.
ms.assetid: 080992B1-AB36-4BA1-BF44-7CF0C9F4EEE3
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Installing HID clients


This section describes the following requirements for installing HIDClass devices in Microsoft Windows.

-   Vendors must use the [*hardware IDs*](https://docs.microsoft.com/windows-hardware/drivers/install/hardware-ids) for top-level collections that are designated as *vendor hardware ID formats* in [HIDClass Hardware IDs for Top-Level Collections](hidclass-hardware-ids-for-top-level-collections.md).

-   Vendor-supplied drivers for parent input devices (installed below the HID class driver in driver stacks for HIDClass devices) must supply the hardware information that the HID class driver uses to generate hardware IDs for top-level collections. (Note that the system-provided drivers for HIDClass devices do this automatically.)

-   In Windows Vista and later versions of Windows, vendors can enable the selective suspend feature for USB HID devices. This feature is defined in Revision 2.0 of the *Universal Serial Bus Specification.* For more information about how Windows supports the USB selective suspend feature, see [USB selective suspend](../usbcon/usb-selective-suspend.md).

There are no other HIDClass-specific requirements for installing HIDClass devices. For more information about how to install devices, see [Device Installation Overview](https://msdn.microsoft.com/library/windows/hardware/ff549455).

 

 




