---
title: pat (WinDbg)
description: The pat extension displays the Page Attribute Table (PAT) registers for the target processor.
keywords: ["PAT", "pat Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- pat
api_type:
- NA
---

# !pat


The **!pat** extension displays the Page Attribute Table (PAT) registers for the target processor.

```dbgcmd
!pat Flag 
!pat 
```

## Parameters


<span id="_______Flag______"></span><span id="_______flag______"></span><span id="_______FLAG______"></span> *Flag*   
If *Flag* is set, the debugger verifies that the PAT feature is present before the PAT is displayed.

### DLL

Kdexts.dll

 

This extension command can only be used with an x86-based target computer.

 

 





