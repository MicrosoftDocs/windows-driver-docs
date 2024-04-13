---
title: "!usbkd.usbver"
description: "The !usbkd.usbver command displays the USBD interface version of the USB driver stack."
keywords: ["!usbkd.usbver Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- usbkd.usbver
api_type:
- NA
---

# !usbkd.usbver

The **!usbkd.usbver** command displays the USBD interface version of the USB driver stack.

```dbgcmd
!usbkd.usbver
```

## DLL

Usbkd.dll

## Remarks

The value of the USBD interface version is stored in the variable `usbport!usbd_version`.

## Examples

Here is an example of the output of **!usbkd.usbver**.

```dbgcmd
1: kd> !usbkd.usbver

USBD VER 600 USB stack is VISTA
```

## See also

[USB 2.0 Debugger Extensions](usb-2-0-extensions.md)

[Universal Serial Bus (USB) Drivers](../usbcon/index.md)

**USBD\_IsInterfaceVersionSupported**
