---
title: usbkd.usbhubmdpd
description: The usbkd.usbhubmdpd command displays a usbhub _HUB_PORT_DATA structure if one is present in a crash dump that was generated as a result of Bug Check 0xFE.
ms.assetid: 128D45A2-A891-42BC-9E3E-FCDC5B4504A2
keywords: ["usbkd.usbhubmdpd Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- usbkd.usbhubmdpd
api_type:
- NA
ms.localizationpriority: medium
---

# !usbkd.usbhubmdpd


The **!usbkd.usbhubmdpd** command displays a **usbhub!\_HUB\_PORT\_DATA** structure if one is present in a crash dump that was generated as a result of [**Bug Check 0xFE**](bug-check-0xfe--bugcode-usb-driver.md).

```dbgcmd
!usbkd.usbhubmdpd [PortNum]
```

## <span id="ddk__devobj_dbg"></span><span id="DDK__DEVOBJ_DBG"></span>Parameters


<span id="_______PortNum______"></span><span id="_______portnum______"></span><span id="_______PORTNUM______"></span> *PortNum*   
A USB port number. If you specify a port number, this command displays the structure (if one is present) that represents the specified port. If you do not specify a port number, this command displays the structure (if one is present) on which [**Bug Check 0xFE**](bug-check-0xfe--bugcode-usb-driver.md) was initiated.

## <span id="DLL"></span><span id="dll"></span>DLL


Usbkd.dll

Remarks
-------

Use this command only when you are debugging a crash dump file that was generated as a result of [**Bug Check 0xFE: BUGCODE\_USB\_DRIVER**](bug-check-0xfe--bugcode-usb-driver.md).

## <span id="see_also"></span>See also


[USB 2.0 Debugger Extensions](usb-2-0-extensions.md)

[Universal Serial Bus (USB) Drivers](https://go.microsoft.com/fwlink/p?LinkID=227351)

 

 






