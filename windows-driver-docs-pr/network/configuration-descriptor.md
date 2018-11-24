---
title: Configuration Descriptor
description: Configuration Descriptor
ms.assetid: 256edfa8-de02-438d-b4ce-0a2df0d0f46e
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Configuration Descriptor





<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Offset</th>
<th align="left">Field</th>
<th align="left">Size</th>
<th align="left">Value</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>0</p></td>
<td align="left"><p>bLength</p></td>
<td align="left"><p>1</p></td>
<td align="left"><p>0x09</p></td>
<td align="left"><p>Size of this descriptor, in bytes</p></td>
</tr>
<tr class="even">
<td align="left"><p>1</p></td>
<td align="left"><p>bDescriptorType</p></td>
<td align="left"><p>1</p></td>
<td align="left"><p>0x02</p></td>
<td align="left"><p>CONFIGURATION descriptor</p></td>
</tr>
<tr class="odd">
<td align="left"><p>2</p></td>
<td align="left"><p>wTotalLength</p></td>
<td align="left"><p>2</p></td>
<td align="left"><p>0x003E</p></td>
<td align="left"><p>Length of the total configuration block, including this descriptor and all following descriptors, in bytes</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>bNumInterfaces</p></td>
<td align="left"><p>1</p></td>
<td align="left"><p>0x02</p></td>
<td align="left"><p>Two interfaces</p></td>
</tr>
<tr class="odd">
<td align="left"><p>5</p></td>
<td align="left"><p>bConfigurationValue</p></td>
<td align="left"><p>1</p></td>
<td align="left"><p>0x01</p></td>
<td align="left"><p>ID of this configuration</p></td>
</tr>
<tr class="even">
<td align="left"><p>6</p></td>
<td align="left"><p>iConfiguration</p></td>
<td align="left"><p>1</p></td>
<td align="left"><p>0x00</p></td>
<td align="left"><p>Unused</p></td>
</tr>
<tr class="odd">
<td align="left"><p>7</p></td>
<td align="left"><p>bmAttributes</p></td>
<td align="left"><p>1</p></td>
<td align="left"><p>0x80</p></td>
<td align="left"><p>Bus Powered</p></td>
</tr>
<tr class="even">
<td align="left"><p>8</p></td>
<td align="left"><p>MaxPower</p></td>
<td align="left"><p>1</p></td>
<td align="left"><p>0x64</p></td>
<td align="left"><p>200 mA</p></td>
</tr>
</tbody>
</table>

 

 

 





