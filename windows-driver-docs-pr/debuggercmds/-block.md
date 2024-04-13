---
title: ".block (WinDbg)"
description: "The .block token performs no action; it is used solely to introduce a block of statements."
keywords: [".block Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- .block
api_type:
- NA
---

# .block


The **.block** token performs no action; it is used solely to introduce a block of statements.

```dbgcmd
    Commands ; .block { Commands } ; Commands 
```

## <span id="ddk_token_block_dbg"></span><span id="DDK_TOKEN_BLOCK_DBG"></span>


## Additional Information

For information about using a new block to evaluate an alias, see [Using Aliases](using-aliases.md) and [**as, aS (Set Alias)**](as--as--set-alias-.md).

For information about other control flow tokens and their use in debugger command programs, see [Using Debugger Command Programs](../debugger/using-debugger-command-programs.md).

## Remarks

Blocks of commands are surrounded by braces. When each block is entered, all aliases within the block are evaluated. If you alter the value of an alias at some point within a command block, commands subsequent to that point will not use the new alias value unless they are within a subordinate block.

Each block must begin with a control flow token. If you wish to create a block for the sole purpose of evaluating aliases, you should prefix it with the **.block** token, since this token has no effect other than to allow a block to be introduced.

