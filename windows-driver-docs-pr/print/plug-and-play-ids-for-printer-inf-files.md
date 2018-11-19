---
title: Plug and Play IDs for Printer INF Files
description: Plug and Play IDs for Printer INF Files
ms.assetid: 4adb9203-1267-466e-89d8-63988ffa56e9
keywords:
- INF files WDK print , Plug and Play IDs
- PnP ID WDK print
- Plug and Play IDs WDK print
- identifiers WDK printer
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Plug and Play IDs for Printer INF Files


You must specify [Plug and Play](plug-and-play-for-printers.md) (PnP) identifiers (IDs) in the [printer INF file install section](printer-inf-file-install-sections.md).

You must use the IDs in the following table, depending on the protocol that the printer uses.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Protocol</th>
<th>PnP ID in the printer INF file.</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>IEEE 1394</p></td>
<td><p>The ID is always specific, with &quot;1394&quot; in the ID string.</p></td>
</tr>
<tr class="even">
<td><p>Parallel</p></td>
<td><p>The ID contains &quot;LPTENUM&amp;quot; in the ID string.</p></td>
</tr>
<tr class="odd">
<td><p>USB</p></td>
<td><p>The ID contains &quot;USBPRINT&amp;quot; in the ID string.</p></td>
</tr>
<tr class="even">
<td><p>Dot4</p></td>
<td><p>The ID contains &quot;DOT4PRT&amp;quot; in the ID string. This ID applies to Dot4USB and parallel. .</p></td>
</tr>
<tr class="odd">
<td><p>Bluetooth</p></td>
<td><p>The ID contains &quot;BTHPRINT&amp;quot; in the ID string.</p></td>
</tr>
<tr class="even">
<td><p>WSD</p></td>
<td><p>The ID contains &quot;WSDPRINT&amp;quot; in the ID string.</p></td>
</tr>
</tbody>
</table>

 

 

 




