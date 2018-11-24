---
title: MB Miniport Driver Types
description: MB Miniport Driver Types
ms.assetid: ec1743a1-4c5e-4960-b352-40fc5b9c016a
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# MB Miniport Driver Types


Based on data packet handling, DHCP Server and ARP emulations, multiple MB miniport driver implementation types are possible. The following table represents the different possible implementation types and the required implementation for production quality miniport drivers.

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Description</th>
<th align="left">MediaType</th>
<th align="left">EnableDhcp</th>
<th align="left">ARP emulation</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Ethernet emulation with DHCP emulation</p></td>
<td align="left"><p>NdisMedium802_3</p></td>
<td align="left"><p>1</p></td>
<td align="left"><p>Required</p></td>
</tr>
<tr class="even">
<td align="left"><p>Ethernet emulation with no DHCP</p></td>
<td align="left"><p>NdisMedium802_3</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>Required</p></td>
</tr>
<tr class="odd">
<td align="left"><p>IP packet handling with DHCP emulation</p></td>
<td align="left"><p>NdisMediumWirelessWan</p></td>
<td align="left"><p>1</p></td>
<td align="left"><p>Not required</p></td>
</tr>
<tr class="even">
<td align="left"><p>IP packet handling capability</p></td>
<td align="left"><p>NdisMediumWirelessWan</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>Not Required</p></td>
</tr>
</tbody>
</table>

 

During development or migration phases, miniport drivers can specify any of first three entries. However, production quality miniport drivers should use only the settings specified in the last entry of the table ("IP packet handling capability").

Production quality MB miniport drivers should specify the settings in the following table in the INF file.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Field in INF file</th>
<th align="left">Recommended value(s)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>*IfType</p></td>
<td align="left"><p>IF_TYPE_WWANPP / IF_TYPE_WWANPP2</p></td>
</tr>
<tr class="even">
<td align="left"><p>MediaType</p></td>
<td align="left"><p>NdisMediumWirelessWan</p></td>
</tr>
<tr class="odd">
<td align="left"><p>EnableDhcp</p></td>
<td align="left"><p>0</p></td>
</tr>
<tr class="even">
<td align="left"><p>UpperRange</p></td>
<td align="left"><p>&quot;flpp4&quot; and &quot;flpp6&quot; (if IPv6 supported)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>LowerRange</p></td>
<td align="left"><p>&quot;ppip&quot;</p></td>
</tr>
</tbody>
</table>

 

 

 





