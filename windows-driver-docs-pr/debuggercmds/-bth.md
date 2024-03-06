---
title: bth (WinDbg)
description: The bth extension displays the Itanium-based branch traces history for the specified processor.
keywords: ["branch trace history", "bth Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- bth
api_type:
- NA
---

# !bth


The **!bth** extension displays the Itanium-based branch traces history for the specified processor.

```dbgcmd
!bth [Processor]
```

**Important**  This command has been deprecated in the Windows Debugger Version 10.0.14257 and later, and is no longer available.

 

## Parameters


<span id="_______Processor______"></span><span id="_______processor______"></span><span id="_______PROCESSOR______"></span> *Processor*   
Specifies a processor. If *Processor* is omitted, then the branch trace history for all of processors is displayed.

## DLL

Windows XP and later - Kdexts.dll

 

This extension command can only be used with an Itanium-based target computer.

 

 





