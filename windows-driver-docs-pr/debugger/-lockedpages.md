---
title: lockedpages
description: The lockedpages extension displays driver-locked pages for a specified process.
keywords: ["driver-locked pages", "lockedpages Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- lockedpages
api_type:
- NA
ms.localizationpriority: medium
---

# !lockedpages


The **!lockedpages** extension displays driver-locked pages for a specified process.

Syntax

```dbgcmd
!lockedpages [Process]
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______Process______"></span><span id="_______process______"></span><span id="_______PROCESS______"></span> *Process*   
Specifies a process. If *Process* is omitted, the current process is used.

### <span id="DLL"></span><span id="dll"></span>DLL

Kdexts.dll

## Remarks

You can stop execution at any point by pressing CTRL+BREAK (in WinDbg) or CTRL+C (in KD).

 

 





