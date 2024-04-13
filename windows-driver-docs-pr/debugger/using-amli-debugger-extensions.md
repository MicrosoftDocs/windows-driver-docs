---
title: Using AMLI Debugger Extensions
description: Using AMLI Debugger Extensions
keywords: ["AMLI Debugger, AMLI Debugger extensions", "amli extension", "acpikd.amli extension"]
ms.date: 11/07/2018
---

# Using AMLI Debugger Extensions

The AMLI Debugger extension commands are contained in the extension module Kdexts.dll and use the following syntax:

```dbgcmd
kd> !amli command [parameters] 
```

As with any extension module, after it has been loaded you can omit the **acpikd** prefix.

If you are at the AMLI Debugger prompt, you can execute any of these extension commands by simply entering the *command* name without the **!amli** prefix:

```dbgcmd
AMLI(? for help)-> command [parameters] 
```

When you are at this prompt, the **!amli debugger** command is not available (because it would be meaningless). Also, the help command ( **?** ) at this prompt shows all AMLI Debugger extensions and commands, while the **!amli ?** extension only displays help on actual extensions.

| Action                      | Extension Command |
|-----------------------------|-------------------|
| Display Help                | !amli ?           |
| Set AML Breakpoint          | !amli bp          |
| List AML Breakpoints        | !amli bl          |
| Disable AML Breakpoint      | !amli bd          |
| Enable AML Breakpoint       | !amli be          |
| Clear AML Breakpoint        | !amli bc          |
| Enter AMLI Debugger         | !amli debugger    |
| Display Event Log           | !amli dl          |
| Clear Event Log             | !amli cl          |
| Display Heap                | !amli dh          |
| Display Data Object         | !amli do          |
| Display Stack               | !amli ds          |
| Display Namespace Object    | !amli dns         |
| Find Namespace Object       | !amli find        |
| Display Nearest Method      | !amli ln          |
| List All Contexts           | !amli lc          |
| Display Context Information | !amli r           |
| Unassemble AML Code         | !amli u           |
| Set AMLI Debugger Options   | !amli set         |

## See Also

[The AMLI Debugger](the-amli-debugger.md)
