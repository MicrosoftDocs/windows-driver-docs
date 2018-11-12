---
title: Analyzing a Kernel-Mode Dump File
description: Analyzing a Kernel-Mode Dump File
ms.assetid: 2bda51c2-b022-4740-8df9-5a2cf2382e3e
keywords: ["dump file, analyzing a kernel-mode dump file"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
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

 

 





