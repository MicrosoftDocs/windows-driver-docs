---
title: WlanTimedConnectRequest rule (ndis)
description: The WlanTimedConnectRequest rule verifies that an OID\_DOT11\_CONNECT\_REQUEST is followed by a NDIS\_STATUS\_DOT11\_CONNECTION\_START within 10 seconds.
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

**Driver model: NDIS**

**Bug check(s) found with this rule**: [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](../debugger/bug-check-0xc4--driver-verifier-detected-violation.md) (0x00094009)


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
