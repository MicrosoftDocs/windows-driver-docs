---
title: WlanDisassociation Rule (NDIS)
description: The WlanDisassociation rule verifies that the miniport driver correctly follows the Native 802.11 wireless LAN (WLAN) disassociation sequence.
ms.date: 05/21/2018
keywords: ["WlanDisassociation rule (ndis)"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WlanDisassociation
api_type:
- NA
---

# WlanDisassociation rule (ndis)


The **WlanDisassociation** rule verifies that the miniport driver correctly follows the Native 802.11 wireless LAN (WLAN) disassociation sequence.

**Driver model: NDIS**

**Bug check(s) found with this rule**: [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](../debugger/bug-check-0xc4--driver-verifier-detected-violation.md) ( 0x00093006)


## How to test

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
<td align="left"><p>Run <a href="/windows-hardware/drivers/devtest/driver-verifier" data-raw-source="[Driver Verifier](./driver-verifier.md)">Driver Verifier</a> and select the <a href="/windows-hardware/drivers/devtest/ndis-wifi-verification" data-raw-source="[NDIS/WIFI verification](./ndis-wifi-verification.md)">NDIS/WIFI verification</a> option.</p></td>
</tr>
</tbody>
</table>

 

## Applies to

[**MiniportHaltEx**](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_halt)
[**MiniportOidRequest**](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_oid_request)
[**NdisMIndicateStatusEx**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismindicatestatusex)
[**NdisMOidRequestComplete**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismoidrequestcomplete)
## See also

[General Connection Operation Guidelines](/previous-versions/windows/hardware/wireless/general-connection-operation-guidelines)
[OID\_DOT11\_RESET\_REQUEST](/previous-versions/windows/hardware/wireless/oid-dot11-reset-request)
[NDIS\_STATUS\_DOT11\_DISASSOCIATION](/previous-versions/windows/hardware/wireless/ndis-status-dot11-disassociation)
[NDIS\_STATUS\_DOT11\_ASSOCIATION\_START](/previous-versions/windows/hardware/wireless/ndis-status-dot11-association-start)
