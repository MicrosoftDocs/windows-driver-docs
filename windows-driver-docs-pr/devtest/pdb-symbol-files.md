---
title: PDB Symbol Files
description: PDB Symbol Files
ms.assetid: 077784d9-06be-450c-bdd5-02321305df1b
keywords:
- program database symbol files WDK
- PDB symbol files WDK
- symbol files WDK software tracing
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# PDB Symbol Files


## <span id="ddk_pdb_symbol_files_tools"></span><span id="DDK_PDB_SYMBOL_FILES_TOOLS"></span>


The program database (PDB) symbol file for a [trace provider](trace-provider.md), such as an application or driver, includes instructions for formatting trace messages so that they can be presented in a human-readable display.

The trace message formatting instructions are part of the trace provider source code. The [WPP preprocessor](wpp-preprocessor.md) extracts them from the code and adds them to the trace provider's PDB symbol file.

The compiler generates a PDB file when you compile a debug (checked) version of the trace provider. The build process creates a PDB file by default when you use [BinPlace](binplace.md) to build a trace provider.

The [trace consumers](trace-consumer.md) in the WDK, [TraceView](traceview.md) and [Tracefmt](tracefmt.md), can extract the trace message formatting information directly from the PDB file or from a TMF file. Others require a TMF file. [Tracepdb](tracepdb.md) takes a PDB file as input, extracts the formatting information, and creates a TMF file as output.

Other trace consumers, such as Tracerpt, a tool included in Windows, do not use PDB files or TMF files. Instead, they use the information in Managed Object Format (MOF) files to format trace events. These tools cannot format trace messages.

 

 





