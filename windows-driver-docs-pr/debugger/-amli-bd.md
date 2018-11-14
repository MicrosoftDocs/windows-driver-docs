---
title: amli bd
description: The amli bd extension temporarily disables an AML breakpoint.
ms.assetid: a7fb4f51-8984-425b-858d-1e1e69825891
keywords: ["amli bd Windows Debugging"]
ms.author: domars
ms.date: 09/17/2018
topic_type:
- apiref
api_name:
- amli bd
api_type:
- NA
ms.localizationpriority: medium
---

# !amli bd


The **!amli bd** extension temporarily disables an AML breakpoint.

Syntax

```dbgcmd
    !amli bd Breakpoint!amli bd *
```

## <span id="ddk__amli_bd_dbg"></span><span id="DDK__AMLI_BD_DBG"></span>Parameters


<span id="_______Breakpoint______"></span><span id="_______breakpoint______"></span><span id="_______BREAKPOINT______"></span> *Breakpoint*   
Specifies the number of the breakpoint to be disabled.

<span id="______________"></span> **\\***   
Specifies that all breakpoints should be disabled.

### <span id="DLL"></span><span id="dll"></span>DLL

Kdexts.dll

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For information about related commands and their uses, see [The AMLI Debugger](the-amli-debugger.md).

Remarks
-------

A disabled breakpoint can be re-enabled by using the [**!amli be**](-amli-be.md) extension.

To determine the breakpoint number of a breakpoint, use the [**!amli bl**](-amli-bl.md) extension.

Here is an example of this command:

```console
kd> !amli bl
 0:  c29accf5 [\_WAK]
 1:  c29c20a5 [\_SB.PCI0.ISA.BAT1._BST]

kd> !amli bd 1
```

 

 





