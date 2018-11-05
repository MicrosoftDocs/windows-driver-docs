---
title: usbkd.usbtx
description: The usbkd.usbtx command displays information from a usbport _HCD_TRANSFER_CONTEXT structure.
ms.assetid: 603AD207-69D5-4DED-80B5-ADA21E191D47
keywords: ["usbkd.usbtx Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- usbkd.usbtx
api_type:
- NA
ms.localizationpriority: medium
---

# !usbkd.usbtx


The **!usbkd.usbtx** command displays information from a **usbport!\_HCD\_TRANSFER\_CONTEXT** structure.

```dbgcmd
!usbkd.usbtx StructAddr
```

## <span id="ddk__devobj_dbg"></span><span id="DDK__DEVOBJ_DBG"></span>Parameters


<span id="_______StructAddr______"></span><span id="_______structaddr______"></span><span id="_______STRUCTADDR______"></span> *StructAddr*   
Address of a **usbport!\_HCD\_TRANSFER\_CONTEXT** structure. To get the transfer list for a USB host controller, use the [**!usbkd.usbhcdext**](-usbkd-usbhcdext.md) command.

## <span id="DLL"></span><span id="dll"></span>DLL


Usbkd.dll

Examples
--------

Here is one way to find the address of a **usbport!\_HCD\_TRANSFER\_CONTEXT** structure. First enter [**!usbkd.usb2tree**](-usbkd-usb2tree.md).

```dbgcmd
0: kd> !usbkd.usb2tree
...
4)!uhci_info ffffe00001c8f1a0 !devobj ffffe00001c8f050 PCI: VendorId 8086 DeviceId 2938 RevisionId 0002 
...
```

In the preceding output, the address of the device extension of the FDO is displayed as the argument of the [DML](debugger-markup-language-commands.md) command **!uhci\_info ffffe00001c8f1a0**.

Either click the DML command or pass the address of the device extension to [**!usbhcdext**](https://msdn.microsoft.com/library/windows/hardware/dn367072) to get the transfer list.

```dbgcmd
0: kd> !usbkd.usbhcdext ffffe00001c8f1a0
...
## I/O TRANSFER LIST(s)

1.) Transfer Request Priority List: (TxQueued) Type: 0-NotSplit, 1-Parent, 2-Child
    --------------------------------------------------------------------------------
    [000]!usbtx ffffe0000653401c !usbep ffffe00004730c60 !irp ffffe00004221220 State: (7)TX_Mapped_inMp
        Priority: 0, Type: 0, Flags= 0000000a, SequenceNum: 10, SplitIdx: 0
        InLen: 4096, OutLen: 0 Status: USBD_STATUS_PENDING (0x40000000)
    ...
```

In the preceding output, `ffffe0000653401c` is the address of an **\_HCD\_TRANSFER\_CONTEXT**structure. Pass this address to **!usbtx**.

```dbgcmd
0: kd> !usbkd.usbtx ffffe0000653401c

dt usbport!_HCD_TRANSFER_CONTEXT ffffe0000653401c
dt usbport!_TRANSFER_PARAMETERS ffffe0000653417c

## TX HISTORY

## EVENT, STATE, NEXT (latest at bottom)

[01]    (23)Ev_TX_Icsq, (0)TX_Undefined, (1)TX_InQueue
[02]    (5)Ev_TX_MapTransfer, (1)TX_InQueue, (2)TX_MapPending
[03]    (7)Ev_TX_MpSubmitSuccess, (2)TX_MapPending, (7)TX_Mapped_inMp

**DMA**
dt usbport!_TRANSFER_SG_LIST ffffe0000653439c
SgCount:  1  MdlVirtualAddress: ffffe00000437000  MdlSystemAddress: ffffe00000437000
    [0] dt usbport!_TRANSFER_SG_ENTRY ffffe000065343bc
    : sysaddr: 0000000000000000 len 0x00001000(4096) offset 0x00000000(0) phys 00000000'ded90000
---
dt usbport!_SCATTER_GATHER_ENTRY ffffe000065343ec
dt _SCATTER_GATHER_LIST ffffe00001bc231c
NumberOfElements = 1
    [0] dt _SCATTER_GATHER_ELEMENT ffffe00001bc232c
     :phys 00000000'ded90000 len 0x00001000(4096)
```

## <span id="see_also"></span>See also


[USB 2.0 Debugger Extensions](usb-2-0-extensions.md)

[Universal Serial Bus (USB) Drivers](https://go.microsoft.com/fwlink/p?LinkID=227351)

 

 






