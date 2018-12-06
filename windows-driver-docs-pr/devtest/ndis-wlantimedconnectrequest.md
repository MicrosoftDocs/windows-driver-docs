---
title: WlanTimedConnectRequest rule (ndis)
description: The WlanTimedConnectRequest rule verifies that an OID\_DOT11\_CONNECT\_REQUEST is followed by a NDIS\_STATUS\_DOT11\_CONNECTION\_START within 10 seconds.
ms.assetid: F40D92B1-CA48-4060-B9E2-A965900EAF7B
ms.date: 05/21/2018
keywords: ["WlanTimedConnectRequest rule (ndis)"]
topic_type:
- apiref
api_name:
- WlanTimedConnectRequest
api_type:
- NA
ms.localizationpriority: medium
---

# WlanTimedConnectRequest rule (ndis)


The **WlanTimedConnectRequest** rule verifies that an OID\_DOT11\_CONNECT\_REQUEST is followed by a NDIS\_STATUS\_DOT11\_CONNECTION\_START within 10 seconds.

Furthermore, an NDIS\_STATUS\_DOT11\_CONNECTION\_START is indicated only if the OID\_DOT11\_CONNECT\_REQUEST is completed with NDIS\_STATUS\_SUCCESS. This rule applies only to the Extensible Station port (Port 0).

|              |      |
|--------------|------|
| Driver model | NDIS |

|                                   |                                                                                                                                       |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Bug check(s) found with this rule | [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](https://msdn.microsoft.com/library/windows/hardware/ff560187) (0x00094009) |

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
 

 





