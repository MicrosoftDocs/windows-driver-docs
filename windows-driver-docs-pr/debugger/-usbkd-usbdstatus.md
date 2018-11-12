---
title: usbkd.usbdstatus
description: The usbkd.usbdstatus command displays the name of a USBD status code.
ms.assetid: 9983433E-1D17-47C6-972B-0A02B228A6AE
keywords: ["usbkd.usbdstatus Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- usbkd.usbdstatus
api_type:
- NA
ms.localizationpriority: medium
---

# !usbkd.usbdstatus


The **!usbkd.usbdstatus** command displays the name of a USBD status code.

```dbgcmd
!usbkd.usbdstatus StatusCode
```

## <span id="ddk__devobj_dbg"></span><span id="DDK__DEVOBJ_DBG"></span>Parameters


<span id="_______StatusCode______"></span><span id="_______statuscode______"></span><span id="_______STATUSCODE______"></span> *StatusCode*   
The hexadecimal value of a USBD status code. These codes are defined in usb.h.

## <span id="DLL"></span><span id="dll"></span>DLL


Usbkd.dll

Examples
--------

Here is an example of the output of **!usbdstatus**.

```dbgcmd
1: kd> !usbkd.usbdstatus 0xC0000008

USBD_STATUS_DATA_OVERRUN (0xC0000008)
```

## <span id="see_also"></span>See also


[USB 2.0 Debugger Extensions](usb-2-0-extensions.md)

[Universal Serial Bus (USB) Drivers](https://go.microsoft.com/fwlink/p?LinkID=227351)

 

 






