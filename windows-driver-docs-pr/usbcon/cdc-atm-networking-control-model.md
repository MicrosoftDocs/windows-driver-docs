---
Description: CDC ATM Networking Control Model
title: CDC ATM Networking Control Model
ms.localizationpriority: medium
ms.date: 01/07/2019
---

# CDC ATM Networking Control Model


USB CDC ATM Networking Control Model (ANCM) interface collections have the following properties.

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
<td><p><em>Universal Serial Bus Class Definitions for Communication Devices</em>, version 1.1, Section 3.8.3</p></td>
</tr>
<tr class="even">
<td><p>Class of the master interface</p></td>
<td><p>Communication Interface Class (0x02)</p></td>
</tr>
<tr class="odd">
<td><p>Subclass of the master interface</p></td>
<td><p>ANCM (0x07)</p></td>
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
<td><p>One data class interface that is referenced by the Union Functional Descriptor (UFD)</p></td>
</tr>
<tr class="odd">
<td><p>Hardware IDs</p></td>
<td><pre space="preserve"><code class="language-syntax">USB\Vid_%04x&Pid_%04x&Rev_%04x&Cdc_07&MI_%02x
USB\Vid_%04x&Pid_%04x&Rev_%04x&Cdc_07
USB\Vid_%04x&Pid_%04x&Cdc_07&MI_%02x
USB\Vid_%04x&Pid_%04x&Cdc_07</code></pre></td>
</tr>
<tr class="even">
<td><p>Compatible IDs</p></td>
<td><pre space="preserve"><code class="language-syntax">USB\Class_02&SubClass_07&Prot_00
USB\Class_02&SubClass_07
USB\Class_02</code></pre></td>
</tr>
<tr class="odd">
<td><p>Special handling</p></td>
<td><p>None</p></td>
</tr>
</tbody>
</table>

 

 

 




