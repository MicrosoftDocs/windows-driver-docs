---
title: ".tlist (List Process IDs)"
description: "The .tlist command lists all processes running on the system."
keywords: ["List Process IDs (.tlist) command", "process, List Process IDs (.tlist) command", ".tlist (List Process IDs) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- .tlist (List Process IDs)
api_type:
- NA
---

# .tlist (List Process IDs)

The **.tlist** command lists all processes running on the system.

```dbgcmd
.tlist [Options][FileNamePattern]
```

## Parameters

*Options*
Can be any number of the following options:

<span id="-v"></span><span id="-V"></span>**-v**  
Causes the display to be verbose. This includes the session number, the process user name, and the command-line used to start the process.

<span id="-c"></span><span id="-C"></span>**-c**  
Limits the display to just the current process.

<span id="_______FileNamePattern______"></span><span id="_______filenamepattern______"></span><span id="_______FILENAMEPATTERN______"></span> *FileNamePattern*   
Specifies the file name to be displayed, or a pattern that the file name of the process must match. Only those processes whose file names match this pattern will be displayed. *FileNamePattern* may contain a variety of wildcards and specifiers; see [String Wildcard Syntax](string-wildcard-syntax.md) for details. This match is made only against the actual file name, not the path.

## Environment

|  Item  | Description          |
|--------|----------------------|
|Modes | user mode only |
|Targets | live debugging only |
|Platforms | all  |

## Additional Information

For other methods of displaying processes, see [Finding the Process ID](../debugger/finding-the-process-id.md).

## Remarks

Each process ID is displayed with an **0n** prefix, to emphasize that the PID is a decimal number.
