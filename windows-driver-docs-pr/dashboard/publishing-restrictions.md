---
title: Publishing restrictions
description: The following items are restricted during publication. You can still create a shipping label for them, but the request will require additional Microsoft review.
ms.assetid: 30D23457-6BE1-4A4C-B69A-3C8C0A8E093A
ms.topic: article
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Publishing restrictions


The following items are restricted during publication. You can still create a shipping label for them, but the request will require additional Microsoft review.

The Windows Hardware Dev Center dashboard enforces these publication restrictions. Publication restrictions ensure that partners cannot publish drivers that overwrite Microsoft class drivers or generic bus HWID strings. They also ensure that devices do not receive incorrect drivers due to generic third party or reused HWIDs.

Examples of these restrictions include, but are not limited to the list in the following table.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Type of restriction</th>
<th>Additional information</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Invalid driver submission category types</p></td>
<td><p>UNCLASSIFIED</p></td>
</tr>
<tr class="even">
<td><p>Invalid Architecture</p></td>
<td><p>ia64</p></td>
</tr>
<tr class="odd">
<td><p>HWIDs with no bus enumerator</p></td>
<td><p>N/A</p></td>
</tr>
<tr class="even">
<td><p>Invalid bus enumerators</p></td>
<td><p>ActivCardBus</p>
<p>CIRCLASS</p>
<p>Hid\irdevice</p>
<p>Irbus</p>
<p>PS2_</p>
<p>MIDI</p>
<p>PNP</p>
<p>ACP</p>
<p>IAN</p>
<p>AVM</p>
<p>STREAM</p>
<p>DISPLAY</p></td>
</tr>
<tr class="odd">
<td><p>Classcode declarations</p></td>
<td><p>\CLASS</p>
<p>\CC</p>
<p>&amp;</p></td>
</tr>
<tr class="even">
<td><p>Two-part HWIDs</p></td>
<td><p>Enforced on PCI and HDAUDIO buses</p></td>
</tr>
<tr class="odd">
<td><p>Bluetooth HWIDs with service UUIDs and no vendor ID or product ID</p></td>
<td><p>N/A</p></td>
</tr>
<tr class="even">
<td><p>Invalid PCI Vendor Codes</p></td>
<td><p>0000</p>
<p>FFFF</p></td>
</tr>
<tr class="odd">
<td><p>Missing device codes or product ID codes</p></td>
<td><p>Enforced on PCI and USB buses</p></td>
</tr>
<tr class="even">
<td><p>Invalid HWID string starts</p></td>
<td><p>HID_DEVI</p>
<p>SERIAL_M</p>
<p>ISAPNP\PNP</p>
<p>SERENUM\PNP</p>
<p>PNP</p>
<p><em>PNP</p>
<p>BIOS\PNP</p>
<p>ACPI\PNP</p></td>
</tr>
<tr class="odd">
<td><p>System reserved HWIDs</p></td>
<td><p>BIOS\PNP</p>
<p>ACPI\PNP</p></td>
</tr>
<tr class="even">
<td><p>Invalid HWIDs</p></td>
<td><p></em>DONTUSE</p>
<p>SERIAL_MOUSE</p>
<p>Root\circlass</p>
<p>Hid\irdevice</p>
<p>Storage\VolumeSnapshot</p>
<p>Storage\Volume</p></td>
</tr>
</tbody>
</table>

 

For more information about the driver publishing workflow, see [Windows 10 Driver Publishing Workflow](http://go.microsoft.com/fwlink/p/?LinkId=617374).

 

 





