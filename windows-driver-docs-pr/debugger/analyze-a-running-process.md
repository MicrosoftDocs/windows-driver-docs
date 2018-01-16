---
title: Analyze a Running Process
description: Use the following commands to record and analyze the heap memory allocations in a running process. This analysis focuses on stack traces.
ms.assetid: 65a8b510-f5f1-4622-87ff-b44d5855787d
keywords: ["Analyze a Running Process Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- Analyze a Running Process
api_type:
- NA
---

# Analyze a Running Process


Use the following commands to record and analyze the heap memory allocations in a running process. This analysis focuses on stack traces.

```
umdh -p:PID [-f:LogFile] [-v[:MsgFile]] | [-g] | [-h]
```

## <span id="ddk_analyze_a_running_process_dtools"></span><span id="DDK_ANALYZE_A_RUNNING_PROCESS_DTOOLS"></span>Parameters


<span id="_______-p_PID______"></span><span id="_______-p_pid______"></span><span id="_______-P_PID______"></span> **-p:***PID*   
Specifies the process to analyze. *PID* is the process ID of the process. This parameter is required.

To find the PID of a running process, use Task Manager, Tasklist (Windows XP and later operating systems), or [TList](tlist.md).

<span id="_______-f_LogFile______"></span><span id="_______-f_logfile______"></span><span id="_______-F_LOGFILE______"></span> **-f:***LogFile*   
Saves the log contents in a text file. By default, UMDH writes the log to stdout (command window).

*LogFile* specifies the path (optional) and name of the file. If you specify an existing file, UMDH overwrites the file.

**Note**   If UMDH was not started in Administrator mode, or attempts to write to "protected" paths, it will be denied access.

 

<span id="_______-v__MsgFile_"></span><span id="_______-v__msgfile_"></span><span id="_______-V__MSGFILE_"></span> **-v\[:***MsgFile***\]**  
Verbose mode. Generates detailed informational and error messages. By default, UMDH writes these messages to stderr.

*MsgFile* specifies the path (optional) and name of a text file. When you use this variable, UMDH writes the verbose messages to the specified file, instead of to stderr. If you specify an existing file, UMDH overwrites the file.

<span id="_______-g"></span><span id="_______-G"></span> **-g**  
Logs the heap blocks that are not referenced by the process ("garbage collection").

<span id="_______-h"></span><span id="_______-H"></span> **-h**  
Displays help.

### <span id="comments"></span><span id="COMMENTS"></span>Comments

On Windows 2000, if UMDH is reporting errors finding the stack trace database, and you have enabled the **Create user mode stack trace database** option in [GFlags](gflags.md), you might have a symbol file conflict. To resolve it, copy the DBG and PDB symbol files for the application to the same directory, and try again.

### <span id="sample_usage"></span><span id="SAMPLE_USAGE"></span>Sample Usage

```
umdh -?
umdh -p:2230
umdh -p:2230  -f:dump_allocations.txt
umdh -p:2230 -f:c:\Log1.txt -v:c:\Msg1.txt
umdh -p:2230 -g -f:garbage.txt
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Analyze%20a%20Running%20Process%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




