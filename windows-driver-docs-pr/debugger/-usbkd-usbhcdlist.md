---
title: usbkd.usbhcdlist
description: The usbkd.usbhcdlist command displays information about all USB host controllers that are represented by the USB port driver (Usbport.sys). 
ms.assetid: 877A6361-0DB9-4089-AF85-BABFBED8C440
keywords: ["usbkd.usbhcdlist Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- usbkd.usbhcdlist
api_type:
- NA
ms.localizationpriority: medium
---

# !usbkd.usbhcdlist


The [**!usbkd.usbhcdlist**](https://msdn.microsoft.com/library/windows/hardware/dn367074) command displays information about all USB host controllers that are represented by the USB port driver (Usbport.sys). For information about the USB port driver and the associated miniport drivers, see [USB Driver Stack Architecture](https://go.microsoft.com/fwlink/p?LinkId=251983).

```dbgcmd
!usbkd.usbhcdlist
```

## <span id="DLL"></span><span id="dll"></span>DLL


Usbkd.dll

Examples
--------

Here is an example of a portion of the output of [**!usbhcdlist**](https://msdn.microsoft.com/library/windows/hardware/dn367074).

```dbgcmd
0: kd> !usbkd.usbhcdlist
MINIPORT List @ fffff80001e5bbd0

## List of UHCI controllers

!drvobj ffffe00002000060 dt USBPORT!_USBPORT_MINIPORT_DRIVER ffffe00001f48010 Registration Packet ffffe00001f48048

01
...

## List of EHCI controllers

!drvobj ffffe00001fd33a0 dt USBPORT!_USBPORT_MINIPORT_DRIVER ffffe00001f48bd0 Registration Packet ffffe00001f48c08

01. Xxxxx Corporation PCI: VendorID Xxxx DeviceID Xxxx RevisionId 0002
    !devobj ffffe00001ca1050
    !ehci_info ffffe00001ca11a0
    Operational Registers ffffd000228bf020
    Device Data ffffe00001ca2da0
    !usbhcdlog ffffe00001ca11a0
    nt!_KINTERRUPT ffffe000020abe78
    Device Capabilities ffffe00001ca135c
    Pending IRP's: 0, Transfers: 0 (Periodic(0), Async(0))
```

## <span id="see_also"></span>See also


[USB 2.0 Debugger Extensions](usb-2-0-extensions.md)

[Universal Serial Bus (USB) Drivers](https://go.microsoft.com/fwlink/p?LinkID=227351)

 

 






