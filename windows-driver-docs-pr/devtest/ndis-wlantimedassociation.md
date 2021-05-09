---
title: WlanTimedAssociation rule (ndis)
description: The WlanTimedAssociation rule specifies that the NDIS miniport driver finishes the wireless LAN (WLAN) association operation in 10 seconds.
ms.date: 05/21/2018
keywords: ["WlanTimedAssociation rule (ndis)"]
topic_type:
- apiref
api_name:
- WlanTimedAssociation
api_type:
- NA
ms.localizationpriority: medium
---

# WlanTimedAssociation rule (ndis)


The **WlanTimedAssociation** rule specifies that the NDIS miniport driver finishes the wireless LAN (WLAN) association operation in 10 seconds.

**Driver model: NDIS**

**Bug check(s) found with this rule**: [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](../debugger/bug-check-0xc4--driver-verifier-detected-violation.md) (0x00094007)


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
## See also

[General Connection Operation Guidelines](/previous-versions/windows/hardware/wireless/general-connection-operation-guidelines)
[OID\_DOT11\_RESET\_REQUEST](/previous-versions/windows/hardware/wireless/oid-dot11-reset-request)
[NDIS\_STATUS\_DOT11\_ASSOCIATION\_START](/previous-versions/windows/hardware/wireless/ndis-status-dot11-association-start)
