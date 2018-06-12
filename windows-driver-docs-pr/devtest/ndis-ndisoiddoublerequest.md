---
title: NdisOidDoubleRequest rule (ndis)
description: This NdisOidDoubleRequest rule verifies that Minport driver must complete the NDIS\_OID\_REQUEST that is currently pending.
ms.assetid: 67B179ED-EEAF-4717-B714-9601BE806269
ms.author: windowsdriverdev
ms.date: 5/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["NdisOidDoubleRequest rule (ndis)"]
topic_type:
- apiref
api_name:
- NdisOidDoubleRequest
api_type:
- NA
---

# NdisOidDoubleRequest rule (ndis)


This **NdisOidDoubleRequest** rule verifies that:

-   Minport driver must complete the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) that is currently pending.

|              |      |
|--------------|------|
| Driver model | NDIS |

|                                   |                                                                                                                                        |
|-----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| Bug check(s) found with this rule | [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](https://msdn.microsoft.com/library/windows/hardware/ff560187) ( 0x0009100E) |

How to test
-----------

<table>
<colgroup>
<col width="100%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">At run time</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Run [Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff545448) and select the [NDIS/WIFI verification](https://msdn.microsoft.com/library/windows/hardware/dn312128) option.</p></td>
</tr>
</tbody>
</table>

 

Applies to
----------

[**MiniportOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff559416)
[**NdisMOidRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff563622)
 

 





