---
title: Analyzing a Kernel-Mode Dump File
description: Analyzing a Kernel-Mode Dump File
keywords: ["dump file, analyzing a kernel-mode dump file"]
ms.date: 06/05/2020
ms.localizationpriority: medium
---

# Analyzing a Kernel-Mode Dump File

This section includes:

[Analyzing a Kernel-Mode Dump File with KD](analyzing-a-kernel-mode-dump-file-with-kd.md)

[Analyzing a Kernel-Mode Dump File with WinDbg](analyzing-a-kernel-mode-dump-file-with-windbg.md)

### Installing Symbol Files

Regardless of which tool you use, you need to access the symbol files for the version of Windows that generated the dump file. These files will be used by the debugger you choose to use to analyze the dump file. For information about working with the symbol server, see see [Microsoft Public Symbols](microsoft-public-symbols.md).

### DumpExam

The DumpExam tool is obsolete. It is no longer needed in the analysis of a crash dump file.
