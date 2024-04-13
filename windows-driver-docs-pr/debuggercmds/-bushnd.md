---
title: "!bushnd (WinDbg)"
description: "The !bushnd extension displays a HAL BUS_HANDLER structure."
keywords: ["!bushnd Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- bushnd
api_type:
- NA
---

# !bushnd


The **!bushnd** extension displays a HAL BUS\_HANDLER structure.

```dbgsyntax
    !bushnd [Address] 
```

## <span id="ddk__bushnd_dbg"></span><span id="DDK__BUSHND_DBG"></span>Parameters


<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the hexadecimal address of the HAL BUS\_HANDLER structure. If omitted, **!bushnd** displays a list of buses and the base address of the handler.

### DLL

Kdexts.dll

 

