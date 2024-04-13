---
title: "!usb3kd.usbdstatus"
description: "The !usb3kd.usbdstatus extension displays the name of a USBD status code."
keywords: ["!usb3kd.usbdstatus Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- usb3kd.usbdstatus
api_type:
- NA
---

# !usb3kd.usbdstatus

The [**!usb3kd.usbdstatus**](-usb3kd-device-info.md) extension displays the name of a USBD status code.

```dbgcmd
!usb3kd.ucx_usbdstatus UrbStatus
```

## Parameters

<span id="_______UsbdStatus______"></span><span id="_______usbdstatus______"></span><span id="_______USBDSTATUS______"></span> *UsbdStatus*   
The numeric value of a USBD status code.

## DLL

Usb3kd.dll

## Remarks

USBD status codes are defined in Usb.h.

## Examples

The following example passes the numeric value 0x80000200 to the **!usbdstatus** command. The command returns the name of the status code, USBD\_STATUS\_INVALID\_URB\_FUNCTION.

```dbgcmd
3: kd> !usbdstatus 0x80000200
USBD_STATUS_INVALID_URB_FUNCTION (0x80000200)
```

## See also

[USB 3.0 Extensions](usb-3-extensions.md)

[Universal Serial Bus (USB) Drivers](../usbcon/index.md)
