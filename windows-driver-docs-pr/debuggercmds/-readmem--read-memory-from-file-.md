---
title: ".readmem (Read Memory from File)"
description: "The .readmem command reads raw binary data from the specified file and copies the data to the target computer's memory."
keywords: [".readmem (Read Memory from File) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- .readmem (Read Memory from File)
api_type:
- NA
---

# .readmem (Read Memory from File)

The **.readmem** command reads raw binary data from the specified file and copies the data to the target computer's memory.

```dbgcmd
.readmem FileName Range 
```

## Parameters

<span id="_______FileName______"></span><span id="_______filename______"></span><span id="_______FILENAME______"></span> *FileName*   
Specifies the name of the file to read. You can specify a full path or only the file name. If the file name contains spaces, enclose *FileName* in quotation marks. If you do not specify a path, the debugger uses the current directory.

<span id="_______Range______"></span><span id="_______range______"></span><span id="_______RANGE______"></span> *Range*   
Specifies the address range for putting the data in memory. This parameter can contain a starting and ending address or a starting address and an object count. For more information about the syntax, see [Address and Address Range Syntax](address-and-address-range-syntax.md).

## Environment

|  Item  | Description          |
|--------|----------------------|
|Modes   |User mode, kernel mode|
|Targets |Live, crash dump      |
|Platforms|All                  |

## Remarks

The memory data is copied literally to the target computer. The debugger does not parse the data in any way. For example, the **.readmem myfile 1000 10** command copies 10 bytes from the Myfile file and stores them in the target computer's memory, starting at address 1000.

The **.readmem** command is the opposite of the [**.writemem (Write Memory to File)**](-writemem--write-memory-to-file-.md) command.
