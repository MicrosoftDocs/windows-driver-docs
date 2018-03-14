---
title: NDIS_ROUTING_DOMAIN_ISOLATION_ENTRY_GET_NEXT macro
author: windows-driver-content
description: Hyper-V extensible switch extensions use the NDIS_ROUTING_DOMAIN_ISOLATION_ENTRY_GET_NEXT macro to access the next NDIS_ROUTING_DOMAIN_ISOLATION_ENTRY element that follows an NDIS_ROUTING_DOMAIN_ISOLATION_ENTRY structure in the array that is specified by an NDIS_SWITCH_PORT_PROPERTY_ROUTING_DOMAIN structure.
ms.assetid: DFBBD989-08E5-48A3-9D03-C6F914753131
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -NDIS_ROUTING_DOMAIN_ISOLATION_ENTRY_GET_NEXT macro Network Drivers Starting with Windows Vista
---

# NDIS\_ROUTING\_DOMAIN\_ISOLATION\_ENTRY\_GET\_NEXT macro


Hyper-V extensible switch extensions use the **NDIS\_ROUTING\_DOMAIN\_ISOLATION\_ENTRY\_GET\_NEXT** macro to access the next [**NDIS\_ROUTING\_DOMAIN\_ISOLATION\_ENTRY**](https://msdn.microsoft.com/library/windows/hardware/dn383684) element that follows an **NDIS\_ROUTING\_DOMAIN\_ISOLATION\_ENTRY** structure in the array that is specified by an [**NDIS\_SWITCH\_PORT\_PROPERTY\_ROUTING\_DOMAIN**](https://msdn.microsoft.com/library/windows/hardware/dn383688) structure.

Syntax
------

```ManagedCPlusPlus
PNDIS_ROUTING_DOMAIN_ISOLATION_ENTRY NDIS_ROUTING_DOMAIN_ISOLATION_ENTRY_GET_NEXT(
   PNDIS_ROUTING_DOMAIN_ISOLATION_ENTRY _IsolationInfoEntry_
);
```

Parameters
----------

*\_IsolationInfoEntry\_*   
A pointer to an [**NDIS\_ROUTING\_DOMAIN\_ISOLATION\_ENTRY**](https://msdn.microsoft.com/library/windows/hardware/dn383684) structure.

Return value
------------

The **NDIS\_ROUTING\_DOMAIN\_ISOLATION\_ENTRY\_GET\_NEXT** macro returns a pointer to the next [**NDIS\_ROUTING\_DOMAIN\_ISOLATION\_ENTRY**](https://msdn.microsoft.com/library/windows/hardware/dn383684) element in the array. If the *\_IsolationInfoEntry\_* parameter already points to the last element in the array, the macro returns **NULL**.

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

 

 




