---
title: usbkd.usbhcdhccontext
description: The usbkd.usbhcdhccontext command displays the USB2LIB_HC_CONTEXT for a USB host controller.
ms.assetid: 72A4BAA1-D395-4D6A-BEFB-F217E994B4E7
keywords: ["usbkd.usbhcdhccontext Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- usbkd.usbhcdhccontext
api_type:
- NA
ms.localizationpriority: medium
---

# !usbkd.usbhcdhccontext


The **!usbkd.usbhcdhccontext** command displays the **USB2LIB\_HC\_CONTEXT** for a USB host controller.

```dbgcmd
!usbkd.usbhcdhccontext DeviceExtension
```

## <span id="ddk__devobj_dbg"></span><span id="DDK__DEVOBJ_DBG"></span>Parameters


<span id="_______DeviceExtension______"></span><span id="_______deviceextension______"></span><span id="_______DEVICEEXTENSION______"></span> *DeviceExtension*   
Address of the device extension for the functional device object (FDO) of a USB host controller.

## <span id="DLL"></span><span id="dll"></span>DLL


Usbkd.dll

## <span id="see_also"></span>See also


[USB 2.0 Debugger Extensions](usb-2-0-extensions.md)

[Universal Serial Bus (USB) Drivers](https://go.microsoft.com/fwlink/p?LinkID=227351)

 

 






