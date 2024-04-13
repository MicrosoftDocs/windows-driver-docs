---
title: "!amli debugger"
description: "The !amli debugger extension breaks into the AMLI Debugger."
keywords: ["!amli debugger Windows Debugging"]
ms.date: 09/17/2018
topic_type:
- apiref
ms.topic: reference
api_name:
- amli debugger
api_type:
- NA
---

# !amli debugger

The **!amli debugger** extension breaks into the AMLI Debugger.

Syntax

```dbgcmd
    !amli debugger
```

## DLL

Kdexts.dll

## Additional Information

For information about related commands and their uses, see [The AMLI Debugger](../debugger/the-amli-debugger.md).

## Remarks

When this command is issued, notification is sent to the AML interpreter. The next time the interpreter is active, it will immediately break into the AMLI Debugger.

The **!amli debugger** extension only causes one break. If you want it to break again, you need to use this extension again, or set a breakpoint.
