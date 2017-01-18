---
title: Publishing restrictions
description: The following items are restricted during publication. You can still create a shipping label for them, but the request will require additional Microsoft review.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 30D23457-6BE1-4A4C-B69A-3C8C0A8E093A
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
<p>\&</p></td>
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
<p>*PNP</p>
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
<td><p>*DONTUSE</p>
<p>SERIAL_MOUSE</p>
<p>Root\circlass</p>
<p>Hid\irdevice</p>
<p>Storage\VolumeSnapshot</p>
<p>Storage\Volume</p></td>
</tr>
</tbody>
</table>

 

For more information about the driver publishing workflow, see [Windows 10 Driver Publishing Workflow](http://go.microsoft.com/fwlink/p/?LinkId=617374).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhw_dashboard\hw_dashboard%5D:%20Publishing%20restrictions%20%20RELEASE:%20%281/3/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




