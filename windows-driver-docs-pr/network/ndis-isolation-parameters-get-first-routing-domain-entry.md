---
title: NDIS_ISOLATION_PARAMETERS_GET_FIRST_ROUTING_DOMAIN_ENTRY macro
author: windows-driver-content
description: The NDIS_ISOLATION_PARAMETERS_GET_FIRST_ROUTING_DOMAIN_ENTRY macro is used to access the first NDIS_ROUTING_DOMAIN_ENTRY that is specified by an NDIS_ISOLATION_PARAMETERS structure.
ms.assetid: 81BFFFAF-89D7-4C21-92C9-D17A92097877
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -NDIS_ISOLATION_PARAMETERS_GET_FIRST_ROUTING_DOMAIN_ENTRY macro Network Drivers Starting with Windows Vista
---

# NDIS\_ISOLATION\_PARAMETERS\_GET\_FIRST\_ROUTING\_DOMAIN\_ENTRY macro


The **NDIS\_ISOLATION\_PARAMETERS\_GET\_FIRST\_ROUTING\_DOMAIN\_ENTRY** macro is used to access the first [**NDIS\_ROUTING\_DOMAIN\_ENTRY**](https://msdn.microsoft.com/library/windows/hardware/dn383681) that is specified by an [**NDIS\_ISOLATION\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/dn383679) structure.

Syntax
------

```ManagedCPlusPlus
PNDIS_ROUTING_DOMAIN_ENTRY NDIS_ISOLATION_PARAMETERS_GET_FIRST_ROUTING_DOMAIN_ENTRY(
   PNDIS_ISOLATION_PARAMETERS _MultiTenancyInfo_
);
```

Parameters
----------

*\_MultiTenancyInfo\_*   
A pointer to an [**NDIS\_ISOLATION\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/dn383679) structure.

Return value
------------

The **NDIS\_ISOLATION\_PARAMETERS\_GET\_FIRST\_ROUTING\_DOMAIN\_ENTRY** macro returns a pointer to the first [**NDIS\_ROUTING\_DOMAIN\_ENTRY**](https://msdn.microsoft.com/library/windows/hardware/dn383681) element in the array.

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

[**NDIS\_ROUTING\_DOMAIN\_ENTRY**](https://msdn.microsoft.com/library/windows/hardware/dn383681)

 

 




