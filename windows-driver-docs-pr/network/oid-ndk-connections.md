---
title: OID_NDK_CONNECTIONS
ms.topic: reference
description: As a query, NDIS and overlying drivers or user-mode applications use the OID_NDK_CONNECTIONS OID to query the list of active Network Direct connections from the miniport adapter.
ms.date: 08/08/2017
keywords: 
 -OID_NDK_CONNECTIONS Network Drivers Starting with Windows Vista
---

# OID\_NDK\_CONNECTIONS


As a query, NDIS and overlying drivers or user-mode applications use the OID\_NDK\_CONNECTIONS OID to query the list of active Network Direct connections from the miniport adapter.

NDIS 6.30 and later miniport drivers that provide NDK services must support this OID. Otherwise, this OID is optional.

## Remarks

NDIS issues this OID to obtain the list of active Network Direct connections from an adapter. The adapter must return the list of connections with the [**NDIS\_NDK\_CONNECTIONS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_ndk_connections) structure at the **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request) structure.

This structure is variable-sized based on the number of connections that are returned. The size of the connection array, as element count, is specified in the **Count** member.

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Minimum supported client</p></td>
<td><p>None supported</p></td>
</tr>
<tr class="even">
<td><p>Minimum supported server</p></td>
<td><p>Windows Server 2012</p></td>
</tr>
<tr class="odd">
<td><p>Version</p></td>
<td><p>Supported in NDIS 6.30 and later.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_NDK\_CONNECTIONS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_ndk_connections)

[**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request)

 

