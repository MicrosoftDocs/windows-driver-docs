---
title: Plug and Play IDs for Printer INF Files
author: windows-driver-content
description: Plug and Play IDs for Printer INF Files
ms.assetid: 4adb9203-1267-466e-89d8-63988ffa56e9
keywords: ["INF files WDK print , Plug and Play IDs", "PnP ID WDK print", "Plug and Play IDs WDK print", "identifiers WDK printer"]
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
<td><p>The ID contains &quot;LPTENUM\&quot; in the ID string.</p></td>
</tr>
<tr class="odd">
<td><p>USB</p></td>
<td><p>The ID contains &quot;USBPRINT\&quot; in the ID string.</p></td>
</tr>
<tr class="even">
<td><p>Dot4</p></td>
<td><p>The ID contains &quot;DOT4PRT\&quot; in the ID string. This ID applies to Dot4USB and parallel. .</p></td>
</tr>
<tr class="odd">
<td><p>Bluetooth</p></td>
<td><p>The ID contains &quot;BTHPRINT\&quot; in the ID string.</p></td>
</tr>
<tr class="even">
<td><p>WSD</p></td>
<td><p>The ID contains &quot;WSDPRINT\&quot; in the ID string.</p></td>
</tr>
</tbody>
</table>

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Plug%20and%20Play%20IDs%20for%20Printer%20INF%20Files%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


