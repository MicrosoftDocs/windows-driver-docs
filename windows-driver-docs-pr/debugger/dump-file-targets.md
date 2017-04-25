---
title: Dump-File Targets
description: Dump-File Targets
ms.assetid: 83fb6753-a6c1-4899-9b06-a6331b3c31a8
keywords: ["targets, dump files", "dump files"]
---

# Dump-File Targets


## <span id="ddk_dump_file_targets_dbx"></span><span id="DDK_DUMP_FILE_TARGETS_DBX"></span>


For an introduction and overview of crash dump files, see [Crash Dump Files](crash-dump-files.md).

### <span id="Opening_Dump_Files"></span><span id="opening_dump_files"></span><span id="OPENING_DUMP_FILES"></span>Opening Dump Files

To open a crash dump file for use as a debugger target, use [**OpenDumpFile**](https://msdn.microsoft.com/library/windows/hardware/ff552322) or [**OpenDumpfileWide**](https://msdn.microsoft.com/library/windows/hardware/ff552324). These methods are similar to the [**.opendump**](https://msdn.microsoft.com/library/windows/hardware/ff564611) debugger command.

**Note**   The engine doesn't completely attach to the dump file until the [**WaitForEvent**](https://msdn.microsoft.com/library/windows/hardware/ff561229) method has been called. When a dump file is created from a process or kernel, information about the last event is stored in the dump file. After the dump file is opened, the next time execution is attempted, the engine will generate this event for the event callbacks. Only then does the dump file become available in the debugging session. See [Debugging Session and Execution Model](debugging-session-and-execution-model.md) for more details.

 

Additional files can be used to assist in debugging a crash dump file. The methods [**AddDumpInformationFile**](https://msdn.microsoft.com/library/windows/hardware/ff537865) and [**AddDumpInformationFileWide**](https://msdn.microsoft.com/library/windows/hardware/ff537874) register files containing page-file information to be used when the next dump file is opened. These methods must be called before the dump file is opened. [**GetNumberDumpFiles**](https://msdn.microsoft.com/library/windows/hardware/ff547887) will return the number of such files that were used when the current dump file was opened and [**GetDumpFile**](https://msdn.microsoft.com/library/windows/hardware/ff546586) will return a description of these files.

User-mode minidump files contain several streams of information. These streams can be read using the [**Request**](https://msdn.microsoft.com/library/windows/hardware/ff554564) operation [**DEBUG\_REQUEST\_READ\_USER\_MINIDUMP\_STREAM**](https://msdn.microsoft.com/library/windows/hardware/ff541575).

### <span id="Creating_Dump_Files"></span><span id="creating_dump_files"></span><span id="CREATING_DUMP_FILES"></span>Creating Dump Files

To create a crash dump file of the current target -- user-mode or kernel-mode -- use [**WriteDumpFile2**](https://msdn.microsoft.com/library/windows/hardware/ff561382). This method is similar to the [**.dump**](https://msdn.microsoft.com/library/windows/hardware/ff562428) debugger command.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Dump-File%20Targets%20%20RELEASE:%20%284/24/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




