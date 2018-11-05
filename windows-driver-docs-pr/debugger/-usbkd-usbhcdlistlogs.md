---
title: usbkd.usbhcdlistlogs
description: The usbkd.usbhcdlistlogs command displays a list of all functional device objects (FDOs) associated with the USB port driver (Usbport.sys) and debug logs.
ms.assetid: C86646D3-7B39-4C8C-9FDA-FD07AA7A880A
keywords: ["usbkd.usbhcdlistlogs Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- usbkd.usbhcdlistlogs
api_type:
- NA
ms.localizationpriority: medium
---

# !usbkd.usbhcdlistlogs


The **!usbkd.usbhcdlistlogs** command displays a list of all functional device objects (FDOs) associated with the USB port driver (Usbport.sys). The command also displays the complete debug logs for all EHCI Host Controllers.

```dbgcmd
!usbkd.usbhcdlistlogs
```

## <span id="DLL"></span><span id="dll"></span>DLL


Usbkd.dll

Examples
--------

This example shows a portion of the output of the **!usbhcdlistlogs** command.

```dbgcmd
0: kd> !usbkd.usbhcdlistlogs

MINIPORT List @ fffff80001e5bbd0
*flink, blink ffffe00001f48018,ffffe00001f48bd8

[0] entry @: ffffe00001f48010 dt usbport!_USBPORT_MINIPORT_DRIVER ffffe00001f48010
UHCI MINIPORT @ ffffe00001f48010 !drvobj ffffe00002000060 regpkt ffffe00001f48048
02. !devobj ffffe00001ca4050 !usbhcdext ffffe00001ca41a0  HFDO 8086 2938  RHPDO ffffe0000213a050
03. !devobj ffffe00001ca7050 !usbhcdext ffffe00001ca71a0  HFDO 8086 2937  RHPDO ffffe00002140050

[1] entry @: ffffe00001f48bd0 dt usbport!_USBPORT_MINIPORT_DRIVER ffffe00001f48bd0
EHCI MINIPORT @ ffffe00001f48bd0 !drvobj ffffe00001fd33a0 regpkt ffffe00001f48c08
01. !devobj ffffe00001ca1050 !usbhcdext ffffe00001ca11a0  HFDO 8086 293c  RHPDO ffffe0000213c050

LOG@: ffffe00001ca11b8 
>LOG mask = 3ff idx = fff69e8d (28d)
*LOG: ffffe000020191a0  LOGSTART: ffffe00002014000 *LOGEND: ffffe0000201bfe0 # -1 
[ 000] ffffe000020191a0 Tmt0 0000000000000000 0000000000000000 0000000000000000 
[ 001] ffffe000020191c0 _Pop 0000000000000003 0000000000003000 0000000000000000 
...
[ 005] ffffe00002019240 chgZ 0000000000000000 0000000000b7228f 0000000000000000 
[ 006] ffffe00002019260 nes- 0000000000000000 0000000000000000 0000000000000000 
[ 007] ffffe00002019280 nes+ ffffe00001ca2370 ffffe00001ca2370 00000000000ced39 
...
[1014] ffffe00002019060 tmo4 0000000000000000 0000000000000040 ffffe00001ca1c20 
...
[1022] ffffe00002019160 xdw2 ffffe00001ca1b88 ffffe00001ca1050 0000000000000002 
[1023] ffffe00002019180 xdB0 ffffe00001ca1b88 ffffe00001ca1050 0000000000000000 
```

The command output shows two FDOs that represent UHCI host controlers and one FDO that represents an EHCI host controller. Then the output shows the debug log for the one EHCI host controller.

## <span id="see_also"></span>See also


[USB 2.0 Debugger Extensions](usb-2-0-extensions.md)

[Universal Serial Bus (USB) Drivers](https://go.microsoft.com/fwlink/p?LinkID=227351)

 

 






