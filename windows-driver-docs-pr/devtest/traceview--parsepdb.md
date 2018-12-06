---
title: TraceView -parsepdb
description: Use a TraceView -parsepdb command to create trace message format files from data in a PDB symbol file.
ms.assetid: d193aa3c-17ee-4fcf-a4ee-afb50c78ec54
keywords:
- TraceView -parsepdb Driver Development Tools
topic_type:
- apiref
api_name:
- TraceView -parsepdb
api_type:
- NA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# TraceView -parsepdb


Use a **TraceView -parsepdb** command to create [trace message format files](trace-message-format-file.md) from data in a [PDB symbol file](pdb-symbol-files.md).

```
    traceview -parsepdb PDBfile [-p TMFPath] 
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______PDBfile______"></span><span id="_______pdbfile______"></span><span id="_______PDBFILE______"></span> *PDBfile*   
Specifies the path and file name of a PDB symbol file.

<span id="_______-p_______TMFPath______"></span><span id="_______-p_______tmfpath______"></span><span id="_______-P_______TMFPATH______"></span> **-p** *TMFPath*   
Specifies a directory for the trace message format (TMF) file.

You cannot specify the name of the TMF file. The file name is the [message GUID](message-guid.md) of the trace provider.

### <span id="examples"></span><span id="EXAMPLES"></span>Examples

```
traceview -parsepdb tracedrv.pdb
traceview -parsepdb tracedrv.pdb -p d:\tracing
```

Comments

TraceView also creates a [trace message control (.tmc) file](trace-message-control-file.md) for each [trace provider](trace-provider.md) in the source code. The TMC file contains the [control GUID](control-guid.md) and the trace levels of each trace provider represented in the PDB file. The name of the TMC file is the control GUID of the trace provider.

If TraceView responds to a **-parsepdb** command only by displaying the **Press any key to exit** message, this might indicate that the required DLL have not been moved to the directory in which the TraceView executable file, traceview.exe, is located. For more information, see [Preparing to Use TraceView](preparing-to-use-traceview.md). This also might indicate that the PDB file does not have the required trace components. Confirm that the source code from which the PDB file was created is instrumented for software tracing.









