---
title: nstree (WinDbg)
description: The nstree extension displays an ACPI namespace object and its children in the namespace tree.
keywords: ["nstree Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- nstree
api_type:
- NA
---

# !nstree


The **!nstree** extension displays an ACPI namespace object and its children in the namespace tree.

Syntax

```dbgcmd
!nstree [Address]
```

## <span id="ddk__nstree_dbg"></span><span id="DDK__NSTREE_DBG"></span>Parameters


<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the address of the namespace object. This object and the entire namespace tree subordinate to it will be displayed. If *Address* is omitted, the entire namespace tree is displayed.

### <span id="DLL"></span><span id="dll"></span>DLL

Kdexts.dll

### Additional Information

For more information, see [ACPI Debugging](../debugger/acpi-debugging.md).

## Remarks

This extension is equivalent to [**!amli dns /s**](-amli-dns.md).

 

 





