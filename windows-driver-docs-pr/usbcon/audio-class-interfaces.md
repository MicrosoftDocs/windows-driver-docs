---
Description: Audio Class Interfaces
title: Audio Class Interfaces
---

# Audio Class Interfaces


USB Audio Device class interface collections that occur on CDC and WMCDC devices have the following properties.

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
<td><p><em>Universal Serial Bus Device Class Definition for Audio Devices</em>, version 1.0.</p></td>
</tr>
<tr class="even">
<td><p>Class</p></td>
<td><p>All interfaces in the interface collection must belong to the Audio Device Class (0x01).</p></td>
</tr>
<tr class="odd">
<td><p>Subclass</p></td>
<td><p>Each interface in the interface collection must have a different subclass from the first interface in the collection.</p></td>
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
USB\Vid_%04x&amp;Pid_%04x&amp;MI_%02x</code></pre>
<p>The hardware IDs for audio interface collections do not contain interface class-specific information. For an explanation of the formatting of hardware IDs that are associated with audio interface collections, see [Enumeration of Interface Collections on Audio Devices without IADs](enumeration-of-interface-collections-on-audio-devices-without-iads.md).</p></td>
</tr>
<tr class="even">
<td><p>Compatible IDs</p></td>
<td><pre space="preserve"><code>USB\Class_01&amp;SubClass_01&amp;Prot_00
USB\Class_01&amp;SubClass_01
USB\Class_01</code></pre>
<p>The format of compatible IDs for audio interface collections contains embedded information about the interface class, interface subclass, and the protocol. For audio interface collections on a CDC or WMCDC device, the interface class is 01, the subclass is 01, and the protocol is 00.</p></td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Busbcon\buses%5D:%20Audio%20Class%20Interfaces%20%20RELEASE:%20%281/26/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")



