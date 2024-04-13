---
title: "!gentable (WinDbg)"
description: "The !gentable extension displays an RTL_GENERIC_TABLE."
keywords: ["!gentable Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- gentable
api_type:
- NA
---

# !gentable

The **!gentable** extension displays an RTL\_GENERIC\_TABLE.

Syntax

```dbgcmd
!gentable Address[Flag]
```

## Parameters

<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the address of the RTL\_GENERIC\_TABLE.

<span id="_______Flag______"></span><span id="_______flag______"></span><span id="_______FLAG______"></span> *Flag*   
Specifies the table source. If *Flag* is 1, the AVL table is used. If *Flag* is 0 or omitted, the non-AVL table is used.

## DLL

Kdexts.dll
