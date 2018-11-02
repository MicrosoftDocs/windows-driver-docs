---
title: Standardized INF keywords for NVGRE Task Offload
description: This section describes standardized keywords used in INF files for NVGRE-capable drivers
ms.assetid: C1FB0519-6BB7-46B0-A3FA-B8E982279C44
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Standardized INF Keywords for NVGRE Task Offload


The **\*EncapsulatedPacketTaskOffload** standardized enumeration keyword is defined to enable or disable support for [Network Virtualization using Generic Routing Encapsulation (NVGRE) Task Offload](network-virtualization-using-generic-routing-encapsulation--nvgre--task-offload.md) in miniport adapters.

The following table describes the possible INF entries for this keyword.

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">SubkeyName</th>
<th align="left">ParamDesc</th>
<th align="left">Value</th>
<th align="left">EnumDesc</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>*EncapsulatedPacketTaskOffload</strong></p></td>
<td align="left"><p>Encapsulated Task Offload</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>Disabled</p></td>
</tr>
<tr class="even">
<td align="left"></td>
<td align="left"></td>
<td align="left"><p>1</p>
(Default)</td>
<td align="left"><p>Enabled</p></td>
</tr>
</tbody>
</table>

 

For more information about standardized INF keywords, see [Standardized INF Keywords for Network Devices](standardized-inf-keywords-for-network-devices.md).

 

 





