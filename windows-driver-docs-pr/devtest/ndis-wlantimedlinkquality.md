---
title: WlanTimedLinkQuality rule (ndis)
description: The WlanTimedLinkQuality rule specifies the NDIS\_STATUS\_DOT11\_LINK\_QUALITY indication is made in 15 seconds after a successful NDIS\_STATUS\_DOT11\_ASSOCIATION\_COMPLETION.
ms.assetid: B7055493-C09B-4565-A10F-32A34CCD5621
ms.date: 05/21/2018
keywords: ["WlanTimedLinkQuality rule (ndis)"]
topic_type:
- apiref
api_name:
- WlanTimedLinkQuality
api_type:
- NA
ms.localizationpriority: medium
---

# WlanTimedLinkQuality rule (ndis)


The **WlanTimedLinkQuality** rule specifies the NDIS\_STATUS\_DOT11\_LINK\_QUALITY indication is made in 15 seconds after a successful NDIS\_STATUS\_DOT11\_ASSOCIATION\_COMPLETION.

|              |      |
|--------------|------|
| Driver model | NDIS |

|                                   |                                                                                                                                       |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Bug check(s) found with this rule | [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](https://msdn.microsoft.com/library/windows/hardware/ff560187) (0x0009400B) |

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
<td align="left"><p>Run <a href="https://msdn.microsoft.com/library/windows/hardware/ff545448" data-raw-source="[Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff545448)">Driver Verifier</a> and select the <a href="https://msdn.microsoft.com/library/windows/hardware/hh454208" data-raw-source="[NDIS/WIFI verification](https://msdn.microsoft.com/library/windows/hardware/hh454208)">NDIS/WIFI verification</a> option.</p></td>
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

[NDIS\_STATUS\_DOT11\_LINK\_QUALITY](https://msdn.microsoft.com/library/windows/hardware/ff567344)
 

 





