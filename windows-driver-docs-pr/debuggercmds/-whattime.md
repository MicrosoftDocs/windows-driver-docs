---
title: whattime (WinDbg)
description: The whattime extension converts a tick count into a standard time value.
keywords: ["tick count", "whattime Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- whattime
api_type:
- NA
---

# !whattime


The **!whattime** extension converts a tick count into a standard time value.

```dbgcmd
!whattime Ticks
```

## Parameters


<span id="_______Ticks______"></span><span id="_______ticks______"></span><span id="_______TICKS______"></span> *Ticks*   
The number of ticks.

## DLL

Windows XP and later - Kdexts.dll

 

## Remarks

The output is displayed as *HH:MM:SS.mmm*. Here is an example:

```dbgcmd
kd> !whattime 29857ae4
696613604 Ticks in Standard Time:  15:02:16.040s
```

 

 





