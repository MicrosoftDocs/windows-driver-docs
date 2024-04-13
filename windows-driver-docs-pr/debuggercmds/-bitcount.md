---
title: "!bitcount (WinDbg)"
description: "The !bitcount extension counts the number of 1 bits in a memory range."
keywords: ["bitcount Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- bitcount
api_type:
- NA
---

# !bitcount

The **!bitcount** extension counts the number of "1" bits in a memory range.

```dbgcmd
!bitcount StartAddress TotalBits
```

## Parameters


<span id="_______StartAddress______"></span><span id="_______startaddress______"></span><span id="_______STARTADDRESS______"></span> *StartAddress*   
Specifies the starting address of the memory range whose "1" bits will be counted.

<span id="_______TotalBits______"></span><span id="_______totalbits______"></span><span id="_______TOTALBITS______"></span> *TotalBits*   
Specifies the size of the memory range, in bits.

<span id="_______-_______"></span> **-?**   
Displays some Help text for this extension in the [Debugger Command window](../debugger/debugger-command-window.md).

## DLL

Exts.dll

 

