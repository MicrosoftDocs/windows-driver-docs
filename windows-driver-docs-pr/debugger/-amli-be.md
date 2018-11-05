---
title: amli be
description: The amli be extension enables an AML breakpoint.
ms.assetid: 75c0c05f-8c56-4489-a798-2e5ec6ca26d8
keywords: ["amli be Windows Debugging"]
ms.author: domars
ms.date: 09/17/2018
topic_type:
- apiref
api_name:
- amli be
api_type:
- NA
ms.localizationpriority: medium
---

# !amli be


The **!amli be** extension enables an AML breakpoint.

Syntax

```dbgcmd
    !amli be Breakpoint!amli be *
```

## <span id="ddk__amli_be_dbg"></span><span id="DDK__AMLI_BE_DBG"></span>Parameters


<span id="_______Breakpoint______"></span><span id="_______breakpoint______"></span><span id="_______BREAKPOINT______"></span> *Breakpoint*   
Specifies the breakpoint number of the breakpoint to be enabled.

<span id="______________"></span> **\\***   
Specifies that all breakpoints should be enabled.

### <span id="DLL"></span><span id="dll"></span>DLL

Kdexts.dll

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For information about related commands and their uses, see [The AMLI Debugger](the-amli-debugger.md).

Remarks
-------

All breakpoints are enabled when they are created. Breakpoints are only disabled if you have used the [**!amli bd**](-amli-bd.md) extension.

To determine the breakpoint number of a breakpoint, use the [**!amli bl**](-amli-bl.md) extension.

 

 





