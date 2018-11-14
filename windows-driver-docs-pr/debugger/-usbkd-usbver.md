---
title: usbkd.usbver
description: The usbkd.usbver command displays the USBD interface version of the USB driver stack.
ms.assetid: E3F5A971-64FB-4826-8DC0-59F3615C106A
keywords: ["usbkd.usbver Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- usbkd.usbver
api_type:
- NA
ms.localizationpriority: medium
---

# !usbkd.usbver


The **!usbkd.usbver** command displays the USBD interface version of the USB driver stack.

```dbgcmd
!usbkd.usbver
```

## <span id="DLL"></span><span id="dll"></span>DLL


Usbkd.dll

Remarks
-------

The value of the USBD interface version is stored in the variable `usbport!usbd_version`.

Examples
--------

Here is an example of the output of **!usbkd.usbver**.

```dbgcmd
1: kd> !usbkd.usbver

USBD VER 600 USB stack is VISTA
```

## <span id="see_also"></span>See also


[USB 2.0 Debugger Extensions](usb-2-0-extensions.md)

[Universal Serial Bus (USB) Drivers](https://go.microsoft.com/fwlink/p?LinkID=227351)

**USBD\_IsInterfaceVersionSupported**
 

 






