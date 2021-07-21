---
title: WlanTimedLinkQuality rule (ndis)
description: The WlanTimedLinkQuality rule specifies the NDIS\_STATUS\_DOT11\_LINK\_QUALITY indication is made in 15 seconds after a successful NDIS\_STATUS\_DOT11\_ASSOCIATION\_COMPLETION.
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

**Driver model: NDIS**

**Bug check(s) found with this rule**: [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](../debugger/bug-check-0xc4--driver-verifier-detected-violation.md) (0x0009400B)


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
[**MiniportOidRequest**](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_oid_request)
[**NdisMIndicateStatusEx**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismindicatestatusex)
[**NdisMOidRequestComplete**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismoidrequestcomplete)
## See also

[NDIS\_STATUS\_DOT11\_LINK\_QUALITY](/previous-versions/windows/hardware/wireless/ndis-status-dot11-link-quality)
