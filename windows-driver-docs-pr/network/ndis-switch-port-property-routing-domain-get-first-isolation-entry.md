---
title: NDIS_SWITCH_PORT_PROPERTY_ROUTING_DOMAIN_GET_FIRST_ISOLATION_ENTRY macro
author: windows-driver-content
description: The NDIS_SWITCH_PORT_PROPERTY_ROUTING_DOMAIN_GET_FIRST_ISOLATION_ENTRY macro is used to access the first NDIS_ROUTING_DOMAIN_ISOLATION_ENTRY that is specified by an NDIS_SWITCH_PORT_PROPERTY_ROUTING_DOMAIN structure.
ms.assetid: AB873417-5FBD-4D01-92E7-B9BF466333BC
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -NDIS_SWITCH_PORT_PROPERTY_ROUTING_DOMAIN_GET_FIRST_ISOLATION_ENTRY macro Network Drivers Starting with Windows Vista
---

# NDIS\_SWITCH\_PORT\_PROPERTY\_ROUTING\_DOMAIN\_GET\_FIRST\_ISOLATION\_ENTRY macro


The **NDIS\_SWITCH\_PORT\_PROPERTY\_ROUTING\_DOMAIN\_GET\_FIRST\_ISOLATION\_ENTRY** macro is used to access the first [**NDIS\_ROUTING\_DOMAIN\_ISOLATION\_ENTRY**](https://msdn.microsoft.com/library/windows/hardware/dn383684) that is specified by an [**NDIS\_SWITCH\_PORT\_PROPERTY\_ROUTING\_DOMAIN**](https://msdn.microsoft.com/library/windows/hardware/dn383688) structure.

Syntax
------

```ManagedCPlusPlus
PNDIS_ROUTING_DOMAIN_ISOLATION_ENTRY NDIS_SWITCH_PORT_PROPERTY_ROUTING_DOMAIN_GET_FIRST_ISOLATION_ENTRY(
   PNDIS_SWITCH_PORT_PROPERTY_ROUTING_DOMAIN _RoutingDomainProperty_
);
```

Parameters
----------

*\_RoutingDomainProperty\_*   
A pointer to an [**NDIS\_SWITCH\_PORT\_PROPERTY\_ROUTING\_DOMAIN**](https://msdn.microsoft.com/library/windows/hardware/dn383688) structure.

Return value
------------

The **NDIS\_SWITCH\_PORT\_PROPERTY\_ROUTING\_DOMAIN\_GET\_FIRST\_ISOLATION\_ENTRY** macro returns a pointer to the first [**NDIS\_ROUTING\_DOMAIN\_ISOLATION\_ENTRY**](https://msdn.microsoft.com/library/windows/hardware/dn383684).

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


[**NDIS\_ROUTING\_DOMAIN\_ISOLATION\_ENTRY**](https://msdn.microsoft.com/library/windows/hardware/dn383684)

[**NDIS\_SWITCH\_PORT\_PROPERTY\_ROUTING\_DOMAIN**](https://msdn.microsoft.com/library/windows/hardware/dn383688)

 

 




