---
title: OID_PNP_WAKE_UP_ERROR
description: OID_PNP_WAKE_UP_ERROR
ms.assetid: e6386a35-7077-45b3-bc0c-164477168a55
ms.date: 08/08/2017
keywords: 
 -OID_PNP_WAKE_UP_ERROR Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_PNP\_WAKE\_UP\_ERROR





The optional OID\_PNP\_WAKE\_UP\_ERROR OID indicates the number of false wake-ups that are signaled by the miniport driver's network adapter. A false wake-up occurs when the network adapter wakes up the system when it shouldn't have. For example, the network adapter could erroneously wake up the system due to an inexact pattern match.

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

 

 




