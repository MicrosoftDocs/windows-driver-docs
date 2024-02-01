---
title: filetime (WinDbg)
description: The filetime extension converts a 64-bit FILETIME structure into a human-readable time.
keywords: ["FILETIME", "filetime Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- filetime
api_type:
- NA
---

# !filetime


The **!filetime** extension converts a 64-bit FILETIME structure into a human-readable time.

```dbgcmd
!filetime Time
```

## Parameters


<span id="_______Time______"></span><span id="_______time______"></span><span id="_______TIME______"></span> *Time*   
Specifies a 64-bit FILETIME structure.

### DLL

Kdexts.dll

 

## Remarks

Here is an example of the output from this extension:

```dbgcmd
kd> !filetime 1c4730984712348
 7/26/2004 04:10:18.712 (Pacific Standard Time)
```

 

 





