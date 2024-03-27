---
title: "!amli dh (WinDbg)"
description: "The !amli dh extension displays the AML interpreter's internal heap block."
keywords: ["!amli dh Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- amli dh
api_type:
- NA
---

# !amli dh

The **!amli dh** extension displays the AML interpreter's internal heap block.

Syntax

```dbgcmd
!amli dh [HeapAddress]
```

## Parameters

<span id="_______HeapAddress______"></span><span id="_______heapaddress______"></span><span id="_______HEAPADDRESS______"></span> *HeapAddress*   
Specifies the address of the heap block. If this is omitted, the global heap is displayed.

## DLL

Kdexts.dll

### Additional Information

For information about related commands and their uses, see [The AMLI Debugger](../debugger/the-amli-debugger.md).
