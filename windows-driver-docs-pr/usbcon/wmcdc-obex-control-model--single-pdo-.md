---
Description: 'WMCDC OBEX Control Model (Single PDO)'
MS-HAID:
- 'usbsystem\_9f6bd2d7-9d48-4cdb-9158-ba35ac7e9e1d.xml'
- 'buses.wmcdc\_obex\_control\_model\_\_single\_pdo\_'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
title: 'WMCDC OBEX Control Model (Single PDO)'
---

# WMCDC OBEX Control Model (Single PDO)


There are two ways to enumerate Object Exchange Protocol (OBEX) control model interface collections: the USB generic parent driver can group all of the OBEX interfaces together and create a single physical device object (PDO) for all of the OBEX interfaces, or the parent driver can create a separate PDO for each OBEX interface. For a description of the hardware IDs that the USB generic parent driver generates for OBEX interfaces that are enumerated separately, see [WMCDC OBEX Control Model (Multiple PDOs)](wmcdc-obex-control-model--multiple-pdos-.md).

When the USB generic parent driver assigns a single PDO to all of the OBEX interfaces, the PDO has the following properties.

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
<td><p><em>Universal Serial Bus CDC Subclass Specification for Wireless Mobile Communication Devices</em>, version 1.0, Section 6.5.</p></td>
</tr>
<tr class="even">
<td><p>Class of the master interface</p></td>
<td><p>Communication Interface Class (0x02).</p></td>
</tr>
<tr class="odd">
<td><p>Subclass of the master interface</p></td>
<td><p>OBEX (0x0B).</p></td>
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
<td><p>One data class interface that the union functional descriptor (UFD) references.</p></td>
</tr>
<tr class="odd">
<td><p>Hardware IDs</p></td>
<td><pre space="preserve"><code>USB\Vid_%04x&amp;Pid_%04x&amp;Rev_%04x&amp;WPD_OBEX&amp;MI_%02x
USB\Vid_%04x&amp;Pid_%04x&amp;Rev_%04x&amp;WPD_OBEX
USB\Vid_%04x&amp;Pid_%04x&amp;WPD_OBEX&amp;MI_%02x
USB\Vid_%04x&amp;Pid_%04x&amp;WPD_OBEX</code></pre></td>
</tr>
<tr class="even">
<td><p>Compatible IDs</p></td>
<td><pre space="preserve"><code>USB\Class_02&amp;WPD_OBEX
USB\Class_02</code></pre></td>
</tr>
<tr class="odd">
<td><p>Special handling</p></td>
<td><p>The registry settings that are associated with the instance of the USB generic parent driver that manages the composite device determine whether OBEX interfaces are managed with a single PDO or multiple PDOs. For an explanation of the registry settings that specify how the USB generic parent driver enumerates OBEX interfaces, see [Enumerating Interface Collections on Wireless Mobile Communication Devices](enumerating-interface-collections-on-wireless-mobile-communication-dev.md).</p></td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Busbcon\buses%5D:%20WMCDC%20OBEX%20Control%20Model%20%28Single%20PDO%29%20%20RELEASE:%20%281/26/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")



