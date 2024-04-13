---
title: "!usbkd.usbhubmddevext"
description: "The !usbkd.usbhubmddevext command displays a usbhub _DEVICE_EXTENSION_HUB structure if one is present in a crash dump that was generated as a result of a Bug Check 0xFE."
keywords: ["!usbkd.usbhubmddevext Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- usbkd.usbhubmddevext
api_type:
- NA
---

# !usbkd.usbhubmddevext

The **!usbkd.usbhubmddevext** command displays a **usbhub!\_DEVICE\_EXTENSION\_HUB** structure if one is present in a crash dump that was generated as a result of a [**Bug Check 0xFE**](../debugger/bug-check-0xfe--bugcode-usb-driver.md).

```dbgcmd
!usbkd.usbhubmddevext
```

## DLL

Usbkd.dll

## Remarks

Use this command only when you are debugging a crash dump file that was generated as a result of [**Bug Check 0xFE: BUGCODE\_USB\_DRIVER**](../debugger/bug-check-0xfe--bugcode-usb-driver.md).

## See also

[USB 2.0 Debugger Extensions](usb-2-0-extensions.md)

[Universal Serial Bus (USB) Drivers](../usbcon/index.md)
