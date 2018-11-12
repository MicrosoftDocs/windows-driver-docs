---
title: amli
description: The amli extension displays some Help text in the Debugger Command window for the amli extension commands.
ms.assetid: bb632778-5266-4d71-bef5-943aaa682db4
keywords: ["amli Windows Debugging"]
ms.author: domars
ms.date: 09/17/2018
topic_type:
- apiref
api_name:
- amli
api_type:
- NA
ms.localizationpriority: medium
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

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For information about related commands and their uses, see [The AMLI Debugger](the-amli-debugger.md).

 

 





