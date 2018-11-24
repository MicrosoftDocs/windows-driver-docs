---
title: OID_PNP_WAKE_UP_OK
description: OID_PNP_WAKE_UP_OK
ms.assetid: 93389bfe-11b9-4433-8eca-4446f05d01c0
ms.date: 08/08/2017
keywords: 
 -OID_PNP_WAKE_UP_OK Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_PNP\_WAKE\_UP\_OK





The optional OID\_PNP\_WAKE\_UP\_OK OID indicates the number of valid wake-ups that are signaled by the miniport driver's NIC. A valid wake-up occurs when the NIC wakes up the system in response to a valid pattern match or magic packet.

The data type for this OID is a ULONG value.

An intermediate driver in which the upper edge receives this OID request must always propagate the request to the underlying miniport driver by calling Ndis(Co)Request.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Version</p></td>
<td><p>Supported for NDIS 5.1, and NDIS 6.0 and later.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

 

 




