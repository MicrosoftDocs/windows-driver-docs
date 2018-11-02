---
title: (Block Delimiter)
description: A pair of braces ( ) is used to surround a block of statements within a debugger command program.
ms.assetid: 1391fa51-61ce-40e5-8bf5-b5a2215c2bd9
keywords: ["(Block Delimiter) Windows Debugging"]
ms.author: domars
ms.date: 09/17/2018
topic_type:
- apiref
api_name:
- (Block Delimiter)
api_type:
- NA
ms.localizationpriority: medium
---

# { } (Block Delimiter)


A pair of braces ( **{ }** ) is used to surround a block of statements within a debugger command program.

```dbgcmd
    Statements { Statements } Statements 
```

## <span id="ddk_token_block_delimiter_dbg"></span><span id="DDK_TOKEN_BLOCK_DELIMITER_DBG"></span>


### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For information about debugger command programs and control flow tokens, see [Using Debugger Command Programs](using-debugger-command-programs.md).

Remarks
-------

When each block is entered, all aliases within the block are evaluated. If you alter the value of an alias at some point within a command block, commands subsequent to that point will not use the new alias value unless they are within a subordinate block.

Each block must begin with a control flow token. If you wish to create a block for the sole purpose of evaluating aliases, you should prefix it with the [**.block**](-block.md) token.

 

 





