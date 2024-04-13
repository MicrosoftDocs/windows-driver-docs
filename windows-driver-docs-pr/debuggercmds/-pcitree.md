---
title: "!pcitree (WinDbg)"
description: "The !pcitree extension displays information about PCI device objects, including child PCI buses and CardBus buses, and the devices attached to them."
keywords: ["PCI bus", "PCI device", "!pcitree Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- pcitree
api_type:
- NA
---

# !pcitree

The **!pcitree** extension displays information about PCI device objects, including child PCI buses and CardBus buses, and the devices attached to them.

```dbgcmd
!pcitree
```

## DLL

Kdexts.dll

## Additional Information

See [Plug and Play Debugging](../debugger/plug-and-play-debugging.md) for applications of this extension command. For information about PCI buses and PCI device objects, see the Windows Driver Kit (WDK) documentation.

## Remarks

Here is an example:

```dbgcmd
kd> !pcitree

Bus 0x0 (FDO Ext fe517338)
  0600 12378086 (d=0,  f=0) devext fe4f4ee8 Bridge/HOST to PCI
  0601 70008086 (d=d,  f=0) devext fe4f4ce8 Bridge/PCI to ISA
  0101 70108086 (d=d,  f=1) devext fe4f4ae8 Mass Storage Controller/IDE
  0604 00211011 (d=e,  f=0) devext fe4f4788 Bridge/PCI to PCI

Bus 0x1 (FDO Ext fe516998)
  0200 905010b7 (d=8,  f=0) devext fe515ee8 Network Controller/Ethernet
  0100 81789004 (d=9,  f=0) devext fe515ce8 Mass Storage Controller/SCSI
  0300 0519102b (d=10, f=0) devext fe4f4428 Display Controller/VGA

Total PCI Root busses processed = 1
```

To understand this display, consider the final device shown. Its base class is 03, its subclass is 00, its Device ID is 0x0519, and its Vendor ID is 0x102B. These values are all intrinsic to the device itself.

The number after "d=" is the device number; the number after "f=" is the function number. After "devext" is the device extension address, 0xFE4F4428. Finally, the base class name and the subclass name appear.

To obtain more information about a device, use the [**!devext**](-devext.md) extension command with the device extension address as the argument. For this particular device, the command to use would be:

```dbgcmd
kd> !devext fe4f4428 pci 
```

If the **!pcitree** extension generates an error, this often means that your PCI symbols were not loaded properly. Use [**.reload pci.sys**](-reload--reload-module-.md) to fix this problem.
