---
title: "!ready (WinDbg)"
description: "!The ready extension displays summary information about each thread in the system in a READY state."
keywords: ["thread, ready threads", "!ready Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- ready
api_type:
- NA
---

# !ready

The **!ready** extension displays summary information about each thread in the system in a READY state.

```dbgcmd
!ready [Flags]
```

## Parameters

<span id="_______Flags______"></span><span id="_______flags______"></span><span id="_______FLAGS______"></span> *Flags*   
Specifies the level of detail to display. *Flags* can be any combination of the following bits. If *Flags* is 0, only a minimal amount of information is displayed. The default is 0x6.

<span id="Bit_1__0x2_"></span><span id="bit_1__0x2_"></span><span id="BIT_1__0X2_"></span>Bit 1 (0x2)  
Causes the display to include the thread's wait states.

<span id="Bit_2__0x4_"></span><span id="bit_2__0x4_"></span><span id="BIT_2__0X4_"></span>Bit 2 (0x4)  
If this is included without Bit 1 (0x2), this has no effect. If this is included along with Bit 1, the thread is displayed with a stack trace.

<span id="Bit_3__0x8_"></span><span id="bit_3__0x8_"></span><span id="BIT_3__0X8_"></span>Bit 3 (0x8)  
Causes the display of each function to include the return address and the stack pointer. The display of function arguments is suppressed.

<span id="Bit_4__0x10_"></span><span id="bit_4__0x10_"></span><span id="BIT_4__0X10_"></span>Bit 4 (0x10)  
Causes the display of each function to include only the return address; arguments and stack pointers are suppressed.

## DLL

Kdexts.dll

## Remarks

The output from this extension is similar to that of [**!thread**](-thread.md), except that only ready threads are displayed, and they are sorted in order of decreasing priority.

## Additional Information

For information about thread scheduling and the READY state, see *Microsoft Windows Internals*, by Mark Russinovich and David Solomon. 
