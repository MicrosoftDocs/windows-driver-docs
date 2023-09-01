---
title: ; (Command Separator)
description: The semicolon ( ; ) character is used to separate multiple commands on a single line.
keywords: ["; (Command Separator) Windows Debugging"]
ms.date: 09/17/2018
topic_type:
- apiref
ms.topic: reference
api_name:
- ; (Command Separator)
api_type:
- NA
---

# ; (Command Separator)

The semicolon ( ; ) character is used to separate multiple commands on a single line.

```dbgcmd
Command1 ; Command2 [; Command3 ...] 
```

## Parameters

*Command1*, *Command2*, ...  

The commands to be executed.

## Remarks

Commands are executed sequentially from left to right. All commands on a single line refer to the current thread, unless otherwise specified. If a command causes the thread to execute, the remaining commands on the line will be deferred until that thread stops on a debug event.

A small number of commands cannot be followed by a semicolon, because they automatically take the entire remainder of the line as their argument. These include [as aS (Set Alias)](as--as--set-alias-.md), [$<(Run Script File)](-----------------------a---run-script-file-.md), and any command beginning with the [\* (Comment Line Specifier)](----comment-line-specifier-.md) token.

Here is an example. This executes the current program to source line 123, prints the value of counter, then resumes execution:

```dbgcmd
0:000> g `:123`; ? poi(counter); g 
```
