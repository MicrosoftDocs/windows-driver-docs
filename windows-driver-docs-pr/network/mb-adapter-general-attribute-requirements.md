---
title: MB Adapter General Attribute Requirements
description: MB Adapter General Attribute Requirements
ms.date: 04/20/2017
ms.custom: UpdateFrequency3
---

# MB Adapter General Attribute Requirements


The following table describes the values that miniport drivers should set the member variables of the [**NDIS\_MINIPORT\_ADAPTER\_GENERAL\_ATTRIBUTES**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_miniport_adapter_general_attributes) structure to. MB miniport drivers must use these values when they call [**NdisMSetMiniportAttributes**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismsetminiportattributes) from their [*MiniportInitializeEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_initialize) function, during miniport driver initialization.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Field in INF file</th>
<th align="left">Recommended values</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>IfType</p></td>
<td align="left"><p>GSM-based devices must specify IF_TYPE_WWANPP.</p>
<p>CDMA-based devices specify IF_TYPE_WWANPP2.</p>
<p>The value must match the *IfType value specified in the miniport driver's INF file.</p></td>
</tr>
<tr class="even">
<td align="left"><p>MediaType</p></td>
<td align="left"><p>The value must match the *MediaType value specified in the miniport driver's INF file. For example, either <strong>NdisMediumWirelessWan</strong> or <strong>NdisMedium802_3</strong>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>PhysicalMediumType</p></td>
<td align="left"><p>The value must match the *PhysicalMediaType value specified in the miniport driver's INF file. The value must be <strong>NdisPhysicalMediumWirelessWan</strong>.</p></td>
</tr>
<tr class="even">
<td align="left"><p>AccessType</p></td>
<td align="left"><p>If the value in MediaType is specified as <strong>NdisMediumWirelessWan</strong>, specify <strong>NET_IF_ACCESS_POINT_TO_POINT</strong> for AccessType. If MediaType is <strong>NdisMedium802_3</strong>, specify NET_IF_ACCESS_BROADCAST.</p></td>
</tr>
</tbody>
</table>

 

 

