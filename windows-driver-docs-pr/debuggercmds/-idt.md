---
title: "!idt (WinDbg)"
description: "The !idt extension displays the interrupt service routines (ISRs) for a specified interrupt dispatch table (IDT)."
keywords: ["ISR (interrupt service routine)", "IDT (interrupt dispatch table)", "!idt Windows Debugging"]
ms.date: 05/13/2020
topic_type:
- apiref
ms.topic: reference
api_name:
- idt
api_type:
- NA
---

# !idt


The **!idt** extension displays the interrupt service routines (ISRs) for a specified interrupt dispatch table (IDT).

```dbgcmd
!idt IDT 
!idt [-a] 
!idt -? 
```

## Parameters


<span id="_______IDT______"></span><span id="_______idt______"></span> *IDT*   
Specifies the IDT to display.

<span id="_______-a______"></span><span id="_______-A______"></span> **-a**   
When *IDT* is not specified, the debugger displays the IDTs of all processors on the target computer in an abbreviated format. If **-a** is specified, the ISRs for each IDT are also displayed.

<span id="_______-_______"></span> **-?**   
Displays help for this extension in the Debugger Command window.

## DLL

Kdexts.dll

This extension command can only be used with an x64-based or x86-based target computer.

## Additional Information

For information about ISRs and IDTs, see the Windows Driver Kit (WDK) documentation and *Microsoft Windows Internals* by Mark Russinovich and David Solomon.

## Remarks

Here is an example of the output from this extension:

```dbgcmd
0: kd> !idt

Dumping IDT:

37:806ba78c hal!PicSpuriousService37
3d:806bbc90 hal!HalpApcInterrupt
41:806bbb04 hal!HalpDispatchInterrupt
50:806ba864 hal!HalpApicRebootService
63:8641376c VIDEOPRT!pVideoPortInterrupt (KINTERRUPT 86413730)
73:862aa044 portcls!CInterruptSyncServiceRoutine (KINTERRUPT 862aa008)
82:86594314 atapi!IdePortInterrupt (KINTERRUPT 865942d8)
83:86591bec SCSIPORT!ScsiPortInterrupt (KINTERRUPT 86591bb0)
92:862b53dc serial!SerialCIsrSw (KINTERRUPT 862b53a0)
93:86435844 i8042prt!I8042KeyboardInterruptService (KINTERRUPT 86435808)
a3:863b366c i8042prt!I8042MouseInterruptService (KINTERRUPT 863b3630)
a4:8636bbec USBPORT!USBPORT_InterruptService (KINTERRUPT 8636bbb0)
b1:86585bec ACPI!ACPIInterruptServiceRoutine (KINTERRUPT 86585bb0)
b2:863c0524 serial!SerialCIsrSw (KINTERRUPT 863c04e8)
b4:86391a54 NDIS!ndisMIsr (KINTERRUPT 86391a18)
         USBPORT!USBPORT_InterruptService (KINTERRUPT 863ae890)
c1:806ba9d0 hal!HalpBroadcastCallService
d1:806b9dd4 hal!HalpClockInterrupt
e1:806baf30 hal!HalpIpiHandler
e3:806baca8 hal!HalpLocalApicErrorService
fd:806bb460 hal!HalpProfileInterrupt
```

