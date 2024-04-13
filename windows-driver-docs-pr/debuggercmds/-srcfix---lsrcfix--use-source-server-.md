---
title: ".srcfix, .lsrcfix (Use Source Server)"
description: "The .srcfix and .lsrcfix commands automatically set the source path to indicate that a source server will be used."
keywords: [".srcfix, .lsrcfix (Use Source Server) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- .srcfix, .lsrcfix (Use Source Server)
api_type:
- NA
---

# .srcfix, .lsrcfix (Use Source Server)

The **.srcfix** and **.lsrcfix** commands automatically set the source path to indicate that a source server will be used.

```dbgcmd
.srcfix[+] [Paths] 
.lsrcfix[+] [Paths] 
```

## Parameters

<span id="______________"></span> **+**   
Causes the existing source path to be preserved, and **; srv\\*** to be appended to the end. If the **+** is not used, the existing source path is replaced.

<span id="_______Paths______"></span><span id="_______paths______"></span><span id="_______PATHS______"></span> *Paths*   
Specifies one or more additional paths to append to the end of the new source path.

## Environment

The **.srcfix** command is available on all debuggers. The **.lsrcfix** command is available only in WinDbg and cannot be used in script files.

|  Item  | Description          |
|--------|----------------------|
|Modes   |User mode, kernel mode|
|Targets |Live, crash dump      |
|Platforms|All                  |

## Additional Information

For more information on setting the local source path for a remote client, see [**WinDbg Command-Line Options**](../debugger/windbg-command-line-options.md). For details about [SrcSrv](../debugger/srcsrv.md), see [Using a Source Server](../debugger/using-a-source-server.md). For details on the source path and the local source path, see [Source Path](../debugger/source-path.md). For more information about commands that can be used while performing remote debugging through the debugger, see [Controlling a Remote Debugging Session](../debugger/controlling-a-remote-debugging-session.md).

## Remarks

When you add `srv*` to the source path, the debugger uses [SrcSrv](../debugger/srcsrv.md) to retrieve source files from locations specified in the target modules' symbol files. Using `srv*` in the source path is fundamentally different from using `srv*` in the symbol path. In the symbol path, you can specify a symbol server location along with the `srv*` (for example, `.sympath SRV*https://msdl.microsoft.com/download/symbols`). In the source path, srv\* stands alone, separated from all other elements by semicolons.

When this command is issued from a debugging client, **.srcfix** sets the source path to use a source server on the debugging server, while **.lsrcfix** does the same on the local machine.

These commands are the same as the [**.srcpath (Set Source Path)**](-srcpath---lsrcpath--set-source-path-.md) and **.lsrcpath (Set Local Source Path)** commands followed by the **srv\\*** source path element. Thus, the following two commands are equivalent:

```dbgcmd
.srcfix[+] [Paths] 
.srcpath[+] srv*[;Paths] 
```

Similarly, the following two commands are equivalent:

```dbgcmd
.lsrcfix[+] [Paths] 
.lsrcpath[+] srv*[;Paths] 
```
