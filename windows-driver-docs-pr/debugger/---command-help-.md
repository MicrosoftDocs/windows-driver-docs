---
title: (Command Help)
description: The question mark ( ) character displays a list of all commands and operators.Note  A question mark by itself displays command help.
keywords: ["(Command Help) Windows Debugging"]
ms.date: 08/30/2023
topic_type:
- apiref
ms.topic: reference
api_name:
- (Command Help)
api_type:
- NA
---

# ? (Command Help)

The question mark (**?**) character displays a list of all commands and operators.

**Note**   A question mark by itself displays command help. The [**? expression**](---evaluate-expression-.md) syntax evaluates the given expression.

```dbgcmd
?
```

## Environment

|  Item  | Description          |
|--------|----------------------|
|Modes   |User mode, kernel mode|
|Targets |Live, crash dump      |
|Platforms|All                  |

## Remarks

For more information about standard commands, use **?**. For more information about meta-commands, use [**.help**](-help--meta-command-help-.md). For more information about extension commands, use [**!help**](-help.md).
