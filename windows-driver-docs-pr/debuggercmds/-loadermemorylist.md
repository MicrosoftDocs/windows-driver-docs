---
title: "!loadermemorylist"
description: "The !loadermemorylist extension displays the memory allocation list that the Windows boot loader passes to Windows."
keywords: ["OSLOADER", "!loadermemorylist Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- loadermemorylist
api_type:
- NA
---

# !loadermemorylist

The **!loadermemorylist** extension displays the memory allocation list that the Windows boot loader passes to Windows.

```dbgcmd
!loadermemorylist ListHeadAddress
```

## Parameters

<span id="_______ListHeadAddress______"></span><span id="_______listheadaddress______"></span><span id="_______LISTHEADADDRESS______"></span> *ListHeadAddress*   
Specifies the address of a list header.

## DLL

Kdexts.dll

## Remarks

This extension is designed to be used at the beginning of the system boot process while Ntldr is running. It displays a memory allocation list that includes the start, end, and type of each page range.

You can stop execution at any point by pressing CTRL+BREAK (in WinDbg) or CTRL+C (in KD).
