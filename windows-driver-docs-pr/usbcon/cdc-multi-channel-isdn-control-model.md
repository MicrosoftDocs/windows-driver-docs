---
Description: CDC Multi-Channel ISDN Control Model
title: CDC Multi-Channel ISDN Control Model
---

# CDC Multi-Channel ISDN Control Model


USB CDC Multi-Channel ISDN Control Model (MCCM) interface collections have the following properties.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Property</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Reference</p></td>
<td><p><em>Universal Serial Bus Class Definitions for Communication Devices</em>, version 1.1, Section 3.7.1</p></td>
</tr>
<tr class="even">
<td><p>Class of the master Interface</p></td>
<td><p>Communication Interface Class (0x02)</p></td>
</tr>
<tr class="odd">
<td><p>Subclass of the master interface</p></td>
<td><p>MCCM (0x04)</p></td>
</tr>
<tr class="even">
<td><p>Protocol</p></td>
<td><p>None (0x00)</p></td>
</tr>
<tr class="odd">
<td><p>Enumerated</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="even">
<td><p>Related interfaces</p></td>
<td><p>Multiple data class interfaces that the union functional descriptor (UFD) references.</p></td>
</tr>
<tr class="odd">
<td><p>Hardware IDs</p></td>
<td><pre space="preserve"><code>USB\Vid_%04x&amp;Pid_%04x&amp;Rev_%04x&amp;Cdc_04&amp;MI_%02x
USB\Vid_%04x&amp;Pid_%04x&amp;Rev_%04x&amp;Cdc_04
USB\Vid_%04x&amp;Pid_%04x&amp;Cdc_04&amp;MI_%02x
USB\Vid_%04x&amp;Pid_%04x&amp;Cdc_04</code></pre></td>
</tr>
<tr class="even">
<td><p>Compatible IDs</p></td>
<td><pre space="preserve"><code>USB\Class_02&amp;SubClass_04&amp;Prot_00
USB\Class_02&amp;SubClass_04
USB\Class_02</code></pre></td>
</tr>
<tr class="odd">
<td><p>Special handling</p></td>
<td><p>None</p></td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Busbcon\buses%5D:%20CDC%20Multi-Channel%20ISDN%20Control%20Model%20%20RELEASE:%20%281/26/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")



