---
title: NdisOidDoubleComplete rule (ndis)
description: The NdisOidDoubleComplete rule specifies that an NDIS miniport driver must not call the NdisMOidRequestComplete routine twice for the same OID.
ms.assetid: 876A3D3C-554F-4D71-AD1B-F568D0AD6C0D
keywords: ["NdisOidDoubleComplete rule (ndis)"]
topic_type:
- apiref
api_name:
- NdisOidDoubleComplete
api_type:
- NA
---

# NdisOidDoubleComplete rule (ndis)


The **NdisOidDoubleComplete** rule specifies that an NDIS miniport driver must not call the [**NdisMOidRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff563622) routine twice for the same OID.

The OID is tracked ( TRACKED\_OBJECT). To help debug this error with the kernel debugger, use **!ndiskd.oid** debugger extension.

|              |      |
|--------------|------|
| Driver model | NDIS |

|                                   |                                                                                                                                        |
|-----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| Bug check(s) found with this rule | [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](https://msdn.microsoft.com/library/windows/hardware/ff560187) ( 0x00091002) |

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
<td align="left"><p>Run [Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff545448) and select the [NDIS/WIFI verification](https://msdn.microsoft.com/library/windows/hardware/dn312128) option. This rule is also tested with the [DDI compliance checking](https://msdn.microsoft.com/library/windows/hardware/hh454208) option.</p></td>
</tr>
</tbody>
</table>

 

.

Applies to
----------

[**MiniportOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff559416)
[**NdisMOidRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff563622)
 

 





