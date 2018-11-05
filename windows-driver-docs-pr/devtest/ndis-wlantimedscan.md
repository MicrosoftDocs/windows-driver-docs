---
title: WlanTimedScan rule (ndis)
description: The WlanTimedScan rule verifies that a WLAN scan operation is completed within 15 seconds.
ms.assetid: 6BFA0DAD-00A4-43EB-A226-40E1B0892E91
ms.date: 05/21/2018
keywords: ["WlanTimedScan rule (ndis)"]
topic_type:
- apiref
api_name:
- WlanTimedScan
api_type:
- NA
ms.localizationpriority: medium
---

# WlanTimedScan rule (ndis)


The **WlanTimedScan** rule verifies that a WLAN scan operation is completed within 15 seconds.

|              |      |
|--------------|------|
| Driver model | NDIS |

|                                   |                                                                                                                                       |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Bug check(s) found with this rule | [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](https://msdn.microsoft.com/library/windows/hardware/ff560187) (0x0009400C) |

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
<td align="left"><p>Run <a href="https://msdn.microsoft.com/library/windows/hardware/ff545448" data-raw-source="[Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff545448)">Driver Verifier</a> and select the <a href="https://msdn.microsoft.com/library/windows/hardware/dn312128" data-raw-source="[NDIS/WIFI verification](https://msdn.microsoft.com/library/windows/hardware/dn312128)">NDIS/WIFI verification</a> option.</p></td>
</tr>
</tbody>
</table>

 

Applies to
----------

[**MiniportHaltEx**](https://msdn.microsoft.com/library/windows/hardware/ff559388)
[**MiniportOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff559416)
[**NdisMIndicateStatusEx**](https://msdn.microsoft.com/library/windows/hardware/ff563600)
[**NdisMOidRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff563622)
See also
--------

[General Connection Operation Guidelines](https://msdn.microsoft.com/library/windows/hardware/ff552458)
[OID\_DOT11\_CONNECT\_REQUEST](https://msdn.microsoft.com/library/windows/hardware/ff569122)
[NDIS\_STATUS\_DOT11\_CONNECTION\_START](https://msdn.microsoft.com/library/windows/hardware/ff567328)
 

 





