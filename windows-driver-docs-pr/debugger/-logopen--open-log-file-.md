---
title: .logopen (Open Log File)
description: The .logopen command sends a copy of the events and commands from the Debugger Command window to a new log file.
ms.assetid: 00ccc09b-3fd7-462f-a688-2f7b45b584fb
keywords: ["Open Log File (.logopen) command", "log file, Open Log File (.logopen) command", ".logopen (Open Log File) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- .logopen (Open Log File)
api_type:
- NA
ms.localizationpriority: medium
---

# .logopen (Open Log File)


The **.logopen** command sends a copy of the events and commands from the [Debugger Command window](debugger-command-window.md) to a new log file.

```dbgcmd
.logopen [Options] [FileName] 
.logopen /d
```

## <span id="ddk_meta_open_log_file_dbg"></span><span id="DDK_META_OPEN_LOG_FILE_DBG"></span>Parameters


<span id="_______Options______"></span><span id="_______options______"></span><span id="_______OPTIONS______"></span> *Options*   
Any of the following options:

<span id="_t"></span><span id="_T"></span>**/t**  
Appends the process ID with the current date and time to the log file name. This data is inserted after the file name and before the file name extension.

<span id="_u"></span><span id="_U"></span>**/u**  
Writes the log file in Unicode format. If you omit this option, the debugger writes the log file in ASCII (ANSI) format.

<span id="_______FileName______"></span><span id="_______filename______"></span><span id="_______FILENAME______"></span> *FileName*   
Specifies the name of the log file. You can specify a full path or only the file name. If the file name contains spaces, enclose *FileName* in quotation marks. If you do not specify a path, the debugger uses the current directory. If you omit *FileName*, the debugger names the file Dbgeng.log.

<span id="________d______"></span><span id="________D______"></span> **/d**   
Automatically chooses a file name based on the name of the target process or target computer and the state of the target. The file always has the .log file name extension.

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>User mode, kernel mode</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Targets</strong></p></td>
<td align="left"><p>Live, crash dump</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>All</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

If you already have a log file open when you run the **.logopen** command, the debugger closes it. If you specify a file name that already exists, the file's contents are overwritten.

The **.logopen /t** command appends the process ID, date, and time to the log file name. In the following example, the process ID in hexadecimal is 0x02BC, the date is February 28, 2005, and the time is 9:05:50.935.

```dbgcmd
0:000> .logopen /t c:\logs\mylogfile.txt
Opened log file 'c:\logs\mylogfile_02BC_2005-02-28_09-05-50-935.txt'
```

 

 





