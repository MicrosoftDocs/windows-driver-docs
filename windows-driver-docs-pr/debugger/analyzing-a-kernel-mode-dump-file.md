---
title: Analyzing a Kernel-Mode Dump File
description: Analyzing a Kernel-Mode Dump File
ms.assetid: 2bda51c2-b022-4740-8df9-5a2cf2382e3e
keywords: ["dump file, analyzing a kernel-mode dump file"]
---

# Analyzing a Kernel-Mode Dump File


## <span id="ddk_analyzing_a_kernel_mode_dump_file_dbg"></span><span id="DDK_ANALYZING_A_KERNEL_MODE_DUMP_FILE_DBG"></span>


This section includes:

[Analyzing a Kernel-Mode Dump File with KD](analyzing-a-kernel-mode-dump-file-with-kd.md)

[Analyzing a Kernel-Mode Dump File with WinDbg](analyzing-a-kernel-mode-dump-file-with-windbg.md)

[Analyzing a Kernel-Mode Dump File with KAnalyze](analyzing-a-kernel-mode-dump-file-with-kanalyze.md)

### <span id="installing_symbol_files"></span><span id="INSTALLING_SYMBOL_FILES"></span>Installing Symbol Files

Regardless of which tool you use, you need to install the symbol files for the version of Windows that generated the dump file. These files will be used by the debugger you choose to use to analyze the dump file. For more information about the proper installation of symbol files, see [Installing Windows Symbol Files](installing-windows-symbol-files.md).

### <span id="ddk_dumpexam_dbg"></span><span id="DDK_DUMPEXAM_DBG"></span>DumpExam

The DumpExam tool is obsolete. It is no longer needed in the analysis of a crash dump file.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Analyzing%20a%20Kernel-Mode%20Dump%20File%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




