---
title: PDB Symbol Files
description: PDB Symbol Files
ms.assetid: 077784d9-06be-450c-bdd5-02321305df1b
keywords: ["program database symbol files WDK", "PDB symbol files WDK", "symbol files WDK software tracing"]
---

# PDB Symbol Files


## <span id="ddk_pdb_symbol_files_tools"></span><span id="DDK_PDB_SYMBOL_FILES_TOOLS"></span>


The program database (PDB) symbol file for a [trace provider](trace-provider.md), such as an application or driver, includes instructions for formatting trace messages so that they can be presented in a human-readable display.

The trace message formatting instructions are part of the trace provider source code. The [WPP preprocessor](wpp-preprocessor.md) extracts them from the code and adds them to the trace provider's PDB symbol file.

The compiler generates a PDB file when you compile a debug (checked) version of the trace provider. The build process creates a PDB file by default when you use [BinPlace](binplace.md) to build a trace provider.

The [trace consumers](trace-consumer.md) in the WDK, [TraceView](traceview.md) and [Tracefmt](tracefmt.md), can extract the trace message formatting information directly from the PDB file or from a TMF file. Others require a TMF file. [Tracepdb](tracepdb.md) takes a PDB file as input, extracts the formatting information, and creates a TMF file as output.

Other trace consumers, such as Tracerpt, a tool included in Windows, do not use PDB files or TMF files. Instead, they use the information in Managed Object Format (MOF) files to format trace events. These tools cannot format trace messages.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20PDB%20Symbol%20Files%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




