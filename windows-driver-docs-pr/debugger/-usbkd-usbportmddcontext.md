---
title: usbkd.usbportmddcontext
description: The usbkd.usbportmddcontext command displays USBPORT context data if it is present in a crash dump that was generated as a result of Bug Check 0xFE.
ms.assetid: 774C7EAE-A33E-49A6-956F-C0791134C221
keywords: ["usbkd.usbportmddcontext Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- usbkd.usbportmddcontext
api_type:
- NA
ms.localizationpriority: medium
---

# !usbkd.usbportmddcontext


The **!usbkd.usbportmddcontext** command displays USBPORT context data if it is present in a crash dump that was generated as a result of [**Bug Check 0xFE**](bug-check-0xfe--bugcode-usb-driver.md).

```dbgcmd
!usbkd.usbportmddcontext
```

## <span id="DLL"></span><span id="dll"></span>DLL


Usbkd.dll

Remarks
-------

Use this command only when you are debugging a crash dump file that was generated as a result of [**Bug Check 0xFE: BUGCODE\_USB\_DRIVER**](bug-check-0xfe--bugcode-usb-driver.md).

## <span id="see_also"></span>See also


[USB 2.0 Debugger Extensions](usb-2-0-extensions.md)

[Universal Serial Bus (USB) Drivers](https://go.microsoft.com/fwlink/p?LinkID=227351)

 

 






