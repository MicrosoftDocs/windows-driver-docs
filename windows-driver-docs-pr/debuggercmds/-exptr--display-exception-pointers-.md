---
title: .exptr (Display Exception Pointers)
description: The .exptr command displays an EXCEPTION_POINTERS structure.
keywords: [".exptr (Display Exception Pointers) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- .exptr (Display Exception Pointers)
api_type:
- NA
---

# .exptr (Display Exception Pointers)


The **.exptr** command displays an EXCEPTION\_POINTERS structure.

```dbgcmd
.exptr Address
```

## <span id="ddk_meta_display_exception_pointers_dbg"></span><span id="DDK_META_DISPLAY_EXCEPTION_POINTERS_DBG"></span>Parameters


<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the address of the EXCEPTION\_POINTERS structure.

### Environment

|  Item  | Description          |
|--------|----------------------|
|Modes   |User mode, kernel mode|
|Targets |Live, crash dump      |
|Platforms|All                  |

 

 

 





