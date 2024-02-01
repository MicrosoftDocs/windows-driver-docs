---
title: ipi (WinDbg)
description: The ipi extension displays the interprocessor interrupt (IPI) state for a specified processor.
keywords: ["IPI (interprocessor interrupt)", "ipi Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- ipi
api_type:
- NA
---

# !ipi


The **!ipi** extension displays the interprocessor interrupt (IPI) state for a specified processor.

```dbgcmd
!ipi [Processor]
```

## Parameters


<span id="_______Processor______"></span><span id="_______processor______"></span><span id="_______PROCESSOR______"></span> *Processor*   
Specifies a processor. If *Processor* is omitted, the IPI state for every processor is displayed.

## DLL

Windows XP and later - Kdexts.dll

 

This extension command can only be used with an x86-based target computer.

### Additional Information

For information about IPIs, see *Microsoft Windows Internals* by Mark Russinovich and David Solomon.

## Remarks

Here is an example of the output from this extension:

```dbgcmd
0: kd> !ipi
IPI State for Processor 0
  Worker Routine:  nt!KiFlushTargetMultipleTb [Stale]
  Parameter[0]:    0
  Parameter[1]:    3
  Parameter[2]:    F7C98770
  Ipi Trap Frame:  F7CCCCDC [.trap F7CCCCDC]
  Signal Done:     0
  IPI Frozen:      24 [FreezeActive] [Owner]
  Request Summary: 0
  Target Set:      0
  Packet Barrier:  0

IPI State for Processor 1
  Worker Routine:  nt!KiFlushTargetMultipleTb [Stale]
  Parameter[0]:    1
  Parameter[1]:    3
  Parameter[2]:    F7CDCD28
  Ipi Trap Frame:  F7C8CCC4 [.trap F7C8CCC4]
  Signal Done:     0
  IPI Frozen:      2 [Frozen]
  Request Summary: 0
  Target Set:      0
  Packet Barrier:  0
```

 

 





