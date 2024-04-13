---
title: Dump-File Targets
description: Dump-File Targets
keywords: ["targets, dump files", "dump files"]
ms.date: 05/23/2017
---

# Dump-File Targets


## <span id="ddk_dump_file_targets_dbx"></span><span id="DDK_DUMP_FILE_TARGETS_DBX"></span>


For an introduction and overview of crash dump files, see [Crash Dump Files](crash-dump-files.md).

### <span id="Opening_Dump_Files"></span><span id="opening_dump_files"></span><span id="OPENING_DUMP_FILES"></span>Opening Dump Files

To open a crash dump file for use as a debugger target, use [**OpenDumpFile**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugclient5-opendumpfile) or [**OpenDumpfileWide**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugclient5-opendumpfilewide). These methods are similar to the [**.opendump**](../debuggercmds/-opendump--open-dump-file-.md) debugger command.

**Note**   The engine doesn't completely attach to the dump file until the [**WaitForEvent**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugcontrol3-waitforevent) method has been called. When a dump file is created from a process or kernel, information about the last event is stored in the dump file. After the dump file is opened, the next time execution is attempted, the engine will generate this event for the event callbacks. Only then does the dump file become available in the debugging session. See [Debugging Session and Execution Model](debugging-session-and-execution-model.md) for more details.

 

Additional files can be used to assist in debugging a crash dump file. The methods [**AddDumpInformationFile**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugclient5-adddumpinformationfile) and [**AddDumpInformationFileWide**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugclient5-adddumpinformationfilewide) register files containing page-file information to be used when the next dump file is opened. These methods must be called before the dump file is opened. [**GetNumberDumpFiles**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugclient5-getnumberdumpfiles) will return the number of such files that were used when the current dump file was opened and [**GetDumpFile**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugclient5-getdumpfile) will return a description of these files.

User-mode minidump files contain several streams of information. These streams can be read using the [**Request**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugadvanced3-request) operation [**DEBUG\_REQUEST\_READ\_USER\_MINIDUMP\_STREAM**](/previous-versions/ff541575(v=vs.85)).

### <span id="Creating_Dump_Files"></span><span id="creating_dump_files"></span><span id="CREATING_DUMP_FILES"></span>Creating Dump Files

To create a crash dump file of the current target -- user-mode or kernel-mode -- use [**WriteDumpFile2**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugclient5-writedumpfile2). This method is similar to the [**.dump**](../debuggercmds/-dump--create-dump-file-.md) debugger command.

 

