---
title: usbkd.usbdpc
description: The usbkd.usbdpc command displays information stored in an _XDPC_CONTEXT structure.
ms.assetid: 51ED1BB0-416B-4B2B-9F4D-61F841224126
keywords: ["usbkd.usbdpc Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- usbkd.usbdpc
api_type:
- NA
ms.localizationpriority: medium
---

# !usbkd.usbdpc


The **!usbkd.usbdpc** command displays information stored in an **\_XDPC\_CONTEXT** structure.

```dbgcmd
!usbkd.usbdpc StructAddr
```

## <span id="ddk__devobj_dbg"></span><span id="DDK__DEVOBJ_DBG"></span>Parameters


<span id="_______StructAddr______"></span><span id="_______structaddr______"></span><span id="_______STRUCTADDR______"></span> *StructAddr*   
Address of a **usbport!\_XDPC\_CONTEXT** structure. To get the XDPC list for a USB host controller, use the [**!usbkd.usbhcdext**](-usbkd-usbhcdext.md) command.

## <span id="DLL"></span><span id="dll"></span>DLL


Usbkd.dll

Examples
--------

Here is one way to find the address of a **usbport!\_XDPC\_CONTEXT** structure. First enter [**!usbkd.usb2tree**](-usbkd-usb2tree.md).

```dbgcmd
0: kd> !usbkd.usb2tree
...
UHCI MINIPORT(s) dt usbport!_USBPORT_MINIPORT_DRIVER ffffe00001e77010
...
4)!uhci_info ffffe00001c7d1a0 !devobj ffffe00001c7d050 PCI: VendorId...
...
```

In the preceding output, the address of the device extension of the FDO is displayed as the argument of the [DML](debugger-markup-language-commands.md) command **!uhci\_info ffffe00001c7d1a0**.

Either click the DML command or pass the address of the device extension to [**!usbhcdext**](https://msdn.microsoft.com/library/windows/hardware/dn367072) to get the XDPC list.

```dbgcmd
0: kd> !usbkd.usbhcdext ffffe00001c7d1a0
...
## XDPC List

01) dt USBPORT!_XDPC_CONTEXT ffffe00001c7df18
02) dt USBPORT!_XDPC_CONTEXT ffffe00001c7db88
03) dt USBPORT!_XDPC_CONTEXT ffffe00001c7dd50
04) dt USBPORT!_XDPC_CONTEXT ffffe00001c7e0e0
...
```

In the preceding output, `ffffe00001c7df18` is the address of an **\_XDPC\_CONTEXT** structure. Pass this address to **!usbdpc**.

```dbgcmd
0: kd> !usbkd.usbdpc ffffe00001c7df18

dt USBPORT!_XDPC_CONTEXT ffffe00001c7df18

## XDPC HISTORY (latest at boottom)

##      EVENT                STATE                   NEXT

[01] Ev_Xdpc_End          XDPC_Running            XDPC_Enabled            
[02] Ev_Xdpc_Signal       XDPC_Enabled            XDPC_DpcQueued          
[03] Ev_Xdpc_Signal       XDPC_DpcQueued          XDPC_DpcQueued          
[04] Ev_Xdpc_Worker       XDPC_DpcQueued          XDPC_Running            
[05] Ev_Xdpc_Signal       XDPC_Running            XDPC_Signaled           
[06] Ev_Xdpc_End          XDPC_Signaled           XDPC_DpcQueued          
[07] Ev_Xdpc_Worker       XDPC_DpcQueued          XDPC_Running            
[08] Ev_Xdpc_End          XDPC_Running            XDPC_Enabled
```

## <span id="see_also"></span>See also


[USB 2.0 Debugger Extensions](usb-2-0-extensions.md)

[Universal Serial Bus (USB) Drivers](https://go.microsoft.com/fwlink/p?LinkID=227351)

 

 






