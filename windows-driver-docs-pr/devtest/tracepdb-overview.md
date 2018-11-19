---
title: Tracepdb Overview
description: Tracepdb Overview
ms.assetid: ec13726f-65e6-4aef-b2b1-a4bddcd73a37
keywords:
- Tracepdb WDK
- trace message control files WDK
- TMC files WDK
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Tracepdb Overview


[Trace providers](trace-provider.md), such as user-mode applications and kernel-mode drivers, store their trace messages in binary form for efficiency. To read the trace messages, you have to apply the formatting instructions specified for each trace message in the trace provider code.

The [WPP preprocessor](wpp-preprocessor.md) extracts the formatting instructions from the trace provider's code and adds them to [PDB symbol files](pdb-symbol-files.md) for the trace provider.

Tracepdb extracts the formatting instructions from the full or private versions of the PDB symbol file for a trace provider (the trace formatting instructions are stripped from public symbol files.) and creates [trace message format (.tmf) files](trace-message-format-file.md) for each trace provider in the source code. TMF files are text files that contain only the formatting instructions for the provider's trace messages.

Tools that display trace messages in readable format, such as [TraceView](traceview.md) and [Tracefmt](tracefmt.md), use TMF files to parse and format trace messages. Also, you can distribute TMF files to users, instead of distributing private symbol files.

Tracepdb creates a MOF (.mof) file that contains the control GUID and the trace levels of each trace provider that are represented in the PDB file. The name of the MOF file is the module name of the trace provider.

Tracepdb can also create a [trace message control (.tmc) file](trace-message-control-file.md) for each trace provider in the source code if you use the **-c** option. The TMC file contains the [control GUID](control-guid.md) and the trace levels of each trace provider represented in the PDB file. The name of the TMC file is the control GUID of the [trace provider](trace-provider.md). You should only care about the TMC file if you will be using Traceview without a PDB file.

The only function of Tracepdb is to create TMF files. However, other tools, such as [BinPlace](binplace.md), TraceView, and Tracefmt, create TMF files, in addition to their other features.. Using Tracepdb is equivalent to using the **binplace -:tmf** command, the **traceview -parsepdb** command, and the **tracefmt -i** command.

On systems prior to Windows Vista, Tracepdb requires mspdb70.dll and msvcr70.dll. If these files are not in the same directory as the Tracepdb.exe file, move them before using Tracepdb.

On systems prior to Windows Vista, you must copy the Dbghelp.dll file from the bin\\&lt;*Platform*&gt; subdirectory of the Windows Driver Kit (WDK) (where &lt;*Platform*&gt;is either x86, amd64, or ia64) into the directory in which Tracefmt.exe is located.

For more information about event tracing, see the Windows SDK documentation. For information about using event tracing in kernel-mode drivers and user-mode applications, see [WPP Software Tracing](wpp-software-tracing.md).

 

 





