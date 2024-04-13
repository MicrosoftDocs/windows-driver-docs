---
title: ".lastevent (Display Last Event)"
description: "The .lastevent command displays the most recent exception or event that occurred."
keywords: [".lastevent (Display Last Event) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- .lastevent (Display Last Event)
api_type:
- NA
---

# .lastevent (Display Last Event)

The **.lastevent** command displays the most recent exception or event that occurred.

```dbgcmd
.lastevent 
```

## Environment

|  Item  | Description          |
|--------|----------------------|
|Modes   |User mode, kernel mode|
|Targets |Live, crash dump      |
|Platforms|All                  |


## Additional Information

For more information about exceptions and events, see [Controlling Exceptions and Events](../debugger/controlling-exceptions-and-events.md).

## Remarks

Breaking into the debugger always creates an exception. There is always a *last event* when the debugger accepted command input. If you break into the debugger by using [**CTRL+C**](../debugger/ctrl-c--break-.md), **CTRL+BREAK**, or Debug | Break, an exception code of 0x80000003 is created.
