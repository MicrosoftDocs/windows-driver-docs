---
title: Querying and Changing RSC State
description: This section describes how to query or change the current receive segment coalescing (RSC) state of an RSC-capable miniport driver.
ms.assetid: 5455FBB2-3603-44EF-B1C6-494D31DD820D
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Querying and Changing RSC State


This section describes how to query or change the current receive segment coalescing (RSC) state of an RSC-capable miniport driver.

## Querying RSC State


The current RSC state can be queried by issuing the [OID\_TCP\_OFFLOAD\_CURRENT\_CONFIG](https://msdn.microsoft.com/library/windows/hardware/ff569805) OID request. NDIS handles this OID and does not pass it down to the miniport.

## Changing RSC State


RSC can be enabled or disabled by issuing the [OID\_TCP\_OFFLOAD\_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/ff569807) OID request. This OID uses an [**NDIS\_OFFLOAD\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff566706) structure. In this structure, the **RscIPv4** and **RscIPv6** members can have the following values:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Term</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>NDIS_OFFLOAD_PARAMETERS_NO_CHANGE</strong></p></td>
<td align="left"><p>The RSC state is unchanged.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>NDIS_OFFLOAD_PARAMETERS_RSC_DISABLED</strong></p></td>
<td align="left"><p>Specify this flag to disable RSC.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>NDIS_OFFLOAD_PARAMETERS_RSC_ENABLED</strong></p></td>
<td align="left"><p>Specify this flag to enable RSC.</p></td>
</tr>
</tbody>
</table>

 

After the miniport driver processes the [OID\_TCP\_OFFLOAD\_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/ff569807) OID request, it must give an [**NDIS\_STATUS\_TASK\_OFFLOAD\_CURRENT\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff567424) status indication with the updated offload state.

When a miniport driver receives a [OID\_TCP\_OFFLOAD\_CURRENT\_CONFIG](https://msdn.microsoft.com/library/windows/hardware/ff569805) OID request in which the **NDIS\_OFFLOAD\_PARAMETERS\_RSC\_DISABLED** flag is specified, the driver must indicate any existing coalesced segments up the stack before completing the OID request.

 

 





