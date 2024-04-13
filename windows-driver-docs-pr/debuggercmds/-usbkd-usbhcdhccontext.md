---
title: "!usbkd.usbhcdhccontext"
description: "The !usbkd.usbhcdhccontext command displays the USB2LIB_HC_CONTEXT for a USB host controller."
keywords: ["!usbkd.usbhcdhccontext Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- usbkd.usbhcdhccontext
api_type:
- NA
---

# !usbkd.usbhcdhccontext

The **!usbkd.usbhcdhccontext** command displays the **USB2LIB\_HC\_CONTEXT** for a USB host controller.

```dbgcmd
!usbkd.usbhcdhccontext DeviceExtension
```

## Parameters

<span id="_______DeviceExtension______"></span><span id="_______deviceextension______"></span><span id="_______DEVICEEXTENSION______"></span> *DeviceExtension*   
Address of the device extension for the functional device object (FDO) of a USB host controller.

## DLL

Usbkd.dll

## See also

[USB 2.0 Debugger Extensions](usb-2-0-extensions.md)

[Universal Serial Bus (USB) Drivers](../usbcon/index.md)
