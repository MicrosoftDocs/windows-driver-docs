---
title: Architecture of HID over USB transport
author: windows-driver-content
description: This section describes the driver stack for devices that support HID over USB transport.
ms.assetid: D0D87B86-AD36-442A-9D36-571D12A360D4
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Architecture and overview


This section describes the driver stack for devices that support HID over the USB transport.

The HID over USB driver stack consists of the following components supplied by Microsoft. The following illustration depicts the stack and these components.

![hid-usb driver architecture ](images/transport-usb.png)

Windows 8 provides a WDF-based HID miniport driver that implements version 1.1+ of the protocol specification for HID over USB. This driver is named HIDUSB.SYS. Windows loads this driver based on a USB Device Class compatible ID match.

 

 




