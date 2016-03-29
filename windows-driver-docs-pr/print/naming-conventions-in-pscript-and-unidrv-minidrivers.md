---
title: Naming Conventions in Pscript and Unidrv Minidrivers
description: Naming Conventions in Pscript and Unidrv Minidrivers
ms.assetid: d15c72e9-781d-4c71-bcf5-b3d08ec603ca
keywords: ["in-box autoconfiguration support WDK printer , naming conventions", "names WDK printer autoconfig"]
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
<th align="left">Type of file</th>
<th align="left">Naming convention</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Main printer description file</p></td>
<td align="left"><p>&lt;printerModelName&gt;.PPD</p></td>
</tr>
<tr class="even">
<td align="left"><p>Auxiliary printer description file</p></td>
<td align="left"><p>&lt;printerModelName&gt;.GDL</p></td>
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
<th align="left">Type of file</th>
<th align="left">Naming convention</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Main printer description file</p></td>
<td align="left"><p>&lt;printerModelName&gt;.GPD or &lt;printerModelName&gt;.GDL</p>
<p>The type of file used depends on the printer description format that is used.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Auxiliary printer description file (optional)</p></td>
<td align="left"><p>&lt;printerModelName&gt;.GDL</p></td>
</tr>
</tbody>
</table>

 

An auxiliary printer description file, which is optional for Unidrv minidrivers, contains bidi or autoconfiguration information. Alternatively, autoconfiguration information can be contained in the main description file.

To enable autoconfiguration, a Unidrv driver must include any &lt;printerModelName&gt;.GPD or &lt;printerModelName&gt;.GDL files in its dependent files list, as well as the following files:

Stddtype.gdl

Stdschem.gdl

Stdschmx.gdl

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Naming%20Conventions%20in%20Pscript%20and%20Unidrv%20Minidrivers%20%20RELEASE:%20%283/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




