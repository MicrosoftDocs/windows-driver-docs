---
title: pte2va (WinDbg)
description: The pte2va extension displays the virtual address that corresponds to the specified page table entry (PTE).
keywords: ["pte2va Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- pte2va
api_type:
- NA
---

# !pte2va


The **!pte2va** extension displays the virtual address that corresponds to the specified page table entry (PTE).

```dbgcmd
!pte2va Address
```

## Parameters


<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the PTE.

## DLL

Windows XP and later - Kdexts.dll

 

### Additional Information

For information about page tables and PTEs, see *Microsoft Windows Internals*, by Mark Russinovich and David Solomon. 

## Remarks

To examine the contents of a specific PTE, use the [**!pte**](-pte.md) extension.

Here is an example of the output from the **!pte2va** extension:

```dbgcmd
kd> !pte2va 9230
000800000248c000 
```

 

 





