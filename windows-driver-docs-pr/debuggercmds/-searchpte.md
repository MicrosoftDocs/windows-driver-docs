---
title: searchpte (WinDbg)
description: The searchpte extension searches physical memory for the specified page frame number (PFN).
keywords: ["searchpte Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- searchpte
api_type:
- NA
---

# !searchpte


The **!searchpte** extension searches physical memory for the specified page frame number (PFN).

```dbgcmd
!searchpte PFN 
!searchpte -?
```

## Parameters


<span id="_______PFN______"></span><span id="_______pfn______"></span> *PFN*   
Specifies the PFN in hexadecimal format.

<span id="_______-_______"></span> **-?**   
Displays help for this extension in the Debugger Command window.

## DLL

Windows XP and later - Kdexts.dll

 

### Additional Information

For information about page tables and page directories, see *Microsoft Windows Internals*, by Mark Russinovich and David Solomon. 

## Remarks

To stop execution at any time, press CTRL+BREAK (in WinDbg) or CTRL+C (in KD).

 

 





