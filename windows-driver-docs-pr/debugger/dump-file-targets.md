---
title: Dump-File Targets
description: Dump-File Targets
ms.assetid: 83fb6753-a6c1-4899-9b06-a6331b3c31a8
keywords: ["targets, dump files", "dump files"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Dump-File Targets


## <span id="ddk_dump_file_targets_dbx"></span><span id="DDK_DUMP_FILE_TARGETS_DBX"></span>


For an introduction and overview of crash dump files, see [Crash Dump Files](crash-dump-files.md).

### <span id="Opening_Dump_Files"></span><span id="opening_dump_files"></span><span id="OPENING_DUMP_FILES"></span>Opening Dump Files

To open a crash dump file for use as a debugger target, use [**OpenDumpFile**](https://msdn.microsoft.com/library/windows/hardware/ff552322) or [**OpenDumpfileWide**](https://msdn.microsoft.com/library/windows/hardware/ff552324). These methods are similar to the [**.opendump**](-opendump--open-dump-file-.md) debugger command.

**Note**   The engine doesn't completely attach to the dump file until the [**WaitForEvent**](https://msdn.microsoft.com/library/windows/hardware/ff561229) method has been called. When a dump file is created from a process or kernel, information about the last event is stored in the dump file. After the dump file is opened, the next time execution is attempted, the engine will generate this event for the event callbacks. Only then does the dump file become available in the debugging session. See [Debugging Session and Execution Model](debugging-session-and-execution-model.md) for more details.

 

Additional files can be used to assist in debugging a crash dump file. The methods [**AddDumpInformationFile**](https://msdn.microsoft.com/library/windows/hardware/ff537865) and [**AddDumpInformationFileWide**](https://msdn.microsoft.com/library/windows/hardware/ff537874) register files containing page-file information to be used when the next dump file is opened. These methods must be called before the dump file is opened. [**GetNumberDumpFiles**](https://msdn.microsoft.com/library/windows/hardware/ff547887) will return the number of such files that were used when the current dump file was opened and [**GetDumpFile**](https://msdn.microsoft.com/library/windows/hardware/ff546586) will return a description of these files.

User-mode minidump files contain several streams of information. These streams can be read using the [**Request**](https://msdn.microsoft.com/library/windows/hardware/ff554564) operation [**DEBUG\_REQUEST\_READ\_USER\_MINIDUMP\_STREAM**](https://msdn.microsoft.com/library/windows/hardware/ff541575).

### <span id="Creating_Dump_Files"></span><span id="creating_dump_files"></span><span id="CREATING_DUMP_FILES"></span>Creating Dump Files

To create a crash dump file of the current target -- user-mode or kernel-mode -- use [**WriteDumpFile2**](https://msdn.microsoft.com/library/windows/hardware/ff561382). This method is similar to the [**.dump**](-dump--create-dump-file-.md) debugger command.

 

 





