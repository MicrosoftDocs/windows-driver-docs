---
title: WlanConnectionRoaming rule (ndis)
description: The WlanConnectionRoaming rule verifies the miniport driver correctly follows the Native 802.11 wireless LAN (WLAN) connection and roaming sequence.
ms.date: 05/21/2018
keywords: ["WlanConnectionRoaming rule (ndis)"]
topic_type:
- apiref
api_name:
- WlanConnectionRoaming
api_type:
- NA
ms.localizationpriority: medium
---

# WlanConnectionRoaming rule (ndis)


The **WlanConnectionRoaming** rule verifies the miniport driver correctly follows the Native 802.11 wireless LAN (WLAN) connection and roaming sequence.

**Driver model: NDIS**

**Bug check(s) found with this rule**: [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](../debugger/bug-check-0xc4--driver-verifier-detected-violation.md) ( 0x00093005)


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
<td align="left"><p>Run <a href="/windows-hardware/drivers/devtest/driver-verifier" data-raw-source="[Driver Verifier](./driver-verifier.md)">Driver Verifier</a> and select the <a href="/windows-hardware/drivers/devtest/ddi-compliance-checking" data-raw-source="[NDIS/WIFI verification](./ddi-compliance-checking.md)">NDIS/WIFI verification</a> option.</p></td>
</tr>
</tbody>
</table>

 

## Applies to

[**MiniportHaltEx**](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_halt)
[**NdisMIndicateStatusEx**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismindicatestatusex)
## See also

[General Connection Operation Guidelines](/previous-versions/windows/hardware/wireless/general-connection-operation-guidelines)
[NDIS\_STATUS\_DOT11\_CONNECTION\_START](/previous-versions/windows/hardware/wireless/ndis-status-dot11-connection-start)
[OID\_DOT11\_RESET\_REQUEST](/previous-versions/windows/hardware/wireless/oid-dot11-reset-request)
[NDIS\_STATUS\_DOT11\_ROAMING\_START](/previous-versions/windows/hardware/wireless/ndis-status-dot11-roaming-start)
