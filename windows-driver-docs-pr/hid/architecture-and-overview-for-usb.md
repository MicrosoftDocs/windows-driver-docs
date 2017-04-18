---
title: Architecture and overview
author: windows-driver-content
description: This section describes the driver stack for devices that support HID over the USB transport.
ms.assetid: D0D87B86-AD36-442A-9D36-571D12A360D4
---

# Architecture and overview


This section describes the driver stack for devices that support HID over the USB transport.

The HID over USB driver stack consists of the following components supplied by Microsoft. The following illustration depicts the stack and these components.

![hid-usb driver architecture ](images/transport-usb.png)

Windows 8 provides a WDF-based HID miniport driver that implements version 1.1+ of the protocol specification for HID over USB. This driver is named HIDUSB.SYS. Windows loads this driver based on a USB Device Class compatible ID match.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhid\hid%5D:%20Architecture%20and%20overview%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


