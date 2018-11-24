---
title: OID_PM_PROTOCOL_OFFLOAD_LIST
description: As a query, overlying drivers can use the OID_PM_PROTOCOL_OFFLOAD_LIST OID to enumerate the protocol offloads that are set on an underlying network adapter.
ms.assetid: 95ace77b-e583-4611-8460-af67b4d4805d
ms.date: 08/08/2017
keywords: 
 -OID_PM_PROTOCOL_OFFLOAD_LIST Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_PM\_PROTOCOL\_OFFLOAD\_LIST


As a query, overlying drivers can use the OID\_PM\_PROTOCOL\_OFFLOAD\_LIST OID to enumerate the protocol offloads that are set on an underlying network adapter. After a successful return from the OID query request, the **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure contains a pointer to a list of [**NDIS\_PM\_PROTOCOL\_OFFLOAD**](https://msdn.microsoft.com/library/windows/hardware/ff566760) structures that describe the currently active protocol offloads.

Remarks
-------

NDIS handles the query for miniport drivers. NDIS drivers can use the OID\_PM\_PROTOCOL\_OFFLOAD\_LIST OID to get a list of protocol offloads that are set on an underlying network adapter.

For each [**NDIS\_PM\_PROTOCOL\_OFFLOAD**](https://msdn.microsoft.com/library/windows/hardware/ff566760) structure in the list, NDIS sets the **NextProtocolOffloadOffset** member to the offset from the beginning of the OID information buffer (that is, the beginning of the buffer that the **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure points to) to the beginning of the next NDIS\_PM\_PROTOCOL\_OFFLOAD structure in the list. The offset in the **NextProtocolOffloadOffset** member of the last structure in the list is zero.

If there are no protocol offloads that are set on the network adapter, NDIS sets the **DATA.QUERY\_INFORMATION.BytesWritten** member of the NDIS\_OID\_REQUEST structure to zero and returns NDIS\_STATUS\_SUCCESS. The data within the **DATA.QUERY\_INFORMATION.InformationBuffer** member is not modified by NDIS.

NDIS returns one of the following status codes for the request:

<a href="" id="ndis-status-success"></a>NDIS\_STATUS\_SUCCESS  
The request completed successfully. The **InformationBuffer** contains a pointer to a list of protocol offloads, if any.

<a href="" id="ndis-status-pending"></a>NDIS\_STATUS\_PENDING  
The request is pending completion. The final status code and results will be passed to the OID request completion handler of the caller.

<a href="" id="ndis-status-buffer-too-short"></a>NDIS\_STATUS\_BUFFER\_TOO\_SHORT  
The information buffer was too short. NDIS set the **DATA.QUERY\_INFORMATION.BytesNeeded** member in the NDIS\_OID\_REQUEST structure to the minimum buffer size that is required.

<a href="" id="ndis-status-failure"></a>NDIS\_STATUS\_FAILURE  
The request failed for reasons other than the preceding reasons.

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
<td><p>Supported in NDIS 6.20 and later. Not requested for miniport drivers. (See Remarks section.)</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710)

[**NDIS\_PM\_PROTOCOL\_OFFLOAD**](https://msdn.microsoft.com/library/windows/hardware/ff566760)

 

 




