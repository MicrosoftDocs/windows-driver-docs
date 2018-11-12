---
title: usbkd.usbusb2ep
description: The usbkd.usbusb2ep command displays information from a usbport _USB2_EP structure.
ms.assetid: 0298D7A2-C121-4B09-8542-CCD10323D573
keywords: ["usbkd.usbusb2ep Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- usbkd.usbusb2ep
api_type:
- NA
ms.localizationpriority: medium
---

# !usbkd.usbusb2ep


The **!usbkd.usbusb2ep** command displays information from a **usbport!\_USB2\_EP** structure.

```dbgcmd
!usbkd.usbusb2ep StructAddr
```

## <span id="ddk__devobj_dbg"></span><span id="DDK__DEVOBJ_DBG"></span>Parameters


<span id="_______StructAddr______"></span><span id="_______structaddr______"></span><span id="_______STRUCTADDR______"></span> *StructAddr*   
Address of a **usbport!\_USB2\_EP** structure. To get the address of **usbport!\_USB2\_EP** structure, use [**!usbkd.usb2**](-usbkd-usb2.md).

## <span id="DLL"></span><span id="dll"></span>DLL


Usbkd.dll

## <span id="see_also"></span>See also


[USB 2.0 Debugger Extensions](usb-2-0-extensions.md)

[Universal Serial Bus (USB) Drivers](https://go.microsoft.com/fwlink/p?LinkID=227351)

 

 






