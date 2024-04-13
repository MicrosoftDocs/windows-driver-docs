---
title: "!usbkd.usbusb2ep"
description: "The !usbkd.usbusb2ep command displays information from a usbport _USB2_EP structure."
keywords: ["!usbkd.usbusb2ep Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- usbkd.usbusb2ep
api_type:
- NA
---

# !usbkd.usbusb2ep

The **!usbkd.usbusb2ep** command displays information from a **usbport!\_USB2\_EP** structure.

```dbgcmd
!usbkd.usbusb2ep StructAddr
```

## Parameters

<span id="_______StructAddr______"></span><span id="_______structaddr______"></span><span id="_______STRUCTADDR______"></span> *StructAddr*   
Address of a **usbport!\_USB2\_EP** structure. To get the address of **usbport!\_USB2\_EP** structure, use [**!usbkd.usb2**](-usbkd-usb2.md).

## DLL

Usbkd.dll

## See also

[USB 2.0 Debugger Extensions](usb-2-0-extensions.md)

[Universal Serial Bus (USB) Drivers](../usbcon/index.md)
