---
title: "{ } (Block Delimiter)"
description: "A pair of braces { } is used to surround a block of statements within a debugger command program."
keywords: ["(Block Delimiter) Windows Debugging"]
ms.date: 08/30/2023
topic_type:
- apiref
ms.topic: reference
api_name:
- (Block Delimiter)
api_type:
- NA
---

# { } (Block Delimiter)

A pair of braces ( **{ }** ) is used to surround a block of statements within a debugger command program.

```dbgcmd
Statements { Statements } Statements 
```

## Additional Information

For information about debugger command programs and control flow tokens, see [Using Debugger Command Programs](../debugger/using-debugger-command-programs.md).

## Remarks

When each block is entered, all aliases within the block are evaluated. If you alter the value of an alias at some point within a command block, commands subsequent to that point will not use the new alias value unless they are within a subordinate block.

Each block must begin with a control flow token. If you wish to create a block for the sole purpose of evaluating aliases, you should prefix it with the [**.block**](-block.md) token.
