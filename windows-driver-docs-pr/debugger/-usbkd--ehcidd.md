---
title: usbkd._ehcidd
description: The usbkd._ehcidd command displays information from a usbehci _DEVICE_DATA structure.
ms.assetid: 8D594564-6506-44A8-A109-A76DA5AE7D89
keywords: ["usbkd._ehcidd Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- usbkd._ehcidd
api_type:
- NA
ms.localizationpriority: medium
---

# !usbkd.\_ehcidd


The **!usbkd.\_ehcidd** command displays information from a **usbehci!\_DEVICE\_DATA** structure.

```dbgcmd
!usbkd._ehcidd StructAddr
```

## <span id="ddk__devobj_dbg"></span><span id="DDK__DEVOBJ_DBG"></span>Parameters


<span id="_______StructAddr______"></span><span id="_______structaddr______"></span><span id="_______STRUCTADDR______"></span> *StructAddr*   
Address of a **usbehci!\_DEVICE\_DATA** structure. To find addresses of **usbehci!\_DEVICE\_DATA** structures, use [**!usbhcdext**](-usbkd-usbhcdext.md) or [**!usbhcdlist**](-usbkd-usbhcdlist.md).

## <span id="DLL"></span><span id="dll"></span>DLL


Usbkd.dll

Examples
--------

Here is one way to get the address of a **usbehci!\_DEVICE\_DATA** structure. First enter [**!usbkd.usbhcdlist**](-usbkd-usbhcdlist.md).

```dbgcmd
0: kd> !usbkd.usbhcdlist

MINIPORT List @ fffff80001e5bbd0

## List of EHCI controllers

!drvobj ffffe00001fd33a0 dt USBPORT!_USBPORT_MINIPORT_DRIVER ffffe00001f48bd0 Registration Packet ffffe00001f48c08

01. Xxxx Corporation PCI: VendorID Xxxx DeviceID Xxxx RevisionId 0002
    !devobj ffffe0000781a050
    !ehci_info ffffe0000781a1a0
    Operational Registers ffffd00021fb8420
    Device Data ffffe0000781bda0
    ...
```

In the preceding output, `ffffe0000781bda0` is the address of a **\_DEVICE\_DATA** structure.

Now pass the structure address to **!\_ehcidd**

```dbgcmd
0: kd> !usbkd._ehcidd ffffe0000781bda0

*USBEHCI DEVICE DATA ffffe0000781bda0
** dt usbehci!_DEVICE_DATA ffffe0000781bda0 

get_field_ulong ffffe0000781bda0 usbehci!_DEVICE_DATA Flags
*All Enpoints list:
head @ ffffe0000781bdb0 f_link ffffe0000781bdb0 b_link ffffe0000781bdb0
AsyncQueueHead ffffd00021cf5000 !_ehciqh ffffd00021cf5000
    PhysicalAddress: 0xde79a000
    NextQh: ffffd00021cf5000 Hlink de79a002
    PrevQh: ffffd00021cf5000
```

## <span id="see_also"></span>See also


[USB 2.0 Debugger Extensions](usb-2-0-extensions.md)

[Universal Serial Bus (USB) Drivers](https://go.microsoft.com/fwlink/p?LinkID=227351)

 

 






