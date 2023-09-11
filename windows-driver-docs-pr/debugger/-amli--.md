---
title: amli (WinDbg)
description: The amli extension displays some Help text in the Debugger Command window for the amli extension commands.
keywords: ["amli Windows Debugging"]
ms.date: 09/17/2018
topic_type:
- apiref
ms.topic: reference
api_name:
- amli
api_type:
- NA
---

# !amli ?


The **!amli ?** extension displays some Help text in the Debugger Command window for the **!amli** extension commands.

Syntax

```dbgcmd
    !amli ? [Command] 
```

## <span id="ddk__amli__dbg"></span><span id="DDK__AMLI__DBG"></span>Parameters


<span id="_______Command______"></span><span id="_______command______"></span><span id="_______COMMAND______"></span> *Command*   
Specifies the **!amli** command whose help is to be displayed. For example, **!amli ? set** displays help for the [**!amli set**](-amli-set.md) command. If *Command* is omitted, a list of all commands is displayed.

### <span id="DLL"></span><span id="dll"></span>DLL

Kdexts.dll

### Additional Information

For information about related commands and their uses, see [The AMLI Debugger](the-amli-debugger.md).

 

 





