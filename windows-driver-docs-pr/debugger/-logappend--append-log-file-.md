---
title: .logappend (Append Log File)
description: The .logappend command appends a copy of the events and commands from the Debugger Command window to the specified log file.
keywords: ["Append Log File (.logappend) command", "log file, Append Log File (.logappend) command", ".logappend (Append Log File) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- .logappend (Append Log File)
api_type:
- NA
---

# .logappend (Append Log File)


The **.logappend** command appends a copy of the events and commands from the [Debugger Command window](debugger-command-window.md) to the specified log file.

```dbgcmd
.logappend [/u] [FileName]
```

## <span id="ddk_meta_append_log_file_dbg"></span><span id="DDK_META_APPEND_LOG_FILE_DBG"></span>Parameters


<span id="________u______"></span><span id="________U______"></span> **/u**   
Writes the log file in Unicode format. If you omit this parameter, the debugger writes the log file in ASCII (ANSI) format.

**Note**   When you are appending to an existing log file, you should use the **/u** parameter only if you created the log file by using the **/u** option. Otherwise, your log file will contain ASCII and Unicode characters, which might make it more difficult to read.

 

<span id="_______FileName______"></span><span id="_______filename______"></span><span id="_______FILENAME______"></span> *FileName*   
Specifies the name of the log file. You can specify a full path or only the file name. If the file name contains spaces, enclose *FileName* in quotation marks. If you do not specify the path, the debugger uses the current directory. If you omit *FileName*, the debugger names the file Dbgeng.log.

### Environment

|  Item  | Description          |
|--------|----------------------|
|Modes   |User mode, kernel mode|
|Targets |Live, crash dump      |
|Platforms|All                  |

 

## Remarks

If you already have a log file open when you run the **.logappend** command, the debugger closes the log file. If you specify the name of a file that already exists, the debugger appends new information to the file. If the file does not exist, the debugger creates it.

 

 





