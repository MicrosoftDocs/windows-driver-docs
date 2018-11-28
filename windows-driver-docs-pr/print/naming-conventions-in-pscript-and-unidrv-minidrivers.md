---
title: Naming Conventions in Pscript and Unidrv Minidrivers
description: Naming Conventions in Pscript and Unidrv Minidrivers
ms.assetid: d15c72e9-781d-4c71-bcf5-b3d08ec603ca
keywords:
- in-box autoconfiguration support WDK printer , naming conventions
- names WDK printer autoconfig
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Naming Conventions in Pscript and Unidrv Minidrivers


Hardware vendors who intend to support autoconfiguration in their Pscript5 or Unidrv minidrivers must adhere to the following naming conventions. Printer description files should be named in accordance with the printer's model name. In the file names shown in this topic, &lt;printerModelName&gt; is a placeholder for the model name of the printer.

### <a href="" id="pscript5-minidrivers"></a> Pscript5 Minidrivers

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Type of file</th>
<th>Naming convention</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Main printer description file</p></td>
<td><p>&lt;printerModelName&gt;.PPD</p></td>
</tr>
<tr class="even">
<td><p>Auxiliary printer description file</p></td>
<td><p>&lt;printerModelName&gt;.GDL</p></td>
</tr>
</tbody>
</table>

 

An auxiliary printer description file contains bidi or autoconfiguration information.

To enable autoconfiguration, a Pscript5 driver must include &lt;printerModelName&gt;.GDL and ps\_schm.GDL in its dependent files list. For information about dependent files, see [Printer INF File Entries](printer-inf-file-entries.md).

### <a href="" id="unidrv-minidrivers"></a> Unidrv Minidrivers

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Type of file</th>
<th>Naming convention</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Main printer description file</p></td>
<td><p>&lt;printerModelName&gt;.GPD or &lt;printerModelName&gt;.GDL</p>
<p>The type of file used depends on the printer description format that is used.</p></td>
</tr>
<tr class="even">
<td><p>Auxiliary printer description file (optional)</p></td>
<td><p>&lt;printerModelName&gt;.GDL</p></td>
</tr>
</tbody>
</table>

 

An auxiliary printer description file, which is optional for Unidrv minidrivers, contains bidi or autoconfiguration information. Alternatively, autoconfiguration information can be contained in the main description file.

To enable autoconfiguration, a Unidrv driver must include any &lt;printerModelName&gt;.GPD or &lt;printerModelName&gt;.GDL files in its dependent files list, as well as the following files:

Stddtype.gdl

Stdschem.gdl

Stdschmx.gdl

 

 




