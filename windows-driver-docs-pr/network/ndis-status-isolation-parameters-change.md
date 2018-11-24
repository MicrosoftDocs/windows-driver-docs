---
title: NDIS_STATUS_ISOLATION_PARAMETERS_CHANGE
description: A VM network adapter miniport driver generates an NDIS_STATUS_ISOLATION_PARAMETERS_CHANGE status indication whenever the routing domain configuration is updated on the network adapter's port.
ms.assetid: 4F3916B6-F52D-4B99-8F1C-A4A5BA9B307B
ms.date: 08/08/2017
keywords: 
 -NDIS_STATUS_ISOLATION_PARAMETERS_CHANGE Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# NDIS\_STATUS\_ISOLATION\_PARAMETERS\_CHANGE


A VM network adapter miniport driver generates an **NDIS\_STATUS\_ISOLATION\_PARAMETERS\_CHANGE** status indication whenever the routing domain configuration is updated on the network adapter's port. This triggers the TCP layer to re-query the multi-tenancy configuration by issuing an [OID\_GEN\_ISOLATION\_PARAMETERS](oid-gen-isolation-parameters.md) OID. This status indication does not have a status buffer.

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
[**NDIS\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567373)

[OID\_GEN\_ISOLATION\_PARAMETERS](oid-gen-isolation-parameters.md)

 

 




