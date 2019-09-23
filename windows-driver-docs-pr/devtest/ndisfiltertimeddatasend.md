---
title: NdisFilterTimedDataSend rule (ndis)
description: The NdisFilterTimedDataSend rule verifies that an NDIS filter driver completes a send request by the FilterSendNetBufferLists function before timing out.
ms.assetid: 0D04DF73-4391-4668-8F6C-023BEE5A7F08
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


The **NdisFilterTimedDataSend** rule verifies that an NDIS filter driver completes a send request by the [*FilterSendNetBufferLists*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nc-ndis-filter_send_net_buffer_lists) function before timing out.

You can use a kernel debugger to help identify the cause of the problem. Check RULE\_STATE for PendingNbl, which points to the oldest pending [**NET\_BUFFER\_LIST**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/ns-ndis-_net_buffer_list). Use the [**!ndiskd.nbl**](https://docs.microsoft.com/windows-hardware/drivers/debugger/-ndiskd-nbl) debugger extension. For information about using the debugger, see [Windows Debugging](https://docs.microsoft.com/windows-hardware/drivers/debugger/index).

|              |      |
|--------------|------|
| Driver model | NDIS |

|                                   |                                                                                                                                        |
|-----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| Bug check(s) found with this rule | [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](https://docs.microsoft.com/windows-hardware/drivers/debugger/bug-check-0xc4--driver-verifier-detected-violation) ( 0x00092011) |

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
<td align="left"><p>Run <a href="https://docs.microsoft.com/windows-hardware/drivers/devtest/driver-verifier" data-raw-source="[Driver Verifier](https://docs.microsoft.com/windows-hardware/drivers/devtest/driver-verifier)">Driver Verifier</a> and select the <a href="https://docs.microsoft.com/windows-hardware/drivers/devtest/ndis-wifi-verification" data-raw-source="[NDIS/WIFI verification](https://docs.microsoft.com/windows-hardware/drivers/devtest/ndis-wifi-verification)">NDIS/WIFI verification</a> option. This rule is also tested with the <a href="https://docs.microsoft.com/windows-hardware/drivers/devtest/ddi-compliance-checking" data-raw-source="[DDI compliance checking](https://docs.microsoft.com/windows-hardware/drivers/devtest/ddi-compliance-checking)">DDI compliance checking</a> option.</p></td>
</tr>
</tbody>
</table>

 

 

 





