---
title: NdisTimedOidComplete rule (ndis)
description: The NdisTimedOidComplete rule specifies that the NDIS miniport driver completes an OID request within 12 seconds.
ms.date: 05/21/2018
keywords: ["NdisTimedOidComplete rule (ndis)"]
topic_type:
- apiref
api_name:
- NdisTimedOidComplete
api_type:
- NA
ms.localizationpriority: medium
---

# NdisTimedOidComplete rule (ndis)


The **NdisTimedOidComplete** rule specifies that the NDIS miniport driver completes an OID request within 12 seconds.

**Driver model: NDIS**

**Bug check(s) found with this rule**: [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](../debugger/bug-check-0xc4--driver-verifier-detected-violation.md) ( 0x00092003)


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

[**MiniportOidRequest**](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_oid_request)
[**NdisMOidRequestComplete**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismoidrequestcomplete)
