---
title: "!wdmaud (WinDbg)"
description: "!wdmaud is obsolete."
keywords: ["!wdmaud Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- wdmaud
api_type:
- NA
---

# !wdmaud

!wdmaud is obsolete.

```dbgcmd
!wdmaud Address Flags
```

## Parameters

<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the address of the structure to be displayed.

<span id="_______Flags______"></span><span id="_______flags______"></span><span id="_______FLAGS______"></span> *Flags*   
Specifies the information to display. This must include exactly one of the bits 0x1, 0x2, 0x4, and 0x8. The 0x100 bit can be added to any of these.

<span id="Bit_0__0x1_"></span><span id="bit_0__0x1_"></span><span id="BIT_0__0X1_"></span>Bit 0 (0x1)  
Displays a list of all IOCTLs that have been sent to wdmaud.sys. When this is used, *Address* should specify the address of the **WdmaIoctlHistoryListHead**. If the 0x100 bit is set, the display also includes the **pContext** that each IOCTL was sent with.

<span id="Bit_1__0x2_"></span><span id="bit_1__0x2_"></span><span id="BIT_1__0X2_"></span>Bit 1 (0x2)  
Displays a list of all IRPs that WDMAud has marked as pending. When this is used, *Address* should specify the address of the **WdmaPendingIrpListHead**. If the 0x100 bit is set, the display also includes the context on which each IRP was allocated.

<span id="Bit_2__0x4_"></span><span id="bit_2__0x4_"></span><span id="BIT_2__0X4_"></span>Bit 2 (0x4)  
Displays a list of all MDLs that WDMAud has allocated. When this is used, *Address* should specify the address of the **WdmaAllocatedMdlListHead**. If the 0x100 bit is set, the display also includes the context on which each MDL was allocated.

<span id="Bit_3__0x8_"></span><span id="bit_3__0x8_"></span><span id="BIT_3__0X8_"></span>Bit 3 (0x8)  
Displays a list of all active contexts attached to wdmaud.sys. When this is used, *Address* should specify the address of the **WdmaContextListHead**. If the 0x100 bit is set, the display also includes the data members of each context structure.

<span id="Bit_8__0x100_"></span><span id="bit_8__0x100_"></span><span id="BIT_8__0X100_"></span>Bit 8 (0x100)  
Causes the display to include verbose information.

## DLL

Windows XP and later - Unavailable

## Additional Information

For information about WDM audio architecture and audio drivers, see the Windows Driver Kit (WDK) documentation.

## Remarks

The contexts attached to wdmaud.sys (**pContext**) contain most of the state data for each device. Whenever wdmaud.drv is loaded into a new process, wdmaud.sys is notified of its arrival. Whenever wdmaud.drv is unloaded, wdmaud.sys cleans up any allocations made in that context.
