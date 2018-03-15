---
title: NDIS_ROUTING_DOMAIN_ENTRY_GET_NEXT macro
author: windows-driver-content
description: The NDIS_ROUTING_DOMAIN_ENTRY_GET_NEXT macro is used to access the next NDIS_ROUTING_DOMAIN_ENTRY element that follows an NDIS_ROUTING_DOMAIN_ENTRY structure in the array that is specified by an NDIS_ISOLATION_PARAMETERS structure.
ms.assetid: 134A6FBD-24BF-4401-9226-6706EE6D7CF2
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -NDIS_ROUTING_DOMAIN_ENTRY_GET_NEXT macro Network Drivers Starting with Windows Vista
---

# NDIS\_ROUTING\_DOMAIN\_ENTRY\_GET\_NEXT macro


The **NDIS\_ROUTING\_DOMAIN\_ENTRY\_GET\_NEXT** macro is used to access the next [**NDIS\_ROUTING\_DOMAIN\_ENTRY**](https://msdn.microsoft.com/library/windows/hardware/dn383681) element that follows an **NDIS\_ROUTING\_DOMAIN\_ENTRY** structure in the array that is specified by an [**NDIS\_ISOLATION\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/dn383679) structure.

Syntax
------

```ManagedCPlusPlus
PNDIS_ROUTING_DOMAIN_ENTRY NDIS_ROUTING_DOMAIN_ENTRY_GET_NEXT(
   PNDIS_ROUTING_DOMAIN_ENTRY _RoutingDomainEntry_
);
```

Parameters
----------

*\_RoutingDomainEntry\_*   
A pointer to an [**NDIS\_ROUTING\_DOMAIN\_ENTRY**](https://msdn.microsoft.com/library/windows/hardware/dn383681) structure.

Return value
------------

The **NDIS\_ROUTING\_DOMAIN\_ENTRY\_GET\_NEXT** macro returns a pointer to the next [**NDIS\_ROUTING\_DOMAIN\_ENTRY**](https://msdn.microsoft.com/library/windows/hardware/dn383681) element in the array. If the *\_RoutingDomainEntry\_* parameter already points to the last element in the array, the macro returns **NULL**.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Target platform</p></td>
<td>Desktop</td>
</tr>
<tr class="even">
<td><p>Version</p></td>
<td><p>Supported in NDIS 6.40 and later.</p></td>
</tr>
<tr class="odd">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_ISOLATION\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/dn383679)

[**NDIS\_ISOLATION\_PARAMETERS\_GET\_FIRST\_ROUTING\_DOMAIN\_ENTRY**](ndis-isolation-parameters-get-first-routing-domain-entry.md)

[**NDIS\_ROUTING\_DOMAIN\_ENTRY**](https://msdn.microsoft.com/library/windows/hardware/dn383681)

 

 




