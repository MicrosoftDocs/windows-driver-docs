---
title: TraceView -parsepdb
description: Use a TraceView -parsepdb command to create trace message format files from data in a PDB symbol file.
ms.assetid: d193aa3c-17ee-4fcf-a4ee-afb50c78ec54
keywords: ["TraceView -parsepdb Driver Development Tools"]
topic_type:
- apiref
api_name:
- TraceView -parsepdb
api_type:
- NA
---

# TraceView -parsepdb


Use a **TraceView -parsepdb** command to create [trace message format files](trace-message-format-file.md) from data in a [PDB symbol file](pdb-symbol-files.md).

``` syntax
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20TraceView%20-parsepdb%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




