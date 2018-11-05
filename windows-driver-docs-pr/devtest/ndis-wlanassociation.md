---
title: WlanAssociation rule (ndis)
description: The WlanAssociation rule verifies the miniport driver correctly follows the Native 802.11 wireless LAN (WLAN) association sequence.
ms.assetid: 3F457C06-29F1-4730-92D5-5B98CD459FD1
ms.date: 05/21/2018
keywords: ["WlanAssociation rule (ndis)"]
topic_type:
- apiref
api_name:
- WlanAssociation
api_type:
- NA
ms.localizationpriority: medium
---

# WlanAssociation rule (ndis)


The **WlanAssociation** rule verifies the miniport driver correctly follows the Native 802.11 wireless LAN (WLAN) association sequence.

|              |      |
|--------------|------|
| Driver model | NDIS |

|                                   |                                                                                                                                        |
|-----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| Bug check(s) found with this rule | [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](https://msdn.microsoft.com/library/windows/hardware/ff560187) ( 0x00093004) |

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
[OID\_DOT11\_RESET\_REQUEST](https://msdn.microsoft.com/library/windows/hardware/ff569409)
[NDIS\_STATUS\_DOT11\_ASSOCIATION\_START](https://msdn.microsoft.com/library/windows/hardware/ff567321)
 

 





