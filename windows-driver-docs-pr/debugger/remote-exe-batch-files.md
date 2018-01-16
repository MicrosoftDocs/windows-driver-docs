---
title: Remote.exe Batch Files
description: Remote.exe Batch Files
ms.assetid: e774d39f-4625-41e7-9309-9dbdd46e986e
keywords: ["remote debugging through remote.exe, batch files"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Remote.exe Batch Files


## <span id="ddk_remote_exe_batch_files_dbg"></span><span id="DDK_REMOTE_EXE_BATCH_FILES_DBG"></span>


As a more detailed example of remote debugging with remote.exe, assume the following about a local host computer in a three-computer kernel debugging scenario:

-   Debugging needs to take place over a null-modem cable on COM2.

-   The symbol files are in the folder c:\\winnt\\symbols.

-   A log file called debug.log is created in **c:\\temp**.

The log file holds a copy of everything you see on the Debug screen during your debug session. All input from the person doing the debugging, and all output from the kernel debugger on the target system, is written to that log file.

A sample batch file for running a debugging session on the local host is:

```
set _NT_DEBUG_PORT=com2
set _NT_DEBUG_BAUD_RATE=19200
set _NT_SYMBOL_PATH=c:\winnt\symbols
set _NT_LOG_FILE_OPEN=c:\temp\debug.log
remote /s "KD -v" debug
```

**Note**   If this batch file is not in the same directory as Remote.exe, and Remote.exe is not in a directory listed in the system path, then you should give the full path to the utility when invoking Remote.exe in this batch file.

 

After this batch file is run, anyone with a Windows computer that is networked to the local host computer can connect to the debug session by using the following command:

```
remote /c computername debug 
```

where *computername* is the NetBIOS name of the local host computer.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Remote.exe%20Batch%20Files%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




