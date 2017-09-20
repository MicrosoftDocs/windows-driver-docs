---
title: ; (Command Separator)
description: The semicolon ( ; ) character is used to separate multiple commands on a single line.
ms.assetid: efa59a34-1d1d-4df4-bbb9-b8066c6f3b3c
keywords: ["; (Command Separator) Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- ; (Command Separator)
api_type:
- NA
---

# ; (Command Separator)


The semicolon ( **;** ) character is used to separate multiple commands on a single line.

```
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

```
0:000> g `:123`; ? poi(counter); g 
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20;%20%20%28Command%20Separator%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




