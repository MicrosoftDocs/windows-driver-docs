---
Description: CDC Direct Line Control Model
title: CDC Direct Line Control Model
ms.localizationpriority: medium
ms.date: 01/07/2019
---

# CDC Direct Line Control Model


USB CDC Direct Line Control Model (DLCM) interface collections have the following properties.

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
<td><p><em>Universal Serial Bus Class Definitions for Communication Devices</em>, version 1.1, Section 3.6.1.</p></td>
</tr>
<tr class="even">
<td><p>Class of the master interface</p></td>
<td><p>Communication Interface Class (0x02).</p></td>
</tr>
<tr class="odd">
<td><p>Subclass of the master interface</p></td>
<td><p>DLCM (0x01).</p></td>
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
<td><p>Audio Class or vendor-defined interfaces that the union functional descriptor (UFD) references.</p></td>
</tr>
<tr class="odd">
<td><p>Hardware IDs</p></td>
<td><pre space="preserve"><code class="language-syntax">USB\Vid_%04x&Pid_%04x&Rev_%04x&Cdc_01&MI_%02x
USB\Vid_%04x&Pid_%04x&Rev_%04x&Cdc_01
USB\Vid_%04x&Pid_%04x&Cdc_01&MI_%02x
USB\Vid_%04x&Pid_%04x&Cdc_01</code></pre></td>
</tr>
<tr class="even">
<td><p>Compatible IDs</p></td>
<td><pre space="preserve"><code class="language-syntax">USB\Class_02&SubClass_01&Prot_00
USB\Class_02&SubClass_01
USB\Class_02</code></pre></td>
</tr>
<tr class="odd">
<td><p>Special handling</p></td>
<td><p>The UFD references an audio class interface collection that is enumerated independently of the DLCM interface collection.</p></td>
</tr>
</tbody>
</table>

 

 

 




