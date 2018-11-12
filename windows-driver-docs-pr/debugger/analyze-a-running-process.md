---
title: Analyze a Running Process
description: Use the following commands to record and analyze the heap memory allocations in a running process. This analysis focuses on stack traces.
ms.assetid: 65a8b510-f5f1-4622-87ff-b44d5855787d
keywords: ["Analyze a Running Process Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- Analyze a Running Process
api_type:
- NA
ms.localizationpriority: medium
---

# Analyze a Running Process


Use the following commands to record and analyze the heap memory allocations in a running process. This analysis focuses on stack traces.

```dbgcmd
umdh -p:PID [-f:LogFile] [-v[:MsgFile]] | [-g] | [-h]
```

## <span id="ddk_analyze_a_running_process_dtools"></span><span id="DDK_ANALYZE_A_RUNNING_PROCESS_DTOOLS"></span>Parameters


<span id="_______-p_PID______"></span><span id="_______-p_pid______"></span><span id="_______-P_PID______"></span> **-p:**<em>PID</em>   
Specifies the process to analyze. *PID* is the process ID of the process. This parameter is required.

To find the PID of a running process, use Task Manager, Tasklist (Windows XP and later operating systems), or [TList](tlist.md).

<span id="_______-f_LogFile______"></span><span id="_______-f_logfile______"></span><span id="_______-F_LOGFILE______"></span> **-f:**<em>LogFile</em>   
Saves the log contents in a text file. By default, UMDH writes the log to stdout (command window).

*LogFile* specifies the path (optional) and name of the file. If you specify an existing file, UMDH overwrites the file.

**Note**   If UMDH was not started in Administrator mode, or attempts to write to "protected" paths, it will be denied access.

 

<span id="_______-v__MsgFile_"></span><span id="_______-v__msgfile_"></span><span id="_______-V__MSGFILE_"></span> **-v\[:**<em>MsgFile</em>**\]**  
Verbose mode. Generates detailed informational and error messages. By default, UMDH writes these messages to stderr.

*MsgFile* specifies the path (optional) and name of a text file. When you use this variable, UMDH writes the verbose messages to the specified file, instead of to stderr. If you specify an existing file, UMDH overwrites the file.

<span id="_______-g"></span><span id="_______-G"></span> **-g**  
Logs the heap blocks that are not referenced by the process ("garbage collection").

<span id="_______-h"></span><span id="_______-H"></span> **-h**  
Displays help.

### <span id="comments"></span><span id="COMMENTS"></span>Comments

On Windows 2000, if UMDH is reporting errors finding the stack trace database, and you have enabled the **Create user mode stack trace database** option in [GFlags](gflags.md), you might have a symbol file conflict. To resolve it, copy the DBG and PDB symbol files for the application to the same directory, and try again.

### <span id="sample_usage"></span><span id="SAMPLE_USAGE"></span>Sample Usage

```dbgcmd
umdh -?
umdh -p:2230
umdh -p:2230  -f:dump_allocations.txt
umdh -p:2230 -f:c:\Log1.txt -v:c:\Msg1.txt
umdh -p:2230 -g -f:garbage.txt
```

 

 





