---
Description: Video Class Interfaces
MS-HAID:
- 'usbsystem\_66ef88c9-87f7-4007-96c0-79b43df1f712.xml'
- 'buses.video\_class\_interfaces'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
title: Video Class Interfaces
---

# Video Class Interfaces


USB Video Device Class interface collections that occur on CDC and WMCDC devices have the following properties.

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
<td><p><em>Universal Serial Bus Device Class Definition for Video Devices</em>, version 1.0.</p></td>
</tr>
<tr class="even">
<td><p>Class</p></td>
<td><p>Video (0x0E).</p></td>
</tr>
<tr class="odd">
<td><p>Subclass</p></td>
<td><p>Video Control (0x01).</p></td>
</tr>
<tr class="even">
<td><p>Protocol</p></td>
<td><p>None (0x00).</p></td>
</tr>
<tr class="odd">
<td><p>Enumerated</p></td>
<td><p>Yes.</p></td>
</tr>
<tr class="even">
<td><p>Related interfaces</p></td>
<td><p>Zero or more contiguous interfaces that belong to the streaming subclass (0x02).</p></td>
</tr>
<tr class="odd">
<td><p>Hardware IDs</p></td>
<td><pre space="preserve"><code>USB\Vid_%04x&amp;Pid_%04x&amp;Rev_%04x&amp;MI_%02x
USB\Vid_%04x&amp;Pid_%04x&amp;MI_%02x</code></pre></td>
</tr>
<tr class="even">
<td><p>Compatible IDs</p></td>
<td><pre space="preserve"><code>USB\Class_0E&amp;SubClass_01&amp;Prot_00
USB\Class_0E&amp;SubClass_01
USB\Class_0E</code></pre></td>
</tr>
<tr class="odd">
<td><p>Special handling</p></td>
<td><p>Video class interface collections receive special handling on CDC devices. On non-CDC devices, video class interface collections are defined by interface association descriptors (IADs). On CDC devices, video class interface collections are defined by union functional descriptors (UFDs).</p></td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Busbcon\buses%5D:%20Video%20Class%20Interfaces%20%20RELEASE:%20%281/26/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")



