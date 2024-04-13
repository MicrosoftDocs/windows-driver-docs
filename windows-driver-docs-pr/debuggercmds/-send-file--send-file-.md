---
title: ".send_file (Send File)"
description: "The .send_file command copies files. If you are performing remote debugging through a process server, it sends a file from the smart client's computer to the process server's computer."
keywords: [".send_file (Send File) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- .send_file (Send File)
api_type:
- NA
---

# .send\_file (Send File)

The **.send\_file** command copies files. If you are performing remote debugging through a process server, it sends a file from the smart client's computer to the process server's computer.

```dbgcmd
.send_file [-f] Source Destination 
.send_file [-f] -s Destination 
```

## Parameters

<span id="_______-f______"></span><span id="_______-F______"></span> **-f**   
Forces file creation. By default, **.send\_file** will not overwrite any existing files. If the -f switch is used, the destination file will always be created, and any existing file with the same name will be overwritten.

<span id="_______Source______"></span><span id="_______source______"></span><span id="_______SOURCE______"></span> *Source*   
Specifies the full path and filename of the file to be sent. If you are debugging through a process server, this file must be located on the computer where the smart client is running.

<span id="_______Destination______"></span><span id="_______destination______"></span><span id="_______DESTINATION______"></span> *Destination*   
Specifies the directory where the file is to be written. If you are debugging through a process server, this directory name is evaluated on the computer where the process server is running.

<span id="_______-s______"></span><span id="_______-S______"></span> **-s**   
Causes the debugger to copy all loaded symbol files.

## Environment

|  Item  | Description          |
|--------|----------------------|
|Modes   |User mode, kernel mode|
|Targets |Live, crash dump      |
|Platforms|All                  |

## Remarks

This command is particularly useful when you have been performing remote debugging through a process server, but wish to begin debugging locally instead. In this case you can use the .send\_file -s command to copy all the symbol files that the debugger has been using to the process server. These symbol files can then be used by a debugger running on the local computer.
