---
title: Remote.exe Batch Files
description: Remote.exe Batch Files
ms.assetid: e774d39f-4625-41e7-9309-9dbdd46e986e
keywords: ["remote debugging through remote.exe, batch files"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Remote.exe Batch Files


## <span id="ddk_remote_exe_batch_files_dbg"></span><span id="DDK_REMOTE_EXE_BATCH_FILES_DBG"></span>


As a more detailed example of remote debugging with remote.exe, assume the following about a local host computer in a three-computer kernel debugging scenario:

-   Debugging needs to take place over a null-modem cable on COM2.

-   The symbol files are in the folder c:\\winnt\\symbols.

-   A log file called debug.log is created in **c:\\temp**.

The log file holds a copy of everything you see on the Debug screen during your debug session. All input from the person doing the debugging, and all output from the kernel debugger on the target system, is written to that log file.

A sample batch file for running a debugging session on the local host is:

```bat
set _NT_DEBUG_PORT=com2
set _NT_DEBUG_BAUD_RATE=19200
set _NT_SYMBOL_PATH=c:\winnt\symbols
set _NT_LOG_FILE_OPEN=c:\temp\debug.log
remote /s "KD -v" debug
```

**Note**   If this batch file is not in the same directory as Remote.exe, and Remote.exe is not in a directory listed in the system path, then you should give the full path to the utility when invoking Remote.exe in this batch file.

 

After this batch file is run, anyone with a Windows computer that is networked to the local host computer can connect to the debug session by using the following command:

```console
remote /c computername debug 
```

where *computername* is the NetBIOS name of the local host computer.

 

 





