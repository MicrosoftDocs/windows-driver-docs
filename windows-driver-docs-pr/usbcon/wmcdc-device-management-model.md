---
Description: WMCDC Device Management Model
title: WMCDC Device Management Model
ms.localizationpriority: medium
ms.date: 01/07/2019
---

# WMCDC Device Management Model


USB WMCDC Device Management Model (DMM) interface collections have the following properties.

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
<td><p><em>Universal Serial Bus CDC Subclass Specification for Wireless Mobile Communication Devices</em>, version 1.0, Section 6.6.</p></td>
</tr>
<tr class="even">
<td><p>Class of the master interface</p></td>
<td><p>Communication Interface Class (0x02).</p></td>
</tr>
<tr class="odd">
<td><p>Subclass of the master interface</p></td>
<td><p>DMM (0x09).</p></td>
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
<td><p>None.</p></td>
</tr>
<tr class="odd">
<td><p>Hardware IDs</p></td>
<td><pre space="preserve"><code class="language-syntax">USB\Vid_%04x&Pid_%04x&Rev_%04x&Cdc_09&MI_%02x
USB\Vid_%04x&Pid_%04x&Rev_%04x&Cdc_09
USB\Vid_%04x&Pid_%04x&Cdc_09&MI_%02x
USB\Vid_%04x&Pid_%04x&Cdc_09</code></pre></td>
</tr>
<tr class="even">
<td><p>Compatible IDs</p></td>
<td><pre space="preserve"><code class="language-syntax">USB\Class_02&SubClass_09&Prot_%02X
USB\Class_02&SubClass_09
USB\Class_02</code></pre></td>
</tr>
<tr class="odd">
<td><p>Special handling</p></td>
<td><p>This control model does not use a union functional descriptor (UFD).</p></td>
</tr>
</tbody>
</table>

 

 

 




