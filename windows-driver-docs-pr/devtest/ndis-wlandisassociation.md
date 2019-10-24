---
title: WlanDisassociation rule (ndis)
description: The WlanDisassociation rule verifies that the miniport driver correctly follows the Native 802.11 wireless LAN (WLAN) disassociation sequence.
ms.assetid: E9C115D5-8522-4275-B874-1DB673AE23F2
ms.date: 05/21/2018
keywords: ["WlanDisassociation rule (ndis)"]
topic_type:
- apiref
api_name:
- WlanDisassociation
api_type:
- NA
ms.localizationpriority: medium
---

# WlanDisassociation rule (ndis)


The **WlanDisassociation** rule verifies that the miniport driver correctly follows the Native 802.11 wireless LAN (WLAN) disassociation sequence.

|              |      |
|--------------|------|
| Driver model | NDIS |

|                                   |                                                                                                                                        |
|-----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| Bug check(s) found with this rule | [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](https://docs.microsoft.com/windows-hardware/drivers/debugger/bug-check-0xc4--driver-verifier-detected-violation) ( 0x00093006) |

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
<td align="left"><p>Run <a href="https://docs.microsoft.com/windows-hardware/drivers/devtest/driver-verifier" data-raw-source="[Driver Verifier](https://docs.microsoft.com/windows-hardware/drivers/devtest/driver-verifier)">Driver Verifier</a> and select the <a href="https://docs.microsoft.com/windows-hardware/drivers/devtest/ndis-wifi-verification" data-raw-source="[NDIS/WIFI verification](https://docs.microsoft.com/windows-hardware/drivers/devtest/ndis-wifi-verification)">NDIS/WIFI verification</a> option.</p></td>
</tr>
</tbody>
</table>

 

Applies to
----------

[**MiniportHaltEx**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_halt)
[**MiniportOidRequest**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_oid_request)
[**NdisMIndicateStatusEx**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismindicatestatusex)
[**NdisMOidRequestComplete**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismoidrequestcomplete)
See also
--------

[General Connection Operation Guidelines](https://docs.microsoft.com/windows-hardware/drivers/network/general-connection-operation-guidelines)
[OID\_DOT11\_RESET\_REQUEST](https://docs.microsoft.com/windows-hardware/drivers/network/oid-dot11-reset-request)
[NDIS\_STATUS\_DOT11\_DISASSOCIATION](https://docs.microsoft.com/windows-hardware/drivers/network/ndis-status-dot11-disassociation)
[NDIS\_STATUS\_DOT11\_ASSOCIATION\_START](https://docs.microsoft.com/windows-hardware/drivers/network/ndis-status-dot11-association-start)
 

 





