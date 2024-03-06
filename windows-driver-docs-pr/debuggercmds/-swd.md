---
title: swd (WinDbg)
description: The swd extension displays the software watchdog timer states for the specified processor, including the deferred procedure call (DPC) and the watchdog timer states for threads.
keywords: ["watchdog timer", "swd Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- swd
api_type:
- NA
---

# !swd


The **!swd** extension displays the software watchdog timer states for the specified processor, including the deferred procedure call (DPC) and the watchdog timer states for threads.

```dbgcmd
!swd [Processor]
```

## Parameters


<span id="_______Processor______"></span><span id="_______processor______"></span><span id="_______PROCESSOR______"></span> *Processor*   
Specifies the processor. If *Processor* is omitted, information is displayed for all processors on the target computer.

## DLL

Windows XP and later - Kdexts.dll

 

## Remarks

The watchdog timer shuts down or restarts Windows if Windows stops responding. The times are displayed in seconds.

 

 





