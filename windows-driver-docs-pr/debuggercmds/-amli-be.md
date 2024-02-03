---
title: "!amli be (WinDbg)"
description: "The !amli be extension enables an AML breakpoint."
keywords: ["!amli be Windows Debugging"]
ms.date: 09/17/2018
topic_type:
- apiref
ms.topic: reference
api_name:
- amli be
api_type:
- NA
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

<span id="______________"></span> **\***
Specifies that all breakpoints should be enabled.

## DLL

Kdexts.dll

### Additional Information

For information about related commands and their uses, see [The AMLI Debugger](../debugger/the-amli-debugger.md).

## Remarks

All breakpoints are enabled when they are created. Breakpoints are only disabled if you have used the [**!amli bd**](-amli-bd.md) extension.

To determine the breakpoint number of a breakpoint, use the [**!amli bl**](-amli-bl.md) extension.
