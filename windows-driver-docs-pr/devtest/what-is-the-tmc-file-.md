---
title: What is the TMC File
description: What is the TMC file
ms.date: 04/20/2017
---

# What is the TMC file?

> [!NOTE]
> Unless you are using [TraceView](traceview.md), ignore references to these TMC files.

The [trace message control (.tmc) file](trace-message-control-file.md) is a text file that contains the [control GUID](control-guid.md) along with the trace levels of each [trace provider](trace-provider.md) that is represented in a [PDB symbol file](pdb-symbol-files.md). The name of the TMC file is the control GUID of the trace provider, followed by the .tmc file name extension.

[TraceView](traceview.md) generates a TMC file when it creates a [trace message format (.tmf) file](trace-message-format-file.md) from a PDB symbol file. [Tracepdb](tracepdb.md) can also generate a TMC file when you use the **-c** option.

Most tracing tools do not use the TMC file, but TraceView uses it to associate the control GUID of the trace provider with the [trace flags](trace-flags.md) and [trace level](trace-level.md) that the provider supports.
