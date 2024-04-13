---
title: "br (Breakpoint Renumber)"
description: "The br command renumbers one or more breakpoints."
keywords: ["br (Breakpoint Renumber) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- br (Breakpoint Renumber)
api_type:
- NA
---

# br (Breakpoint Renumber)


The **br** command renumbers one or more breakpoints.

```dbgcmd
br OldID NewID [OldID2 NewID2 ...] 
```

## <span id="ddk_cmd_breakpoint_renumber_dbg"></span><span id="DDK_CMD_BREAKPOINT_RENUMBER_DBG"></span>Parameters


<span id="_______OldID______"></span><span id="_______oldid______"></span><span id="_______OLDID______"></span> *OldID*   
Specifies the current ID number of the breakpoint.

<span id="_______NewID______"></span><span id="_______newid______"></span><span id="_______NEWID______"></span> *NewID*   
Specifies a new number that becomes the ID of the breakpoint.

## Environment

|  Item       | Description               |
|-----------|------------------------|
| Modes     | user mode, kernel mode |
| Targets   | live debugging only    |
| Platforms | all                    |

 

## Additional Information

For more information about and examples of how to use breakpoints, other breakpoint commands and methods of controlling breakpoints, and how to set breakpoints in user space from a kernel debugger, see [Using Breakpoints](../debugger/using-breakpoints.md). For more information about conditional breakpoints, see [Setting a Conditional Breakpoint](../debugger/setting-a-conditional-breakpoint.md).

## Remarks

You can use the **br** command to renumber any number of breakpoints at the same time. For each breakpoint, list the old ID and the new ID, in that order, as parameters to **br**.

If there is already a breakpoint with an ID equal to *NewID*, the command fails and an error message is displayed.

