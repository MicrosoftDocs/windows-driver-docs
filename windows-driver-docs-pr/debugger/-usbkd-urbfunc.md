---
title: usbkd.urbfunc
description: The usbkd.urbfunc command displays the name of a URB function code.
ms.assetid: 111DD6CD-D7DB-4772-B6DD-8EA88587FD1F
keywords: ["usbkd.urbfunc Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- usbkd.urbfunc
api_type:
- NA
ms.localizationpriority: medium
---

# !usbkd.urbfunc


The **!usbkd.urbfunc** command displays the name of a URB function code.

```dbgcmd
!usbkd.urbfunc FunctionCode
```

## <span id="ddk__devobj_dbg"></span><span id="DDK__DEVOBJ_DBG"></span>Parameters


<span id="_______FunctionCode______"></span><span id="_______functioncode______"></span><span id="_______FUNCTIONCODE______"></span> *FunctionCode*   
The hexadecimal value of a URB function code. These codes are defined in usb.h.

## <span id="DLL"></span><span id="dll"></span>DLL


Usbkd.dll

Examples
--------

Here is an example of the output of **!urbfunc**.

```dbgcmd
0: kd> !usbkd.urbfunc 0xA

URB_FUNCTION_ISOCH_TRANSFER (0xA)
```

## <span id="see_also"></span>See also


[USB 2.0 Debugger Extensions](usb-2-0-extensions.md)

[Universal Serial Bus (USB) Drivers](https://go.microsoft.com/fwlink/p?LinkID=227351)

 

 






