---
title: "!frozen (WinDbg)"
description: The frozen extension displays the state of each processor.
keywords: ["processor states", "frozen Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- frozen
api_type:
- NA
---

# !frozen

The **!frozen** extension displays the state of each processor.

```dbgcmd
!frozen
```

## DLL

Windows XP and later - Kdexts.dll

 

## Remarks

Here is an example of the output from this extension:

```dbgcmd
0: kd> !frozen
Processor states:
       0 : Current
       1 : Frozen
```

 

 





