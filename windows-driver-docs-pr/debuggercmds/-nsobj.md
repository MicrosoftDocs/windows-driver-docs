---
title: nsobj (WinDbg)
description: The nsobj extension displays an ACPI namespace object.
keywords: ["nsobj Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- nsobj
api_type:
- NA
---

# !nsobj


The **!nsobj** extension displays an ACPI namespace object.

Syntax

```dbgcmd
!nsobj [Address]
```

## <span id="ddk__nsobj_dbg"></span><span id="DDK__NSOBJ_DBG"></span>Parameters


<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the address of the namespace object. If this is omitted, the root of the namespace tree is used.

### <span id="DLL"></span><span id="dll"></span>DLL

Kdexts.dll

### Additional Information

For more information, see [ACPI Debugging](../debugger/acpi-debugging.md).

## Remarks

This extension is equivalent to [**!amli dns**](-amli-dns.md).

 

 





