---
title: Trace Managed Object Format (MOF) File
description: Trace Managed Object Format (MOF) File
ms.date: 04/20/2017
---

# Trace Managed Object Format (MOF) File


A trace [managed object format](/windows/win32/wmisdk/managed-object-format--mof-) (MOF) file is a text file that contains the control GUID for each [trace provider](trace-provider.md) that is represented in a PDB file. The name of the MOF file is the module name of the trace producer, followed by the .mof file name extension.

[Tracepdb](tracepdb.md) and [BinPlace](binplace.md) create a MOF file for each trace provider when they create a trace message format (.tmf) file from the formatting instructions in a PDB file.

The trace MOF file also contains the following information:

-   The path and file name of the PDB file.

-   The date and time that the PDB file was created.

-   The control GUID for each trace provider.

-   The trace flags defined by the trace provider.

Logman and Perfmon can use the MOF file to find the trace flags for each provider. You can use the MOF file as a quick reference to the control GUID of a trace provider.
