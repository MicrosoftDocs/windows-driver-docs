---
title: usbkd._ehciframe
description: The usbkd._ehciframe command displays an EHCI miniport FrameListBaseAddress periodic list entry chain indexed by a frame number.
keywords: ["usbkd._ehciframe Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- usbkd._ehciframe
api_type:
- NA
---

# !usbkd.\_ehciframe


The **!usbkd.\_ehciframe** command displays an EHCI miniport FrameListBaseAddress periodic list entry chain indexed by a frame number.

```dbgcmd
!usbkd._ehciframe StructAddr, FrameNumber
```

## <span id="ddk__devobj_dbg"></span><span id="DDK__DEVOBJ_DBG"></span>Parameters


<span id="_______StructAddr______"></span><span id="_______structaddr______"></span><span id="_______STRUCTADDR______"></span> *StructAddr*   
Address of a **usbehci!\_DEVICE\_DATA** structure.

<span id="_______FrameNumber______"></span><span id="_______framenumber______"></span><span id="_______FRAMENUMBER______"></span> *FrameNumber*   
Frame number in the range 0 through 1023.

## <span id="DLL"></span><span id="dll"></span>DLL


Usbkd.dll

## <span id="see_also"></span>See also


[USB 2.0 Debugger Extensions](usb-2-0-extensions.md)

[Universal Serial Bus (USB) Drivers](../usbcon/index.md)

 

