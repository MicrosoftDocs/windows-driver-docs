---
title: Tracepdb
description: Tracepdb
ms.assetid: da7658a8-5fc3-409c-8a34-2aa134b9823b
keywords:
- software tracing WDK , Tracepdb
- Tracepdb WDK
- TMF files WDK , Tracepdb
- tracing WDK , Tracepdb
- trace message format files WDK
ms.date: 04/20/2017
ms.localizationpriority: medium
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
<td align="left"><p>Tracepdb (Tracepdb.exe) is included when you install the WDK, Visual Studio, and the Windows SDK for desktop apps. For information about downloading the kits, see <a href="http://go.microsoft.com/fwlink/p/?linkid=290798" data-raw-source="[Windows Hardware Downloads](http://go.microsoft.com/fwlink/p/?linkid=290798)">Windows Hardware Downloads</a>.</p>
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

 

 





