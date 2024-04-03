---
title: "!usbkd.usbdstatus"
description: "The !usbkd.usbdstatus command displays the name of a USBD status code."
keywords: ["!usbkd.usbdstatus Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- usbkd.usbdstatus
api_type:
- NA
---

# !usbkd.usbdstatus

The **!usbkd.usbdstatus** command displays the name of a USBD status code.

```dbgcmd
!usbkd.usbdstatus StatusCode
```

## Parameters

<span id="_______StatusCode______"></span><span id="_______statuscode______"></span><span id="_______STATUSCODE______"></span> *StatusCode*   
The hexadecimal value of a USBD status code. These codes are defined in usb.h.

## DLL

Usbkd.dll

## Examples

Here is an example of the output of **!usbdstatus**.

```dbgcmd
1: kd> !usbkd.usbdstatus 0xC0000008

USBD_STATUS_DATA_OVERRUN (0xC0000008)
```

## See also

[USB 2.0 Debugger Extensions](usb-2-0-extensions.md)

[Universal Serial Bus (USB) Drivers](../usbcon/index.md)
