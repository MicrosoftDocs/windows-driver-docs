---
title: amli debugger
description: The amli debugger extension breaks into the AMLI Debugger.
ms.assetid: ef55a45f-445a-4b05-a2a9-b21be3667ec3
keywords: ["amli debugger Windows Debugging"]
ms.author: domars
ms.date: 09/17/2018
topic_type:
- apiref
api_name:
- amli debugger
api_type:
- NA
ms.localizationpriority: medium
---

# !amli debugger


The **!amli debugger** extension breaks into the AMLI Debugger.

Syntax

```dbgcmd
    !amli debugger
```

## <span id="ddk__amli_debugger_dbg"></span><span id="DDK__AMLI_DEBUGGER_DBG"></span>


### <span id="DLL"></span><span id="dll"></span>DLL

Kdexts.dll

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For information about related commands and their uses, see [The AMLI Debugger](the-amli-debugger.md).

Remarks
-------

When this command is issued, notification is sent to the AML interpreter. The next time the interpreter is active, it will immediately break into the AMLI Debugger.

The **!amli debugger** extension only causes one break. If you want it to break again, you need to use this extension again, or set a breakpoint.

 

 





