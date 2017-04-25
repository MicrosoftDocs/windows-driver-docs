---
title: Analyzing a User-Mode Dump File with CDB
description: Analyzing a User-Mode Dump File with CDB
ms.assetid: 992e9e5b-a2de-4644-b1bb-1569a18081df
keywords: ["CDB, analyzing a dump file", "CAB file containing a dump file, analyzing user-mode dump file with CDB"]
---

# Analyzing a User-Mode Dump File with CDB


## <span id="ddk_analyzing_a_user_mode_dump_file_with_cdb_dbg"></span><span id="DDK_ANALYZING_A_USER_MODE_DUMP_FILE_WITH_CDB_DBG"></span>


User-mode memory dump files can be analyzed by CDB. The processor or Windows version that the dump file was created on does not need to match the platform on which CDB is being run.

### <span id="installing_symbol_files"></span><span id="INSTALLING_SYMBOL_FILES"></span>Installing Symbol Files

Before analyzing the memory dump file, you will need to install the symbol files for the version of Windows that generated the dump file. These files will be used by the debugger you choose to use to analyze the dump file. For more information about the proper installation of symbol files, see [Installing Windows Symbol Files](installing-windows-symbol-files.md).

You will also need to install all the symbol files for the user-mode process, either an application or system service, that caused the system to generate the dump file. If this code was written by you, the symbol files should have been generated when the code was compiled and linked. If this is commercial code, check on the product CD-ROM or contact the software manufacturer for these particular symbol files.

### <span id="starting_cdb"></span><span id="STARTING_CDB"></span>Starting CDB

To analyze a dump file, start CDB with the **-z** command-line option:

**cdb -y** *SymbolPath* **-i** *ImagePath* **-z** *DumpFileName*

The **-v** option (verbose mode) is also useful. For a full list of options, see [**CDB Command-Line Options**](https://msdn.microsoft.com/library/windows/hardware/ff539058).

You can also open a dump file after the debugger is running by using the [**.opendump (Open Dump File)**](https://msdn.microsoft.com/library/windows/hardware/ff564611) command, followed with [**g (Go)**](https://msdn.microsoft.com/library/windows/hardware/ff549693). This allows you to debug multiple dump files at the same time.

It is possible to debug multiple dump files at the same time. This can be done by including multiple **-z** switches on the command line (each followed by a different file name), or by using [**.opendump**](https://msdn.microsoft.com/library/windows/hardware/ff564611) to add additional dump files as debugger targets. For information about how to control a multiple-target session, see [Debugging Multiple Targets](debugging-multiple-targets.md).

Dump files generally end with the extension .dmp or .mdmp. You can use network shares or Universal Naming Convention (UNC) file names for the memory dump file.

It is also common for dump files to be packed into a CAB file. If you specify the file name (including the .cab extension) after the **-z** option or as the argument to an [**.opendump**](https://msdn.microsoft.com/library/windows/hardware/ff564611) command, the debugger can read the dump files directly out of the CAB. However, if there are multiple dump files stored in a single CAB, the debugger will only be able to read one of them. The debugger will not read any additional files from the CAB, even if they are symbol files or executables associated with the dump file.

### <span id="analyzing_a_full_user_dump_file"></span><span id="ANALYZING_A_FULL_USER_DUMP_FILE"></span>Analyzing a Full User Dump File

Analysis of a full user dump file is similar to analysis of a live debugging session. See the [Debugger Commands](https://msdn.microsoft.com/library/windows/hardware/ff540507) reference section for details on which commands are available for debugging dump files in user mode.

### <span id="analyzing_minidump_files"></span><span id="ANALYZING_MINIDUMP_FILES"></span>Analyzing Minidump Files

Analysis of a user-mode minidump file is done in the same way as a full user dump. However, since much less memory has been preserved, you are much more limited in the actions you can perform. Commands that attempt to access memory beyond what is preserved in the minidump file will not function properly.

### <span id="additional_techniques"></span><span id="ADDITIONAL_TECHNIQUES"></span>Additional Techniques

For techniques that can be used to read specific kinds of information from a dump file, see [Extracting Information from a Dump File](extracting-information-from-a-dump-file.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Analyzing%20a%20User-Mode%20Dump%20File%20with%20CDB%20%20RELEASE:%20%284/24/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




