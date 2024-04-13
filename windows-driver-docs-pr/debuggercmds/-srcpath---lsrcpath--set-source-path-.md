---
title: ".srcpath, .lsrcpath (Set Source Path)"
description: "The .srcpath and .lsrcpath commands set or display the source file search path."
keywords: [".srcpath, .lsrcpath (Set Source Path) Windows Debugging"]
ms.date: 11/05/2020
topic_type:
- apiref
ms.topic: reference
api_name:
- .srcpath, .lsrcpath (Set Source Path)
api_type:
- NA
---

# .srcpath, .lsrcpath (Set Source Path)

The **.srcpath** and **.lsrcpath** commands set or display the source file search path.

```dbgcmd
.srcpath[+] [Directory [; ...]] 
.lsrcpath[+] [Directory [; ...]] 
```

## Parameters

<span id="______________"></span> **+**   
Specifies that the new directories will be appended to (rather than replacing) the previous source file search path.

<span id="_______Directory______"></span><span id="_______directory______"></span><span id="_______DIRECTORY______"></span> *Directory*   
Specifies one or more directories to put in the search path. If *Directory* is not specified, the current path is displayed. Separate multiple directories with semicolons.

## Environment

The **.srcpath** command is available on all debuggers. The **.lsrcpath** command is available only in WinDbg and cannot be used in script files.

|  Item  | Description          |
|--------|----------------------|
|Modes   |User mode, kernel mode|
|Targets |Live, crash dump      |
|Platforms|All                  |

## Additional Information

For details and other ways to change this path, see [Source Path](../debugger/source-path.md). For more information about commands that can be used while performing remote debugging through the debugger, see [Controlling a Remote Debugging Session](../debugger/controlling-a-remote-debugging-session.md).

>[!NOTE]
> The source path in WinDbg supports file retrieval using Source Link 1.0, and starting version 1.2104, file retrieval using Source Link 2.0 or DebugInfoD servers. For more information on source path syntax, see [Source Code Extended Access](../debugger/source-code-extended-access.md).

## Remarks

If you include `srv*` in your source path, the debugger uses [SrcSrv](../debugger/srcsrv.md) to retrieve source files from locations specified in the target modules' symbol files. For more information about using srv\* in a source path, see [Using a Source Server](../debugger/using-a-source-server.md) and [**.srcfix**](-srcfix---lsrcfix--use-source-server-.md).

When this command is issued from a debugging client, **.srcpath** sets the source path on the debugging server, while **.lsrcpath** sets the source path on the local machine.
