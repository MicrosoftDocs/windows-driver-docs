---
title: usbkd._ehciqh
description: The usbkd._ehciqh command displays information from a usbehci _HCD_QUEUEHEAD_DESCRIPTOR structure. 
ms.assetid: 52A1CF03-3B1D-4CC6-A4DD-3E73A7AB2F00
keywords: ["usbkd._ehciqh Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- usbkd._ehciqh
api_type:
- NA
ms.localizationpriority: medium
---

# !usbkd.\_ehciqh


The **!usbkd.\_ehciqh** command displays information from a **usbehci!\_HCD\_QUEUEHEAD\_DESCRIPTOR** structure. Use this command to display information about asynchronous endpoints (that is, control and bulk endpoints).

```dbgcmd
!usbkd._ehciqh StructAddr
```

## <span id="ddk__devobj_dbg"></span><span id="DDK__DEVOBJ_DBG"></span>Parameters


<span id="_______StructAddr______"></span><span id="_______structaddr______"></span><span id="_______STRUCTADDR______"></span> *StructAddr*   
Address of a **usbehci!\_HCD\_QUEUEHEAD\_DESCRIPTOR** structure.

## <span id="DLL"></span><span id="dll"></span>DLL


Usbkd.dll

## <span id="see_also"></span>See also


[USB 2.0 Debugger Extensions](usb-2-0-extensions.md)

[Universal Serial Bus (USB) Drivers](https://go.microsoft.com/fwlink/p?LinkID=227351)

 

 






