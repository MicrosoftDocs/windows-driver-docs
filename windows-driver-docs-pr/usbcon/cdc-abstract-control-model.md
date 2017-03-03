---
Description: CDC Abstract Control Model
MS-HAID:
- 'usbsystem\_0f00b19e-8fff-42de-901d-d8ab0a138218.xml'
- 'buses.cdc\_abstract\_control\_model'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
title: CDC Abstract Control Model
author: windows-driver-content
---

# CDC Abstract Control Model


There are two versions of the Abstract Control Model (ACM). The original version is defined in the *USB Communication Device Class* (CDC) specification. The *USB Wireless Mobile Communication Device Class* (WMCDC) specification contains an extended definition of the ACM.

Interface collections that comply with the WMCDC specification are described in [WMCDC Abstract Control Model](wmcdc-abstract-control-model.md).

Interface collections that comply with the CDC specification have the following properties.

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
<td><p><em>Universal Serial Bus Class Definitions for Communication Devices</em>, version 1.1, Section 3.6.2.</p></td>
</tr>
<tr class="even">
<td><p>Class of the master interface</p></td>
<td><p>Communication Interface Class (0x02).</p></td>
</tr>
<tr class="odd">
<td><p>Subclass of the master interface</p></td>
<td><p>ACM (0x02).</p></td>
</tr>
<tr class="even">
<td><p>Protocol</p></td>
<td><p>Any.</p></td>
</tr>
<tr class="odd">
<td><p>Enumerated</p></td>
<td><p>Yes.</p></td>
</tr>
<tr class="even">
<td><p>Related interfaces</p></td>
<td><p>One data class interface and optional audio class interfaces that the union functional descriptor (UFD) references.</p></td>
</tr>
<tr class="odd">
<td><p>Hardware IDs</p></td>
<td><pre space="preserve"><code>USB\Vid_%04x&amp;Pid_%04x&amp;Rev_%04x&amp;Cdc_02&amp;MI_%02x
USB\Vid_%04x&amp;Pid_%04x&amp;Rev_%04x&amp;Cdc_02
USB\Vid_%04x&amp;Pid_%04x&amp;Cdc_02&amp;MI_%02x
USB\Vid_%04x&amp;Pid_%04x&amp;Cdc_02</code></pre></td>
</tr>
<tr class="even">
<td><p>Compatible IDs</p></td>
<td><pre space="preserve"><code>USB\Class_02&amp;SubClass_02&amp;Prot_%02X
USB\Class_02&amp;SubClass_02
USB\Class_02</code></pre></td>
</tr>
<tr class="odd">
<td><p>Special handling</p></td>
<td><p>The UFD can reference an audio interface collection that is enumerated independently of the ACM interface collection.</p></td>
</tr>
</tbody>
</table>

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Busbcon\buses%5D:%20CDC%20Abstract%20Control%20Model%20%20RELEASE:%20%281/26/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


