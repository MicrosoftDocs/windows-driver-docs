---
title: Tracepdb
description: Tracepdb
ms.assetid: da7658a8-5fc3-409c-8a34-2aa134b9823b
keywords: ["software tracing WDK , Tracepdb", "Tracepdb WDK", "TMF files WDK , Tracepdb", "tracing WDK , Tracepdb", "trace message format files WDK"]
---

# Tracepdb


## <span id="ddk_tracepdb_tools"></span><span id="DDK_TRACEPDB_TOOLS"></span>


Tracepdb (Tracepdb.exe) is a command-line tool that creates [trace message format (.tmf) files](trace-message-format-file.md) by extracting trace message formatting instructions from the full or private [PDB symbol file](pdb-symbol-files.md) for a [trace provider](trace-provider.md) that uses WPP software tracing macros.

You can provide the private PDB symbol file for the trace provider or Tracepdb can find the provider's private PDB symbol file in a directory or by using an internal symbol server. Tracepdb runs on Windows 2000 and later versions of Windows.

**Note**  [Tracefmt](tracefmt.md), a tool that formats and displays trace messages, can also create TMF files from PDB symbol files. For information, see Tracefmt.

 

<table>
<colgroup>
<col width="100%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Where can I get Tracepdb?</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Tracepdb (Tracepdb.exe) is included when you install the WDK, Visual Studio, and the Windows SDK for desktop apps. For information about downloading the kits, see [Windows Hardware Downloads](http://go.microsoft.com/fwlink/p/?linkid=290798).</p>
<p><strong>Windows Driver Kit (WDK) 8.1</strong> (installation path)</p>
<p>%WindowsSdkDir%\bin\x64\Tracepdb.exe</p>
<p>%WindowsSdkDir%\bin\x86\Tracepdb.exe</p>
<div class="alert">
<strong>Note</strong>  The Visual Studio environment variable, %WindowsSdkDir%, represents the path to the Windows kits directory where the kits are installed, for example, C:\Program Files (x86)\Windows Kits\8.1.
</div>
<div>
 
</div></td>
</tr>
</tbody>
</table>

 

This section includes the following topics:

[Tracepdb Overview](tracepdb-overview.md)

[**Tracepdb Commands**](tracepdb-commands.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Tracepdb%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




