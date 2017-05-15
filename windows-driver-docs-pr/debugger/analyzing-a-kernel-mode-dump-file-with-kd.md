---
title: Analyzing a Kernel-Mode Dump File with KD
description: Analyzing a Kernel-Mode Dump File with KD
ms.assetid: 7e8fbf6e-0adc-434c-ba93-f83f49a4af92
keywords: ["KD, analyzing a dump file", "CAB file containing a dump file, analyzing kernel-mode dump file with KD"]
---

# Analyzing a Kernel-Mode Dump File with KD


## <span id="ddk_analyzing_a_kernel_mode_dump_file_with_kd_dbg"></span><span id="DDK_ANALYZING_A_KERNEL_MODE_DUMP_FILE_WITH_KD_DBG"></span>


Kernel-mode memory dump files can be analyzed by KD. The processor or Windows version that the dump file was created on does not need to match the platform on which KD is being run.

### <span id="starting_kd"></span><span id="STARTING_KD"></span>Starting KD

To analyze a dump file, start KD with the **-z** command-line option:

**kd -y** *SymbolPath* **-i** *ImagePath* **-z** *DumpFileName*

The **-v** option (verbose mode) is also useful. For a full list of options, see [**KD Command-Line Options**](kd-command-line-options.md).

You can also open a dump file after the debugger is running by using the [**.opendump (Open Dump File)**](-opendump--open-dump-file-.md) command, followed with [**g (Go)**](g--go-.md).

It is possible to debug multiple dump files at the same time. This can be done by including multiple **-z** switches on the command line (each followed by a different file name), or by using [**.opendump**](-opendump--open-dump-file-.md) to add additional dump files as debugger targets. For information about how to control a multiple-target session, see [Debugging Multiple Targets](debugging-multiple-targets.md).

Dump files generally end with the extension .dmp or .mdmp. You can use network shares or Universal Naming Convention (UNC) file names for the memory dump file.

It is also common for dump files to be packed into a CAB file. If you specify the file name (including the .cab extension) after the **-z** option or as the argument to an [**.opendump**](-opendump--open-dump-file-.md) command, the debugger can read the dump files directly out of the CAB. However, if there are multiple dump files stored in a single CAB, the debugger will only be able to read one of them. The debugger will not read any additional files from the CAB, even if they were symbol files or other files associated with the dump file.

### <span id="analyzing_the_dump_file"></span><span id="ANALYZING_THE_DUMP_FILE"></span>Analyzing the Dump File

If you are analyzing a Kernel Memory Dump or a Small Memory Dump, you may need to set the executable image path to point to any executable files which may have been loaded in memory at the time of the crash.

Analysis of a dump file is similar to analysis of a live debugging session. See the [Debugger Commands](debugger-commands.md) reference section for details on which commands are available for debugging dump files in kernel mode.

In most cases, you should begin by using [**!analyze**](-analyze.md). This extension command performs automatic analysis of the dump file and can often result in a lot of useful information.

The [**.bugcheck (Display Bug Check Data)**](-bugcheck--display-bug-check-data-.md) shows the bug check code and its parameters. Look up this bug check in the [Bug Check Code Reference](bug-check-code-reference2.md) for information about the specific error.

The following debugger extensions are especially useful for analyzing a kernel-mode crash dump:

[**!drivers**](-drivers.md)

[**!kdext\*.locks**](-locks---kdext--locks-.md)

[**!memusage**](-memusage.md)

[**!vm**](-vm.md)

[**!errlog**](-errlog.md)

[**!process 0 0**](-process.md)

[**!process 0 7**](-process.md)

For techniques that can be used to read specific kinds of information from a dump file, see [Extracting Information from a Dump File](extracting-information-from-a-dump-file.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Analyzing%20a%20Kernel-Mode%20Dump%20File%20with%20KD%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




