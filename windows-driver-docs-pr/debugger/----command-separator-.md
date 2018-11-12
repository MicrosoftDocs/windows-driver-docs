---
title: ; (Command Separator)
description: The semicolon ( ; ) character is used to separate multiple commands on a single line.
ms.assetid: efa59a34-1d1d-4df4-bbb9-b8066c6f3b3c
keywords: ["; (Command Separator) Windows Debugging"]
ms.author: domars
ms.date: 09/17/2018
topic_type:
- apiref
api_name:
- ; (Command Separator)
api_type:
- NA
ms.localizationpriority: medium
---

# ; (Command Separator)


The semicolon ( **;** ) character is used to separate multiple commands on a single line.

```dbgcmd
    Command1 ; Command2 [; Command3 ...] 
```

## <span id="ddk_token_command_separator_dbg"></span><span id="DDK_TOKEN_COMMAND_SEPARATOR_DBG"></span>Parameters


<span id="_______Command1__Command2__..."></span><span id="_______command1__command2__..."></span><span id="_______COMMAND1__COMMAND2__..."></span> *Command1*, *Command2*, ...  
The commands to be executed.

Remarks
-------

Commands are executed sequentially from left to right. All commands on a single line refer to the current thread, unless otherwise specified. If a command causes the thread to execute, the remaining commands on the line will be deferred until that thread stops on a debug event.

A small number of commands cannot be followed by a semicolon, because they automatically take the entire remainder of the line as their argument. These include [**as (Set Alias)**](as--as--set-alias-.md), [**$&lt; (Run Script File)**](-----------------------a---run-script-file-.md), **$&gt;&lt; (Run Script File)**, and any command beginning with the [**\* (Comment Line Specifier)**](----comment-line-specifier-.md) token.

Here is an example. This executes the current program to source line 123, prints the value of **counter**, then resumes execution:

```console
0:000> g `:123`; ? poi(counter); g 
```

 

 





