---
title: "!usbkd.usbportmddcontext"
description: "The !usbkd.usbportmddcontext command displays USBPORT context data if it is present in a crash dump that was generated as a result of Bug Check 0xFE."
keywords: ["!usbkd.usbportmddcontext Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- usbkd.usbportmddcontext
api_type:
- NA
---

# !usbkd.usbportmddcontext

The **!usbkd.usbportmddcontext** command displays USBPORT context data if it is present in a crash dump that was generated as a result of [**Bug Check 0xFE**](../debugger/bug-check-0xfe--bugcode-usb-driver.md).

```dbgcmd
!usbkd.usbportmddcontext
```

## DLL

Usbkd.dll

## Remarks

Use this command only when you are debugging a crash dump file that was generated as a result of [**Bug Check 0xFE: BUGCODE\_USB\_DRIVER**](../debugger/bug-check-0xfe--bugcode-usb-driver.md).

## See also

[USB 2.0 Debugger Extensions](usb-2-0-extensions.md)

[Universal Serial Bus (USB) Drivers](../usbcon/index.md)
