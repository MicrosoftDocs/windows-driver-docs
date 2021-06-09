---
title: NdisFilterTimedPauseComplete rule (ndis)
description: The NdisFilterTimedPauseComplete verifies three things The FilterPause function will be completed in 10 seconds or less.The FilterPause function must not fail.The FilterPause function must not complete twice.
ms.date: 05/21/2018
keywords: ["NdisFilterTimedPauseComplete rule (ndis)"]
topic_type:
- apiref
api_name:
- NdisFilterTimedPauseComplete
api_type:
- NA
ms.localizationpriority: medium
---

# NdisFilterTimedPauseComplete rule (ndis)


The **NdisFilterTimedPauseComplete** verifies three things:

-   The [*FilterPause*](/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_pause) function will be completed in 10 seconds or less.

-   The [*FilterPause*](/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_pause) function must not fail.

-   The [*FilterPause*](/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_pause) function must not complete twice.

**Driver model: NDIS**

**Bug check(s) found with this rule**: [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](../debugger/bug-check-0xc4--driver-verifier-detected-violation.md) ( 0x00092010)


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
<td align="left"><p>Run <a href="/windows-hardware/drivers/devtest/driver-verifier" data-raw-source="[Driver Verifier](./driver-verifier.md)">Driver Verifier</a> and select the <a href="/windows-hardware/drivers/devtest/ndis-wifi-verification" data-raw-source="[NDIS/WIFI verification](./ndis-wifi-verification.md)">NDIS/WIFI verification</a> option. This rule is also tested with the <a href="/windows-hardware/drivers/devtest/ddi-compliance-checking" data-raw-source="[DDI compliance checking](./ddi-compliance-checking.md)">DDI compliance checking</a> option.</p></td>
</tr>
</tbody>
</table>

 

