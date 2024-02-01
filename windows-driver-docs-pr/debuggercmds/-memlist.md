---
title: memlist (WinDbg)
description: The memlist extension scans physical memory lists from the page frame number (PFN) database in order to check them for consistency.
keywords: ["PFN database", "memlist Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- memlist
api_type:
- NA
---

# !memlist

The **!memlist** extension scans physical memory lists from the page frame number (PFN) database in order to check them for consistency.

Syntax

`!memlist Flags`

## Parameters


<span id="_______Flags______"></span><span id="_______flags______"></span><span id="_______FLAGS______"></span> *Flags*   
Specifies which memory lists to verify. At present, only one value has been implemented:

<span id="Bit_0__0x1_"></span><span id="bit_0__0x1_"></span><span id="BIT_0__0X1_"></span>Bit 0 (0x1)  
Causes the zeroed pages list to be verified.

## DLL

Windows XP and later - Kdexts.dll

## Remarks

This extension will only check the zeroed pages list to make sure that all pages in that list are zeroed. The appropriate syntax is:

```dbgcmd
kd> !memlist 1
```
