---
title: NDIS_STATUS_ISOLATION_PARAMETERS_CHANGE
ms.topic: reference
description: A VM network adapter miniport driver generates an NDIS_STATUS_ISOLATION_PARAMETERS_CHANGE status indication whenever the routing domain configuration is updated on the network adapter's port.
ms.date: 03/02/2023
keywords: 
 -NDIS_STATUS_ISOLATION_PARAMETERS_CHANGE Network Drivers Starting with Windows Vista
---

# NDIS\_STATUS\_ISOLATION\_PARAMETERS\_CHANGE


A VM network adapter miniport driver generates an **NDIS\_STATUS\_ISOLATION\_PARAMETERS\_CHANGE** status indication whenever the routing domain configuration is updated on the network adapter's port. This triggers the TCP layer to re-query the multi-tenancy configuration by issuing an [OID\_GEN\_ISOLATION\_PARAMETERS](oid-gen-isolation-parameters.md) OID. This status indication does not have a status buffer.

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Version</p></td>
<td><p>Supported in NDIS 6.40 and later.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ndis.h</td>
</tr>
</tbody>
</table>

## See also


****
[**NDIS\_STATUS\_INDICATION**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_status_indication)

[OID\_GEN\_ISOLATION\_PARAMETERS](oid-gen-isolation-parameters.md)

 

