---
title: NDIS_ROUTING_DOMAIN_ENTRY_GET_FIRST_ISOLATION_ENTRY macro
author: windows-driver-content
description: The NDIS_ROUTING_DOMAIN_ENTRY_GET_FIRST_ISOLATION_ENTRY macro is used to access the first NDIS_ROUTING_DOMAIN_ISOLATION_ENTRY that is specified by an NDIS_ROUTING_DOMAIN_ENTRY structure.
ms.assetid: 02000ABE-15CB-4893-8BF1-2B5D6C5767EC
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -NDIS_ROUTING_DOMAIN_ENTRY_GET_FIRST_ISOLATION_ENTRY macro Network Drivers Starting with Windows Vista
---

# NDIS\_ROUTING\_DOMAIN\_ENTRY\_GET\_FIRST\_ISOLATION\_ENTRY macro


The **NDIS\_ROUTING\_DOMAIN\_ENTRY\_GET\_FIRST\_ISOLATION\_ENTRY** macro is used to access the first [**NDIS\_ROUTING\_DOMAIN\_ISOLATION\_ENTRY**](https://msdn.microsoft.com/library/windows/hardware/dn383684) that is specified by an [**NDIS\_ROUTING\_DOMAIN\_ENTRY**](https://msdn.microsoft.com/library/windows/hardware/dn383681) structure.

Syntax
------

```ManagedCPlusPlus
PNDIS_ROUTING_DOMAIN_ISOLATION_ENTRY NDIS_ROUTING_DOMAIN_ENTRY_GET_FIRST_ISOLATION_ENTRY(
   PNDIS_ROUTING_DOMAIN_ENTRY _RoutingDomainEntry_
);
```

Parameters
----------

*\_RoutingDomainEntry\_*   
A pointer to an [**NDIS\_ROUTING\_DOMAIN\_ENTRY**](https://msdn.microsoft.com/library/windows/hardware/dn383681) structure.

Return value
------------

The **NDIS\_ROUTING\_DOMAIN\_ENTRY\_GET\_FIRST\_ISOLATION\_ENTRY** macro returns a pointer to the first [**NDIS\_ROUTING\_DOMAIN\_ISOLATION\_ENTRY**](https://msdn.microsoft.com/library/windows/hardware/dn383684) element in the array.

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


[**NDIS\_ROUTING\_DOMAIN\_ENTRY**](https://msdn.microsoft.com/library/windows/hardware/dn383681)

[**NDIS\_ROUTING\_DOMAIN\_ISOLATION\_ENTRY**](https://msdn.microsoft.com/library/windows/hardware/dn383684)

 

 




