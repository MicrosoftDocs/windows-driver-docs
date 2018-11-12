---
title: amli dh
description: The amli dh extension displays the AML interpreter's internal heap block.
ms.assetid: 52027a44-3308-4d9e-be66-8b45cdd88b3b
keywords: ["amli dh Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- amli dh
api_type:
- NA
ms.localizationpriority: medium
---

# !amli dh


The **!amli dh** extension displays the AML interpreter's internal heap block.

Syntax

```dbgcmd
!amli dh [HeapAddress]
```

## <span id="ddk__amli_dh_dbg"></span><span id="DDK__AMLI_DH_DBG"></span>Parameters


<span id="_______HeapAddress______"></span><span id="_______heapaddress______"></span><span id="_______HEAPADDRESS______"></span> *HeapAddress*   
Specifies the address of the heap block. If this is omitted, the global heap is displayed.

### <span id="DLL"></span><span id="dll"></span>DLL

Kdexts.dll

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For information about related commands and their uses, see [The AMLI Debugger](the-amli-debugger.md).

 

 





