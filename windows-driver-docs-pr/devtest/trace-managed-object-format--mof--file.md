---
title: Trace Managed Object Format (MOF) File
description: Trace Managed Object Format (MOF) File
ms.assetid: e0ef452b-042d-42d0-be0f-b36e7bf47285
---

# Trace Managed Object Format (MOF) File


A trace [managed object format](http://go.microsoft.com/fwlink/p/?linkid=74565) (MOF) file is a text file that contains the control GUID for each [trace provider](trace-provider.md) that is represented in a PDB file. The name of the MOF file is the module name of the trace producer, followed by the .mof file name extension.

[Tracepdb](tracepdb.md) and [BinPlace](binplace.md) create a MOF file for each trace provider when they create a trace message format (.tmf) file from the formatting instructions in a PDB file.

The trace MOF file also contains the following information:

-   The path and file name of the PDB file.

-   The date and time that the PDB file was created.

-   The control GUID for each trace provider.

-   The trace flags defined by the trace provider.

Logman and Perfmon can use the MOF file to find the trace flags for each provider. You can use the MOF file as a quick reference to the control GUID of a trace provider.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Trace%20Managed%20Object%20Format%20%28MOF%29%20File%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




