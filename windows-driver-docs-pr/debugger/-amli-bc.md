---
title: amli bc
description: The amli bc extension permanently clears an AML breakpoint.
ms.assetid: e975ee10-cd2f-4944-8d00-b2eda2dd099a
keywords: ["amli bc Windows Debugging"]
ms.author: domars
ms.date: 09/17/2018
topic_type:
- apiref
api_name:
- amli bc
api_type:
- NA
ms.localizationpriority: medium
---

# !amli bc


The **!amli bc** extension permanently clears an AML breakpoint.

Syntax

```dbgcmd
    !amli bc Breakpoint 
    !amli bc *
```

## <span id="ddk__amli_bc_dbg"></span><span id="DDK__AMLI_BC_DBG"></span>Parameters


<span id="_______Breakpoint______"></span><span id="_______breakpoint______"></span><span id="_______BREAKPOINT______"></span> *Breakpoint*   
Specifies the number of the breakpoint to be cleared.

<span id="______________"></span> **\\***   
Specifies that all breakpoints should be cleared.

### <span id="DLL"></span><span id="dll"></span>DLL

Kdexts.dll

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For information about related commands and their uses, see [The AMLI Debugger](the-amli-debugger.md).

Remarks
-------

To determine the breakpoint number of a breakpoint, use the [**!amli bl**](-amli-bl.md) extension.

 

 





