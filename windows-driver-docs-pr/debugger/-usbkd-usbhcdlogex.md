---
title: usbkd.usbhcdlogex
description: The usbkd.usbhcdlogex command displays an annotated debug log for a USB host controller.
ms.assetid: 47274AEE-0BDB-4C25-9158-6213366434E0
keywords: ["usbkd.usbhcdlogex Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- usbkd.usbhcdlogex
api_type:
- NA
ms.localizationpriority: medium
---

# !usbkd.usbhcdlogex


The **!usbkd.usbhcdlogex** command displays an annotated debug log for a USB host controller.

```dbgcmd
!usbkd.usbhcdlogex DeviceExtension[, NumberOfEntries]
```

## <span id="ddk__devobj_dbg"></span><span id="DDK__DEVOBJ_DBG"></span>Parameters


<span id="_______DeviceExtension______"></span><span id="_______deviceextension______"></span><span id="_______DEVICEEXTENSION______"></span> *DeviceExtension*   
Address of the device extension for the functional device object (FDO) of a UHCI or EHCI USB host controller.

<span id="_______NumberOfEntries______"></span><span id="_______numberofentries______"></span><span id="_______NUMBEROFENTRIES______"></span> *NumberOfEntries*   
The number of log entries to display. To display the entire log, set this parameter to -1.

## <span id="DLL"></span><span id="dll"></span>DLL


Usbkd.dll

Examples
--------

Here is one way to find the address of the device extension for the FDO of a USB host controller. First enter [**!usbkd.usb2tree**](-usbkd-usb2tree.md).

```dbgcmd
0 kd> !usbkd.usb2tree

EHCI MINIPORT(s) dt usbport!_USBPORT_MINIPORT_DRIVER ffffe00001f48bd0
...

2)!ehci_info ffffe00001ca11a0 !devobj ffffe00001ca1050 PCI: VendorId 8086 DeviceId 293c RevisionId 0002 
...
```

In the preceding output, the address of the device extension of the FDO is displayed as the argument of the [DML](debugger-markup-language-commands.md) command **!ehci\_info ffffe00001ca11a0**.

Now pass the address of the device extension to the **!usbhcdlogex** command. In this example, the second argument limits the display to 20 log entries.

```dbgcmd
0: kd> !usbkd.usbhcdlogex ffffe00001ca11a0, 20
LOG@: ffffe00001ca11b8 
>LOG mask = 3ff idx = fff68e95 (295)
*LOG: ffffe000020192a0  LOGSTART: ffffe00002014000 *LOGEND: ffffe0000201bfe0 # 20 
[ 000] ffffe000020192a0 xSt0 ffffe00001ca1b88 0000000000000006 0000000000000001 
[ 001] ffffe000020192c0 xnd8 ffffe00001ca1b88 ffffe00001ca1050 0000000000000000 
[ 002] ffffe000020192e0 xnd0 ffffe00001ca1b88 ffffe00001ca1050 0000000000000000 
//
// USBPORT_Xdpc_End()    - USBPORT_Core_UsbHcIntDpc_Worker() DPC/XDPC: 2 of 4

[ 003] ffffe00002019300 gNX0 0000000000000000 0000000000000000 ffffe00001ca1b88 
[ 004] ffffe00002019320 xbg1 ffffe00001ca1b88 ffffe00001ca1050 0000000000000000 
[ 005] ffffe00002019340 xbg0 ffffe00001ca1b88 ffffe00001ca1050 ffffe00001ca22e8 
//
// USBPORT_Xdpc_iBegin() - USBPORT_Core_UsbHcIntDpc_Worker() DPC/XDPC: 2 of 4

[ 006] ffffe00002019360 tmo4 0000000000000000 0000000000000040 ffffe00001ca1c20 
[ 007] ffffe00002019380 tmo3 0000000000000000 0000000000989680 ffffe00001ca1c20 
[ 008] ffffe000020193a0 tmo2 0000000000000000 00000000000003e8 ffffe00001ca1c20 
[ 009] ffffe000020193c0 tmo1 0000000000000000 000000000002625a ffffe00001ca1c20 
[ 010] ffffe000020193e0 tmo0 00000000000003e8 ffffe00001ca1b88 ffffe00001ca1c20 
[ 011] ffffe00002019400 hci0 0000000000000000 0000000000000000 0000000000000000 
[ 012] ffffe00002019420 xSt0 ffffe00001ca1b88 0000000000000008 0000000000000003 
[ 013] ffffe00002019440 xdw4 ffffe00001ca1b88 0000000000000000 0000000000000000 
[ 014] ffffe00002019460 xdw2 ffffe00001ca1b88 ffffe00001ca1050 0000000000000002 
[ 015] ffffe00002019480 xdB0 ffffe00001ca1b88 ffffe00001ca1050 0000000000000000 
//
// USBPORT_Xdpc_Worker_HcIntDpc()  DPC/XDPC: 2 of 4

[ 016] ffffe000020194a0 iDP- 0000000000000000 0000000000b73e26 0000000000000000 
//
// USBPORT_IsrDpc() - Exit()

[ 017] ffffe000020194c0 xSt0 ffffe00001ca1b88 0000000000000007 0000000000000002 
[ 018] ffffe000020194e0 Xsi1 ffffe00001ca1b88 0000000000000000 0000000000000000 
//
// USBPORT_Xdpc_iSignal()- USBPORT_Core_UsbHcIntDpc_Worker() DPC/XDPC: 2 of 4

[ 019] ffffe00002019500 chgZ 0000000000000000 0000000000b73e26 0000000000000000 
```

## <span id="see_also"></span>See also


[USB 2.0 Debugger Extensions](usb-2-0-extensions.md)

[Universal Serial Bus (USB) Drivers](https://go.microsoft.com/fwlink/p?LinkID=227351)

 

 






