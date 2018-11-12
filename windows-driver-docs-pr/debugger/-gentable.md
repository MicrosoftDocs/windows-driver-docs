---
title: gentable
description: The gentable extension displays an RTL_GENERIC_TABLE.
ms.assetid: acf85ff8-9004-4c8e-b67f-20202c577aab
keywords: ["gentable Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- gentable
api_type:
- NA
ms.localizationpriority: medium
---

# !gentable


The **!gentable** extension displays an RTL\_GENERIC\_TABLE.

Syntax

```dbgcmd
!gentable Address[Flag]
```

## <span id="ddk__gentable_dbg"></span><span id="DDK__GENTABLE_DBG"></span>Parameters


<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the address of the RTL\_GENERIC\_TABLE.

<span id="_______Flag______"></span><span id="_______flag______"></span><span id="_______FLAG______"></span> *Flag*   
Specifies the table source. If *Flag* is 1, the AVL table is used. If *Flag* is 0 or omitted, the non-AVL table is used.

### <span id="DLL"></span><span id="dll"></span>DLL

Kdexts.dll

 

 





