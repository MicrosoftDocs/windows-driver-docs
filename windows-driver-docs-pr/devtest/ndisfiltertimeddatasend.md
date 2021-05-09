---
title: NdisFilterTimedDataSend rule (ndis)
description: The NdisFilterTimedDataSend rule verifies that an NDIS filter driver completes a send request by the FilterSendNetBufferLists function before timing out.
ms.date: 05/21/2018
keywords: ["NdisFilterTimedDataSend rule (ndis)"]
topic_type:
- apiref
api_name:
- NdisFilterTimedDataSend
api_type:
- NA
ms.localizationpriority: medium
---

# NdisFilterTimedDataSend rule (ndis)


The **NdisFilterTimedDataSend** rule verifies that an NDIS filter driver completes a send request by the [*FilterSendNetBufferLists*](/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_send_net_buffer_lists) function before timing out.

You can use a kernel debugger to help identify the cause of the problem. Check RULE\_STATE for PendingNbl, which points to the oldest pending [**NET\_BUFFER\_LIST**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_net_buffer_list). Use the [**!ndiskd.nbl**](../debugger/-ndiskd-nbl.md) debugger extension. For information about using the debugger, see [Windows Debugging](../debugger/index.md).

**Driver model: NDIS**

**Bug check(s) found with this rule**: [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](../debugger/bug-check-0xc4--driver-verifier-detected-violation.md) ( 0x00092011)


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

 

