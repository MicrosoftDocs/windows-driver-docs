---
title: NdisTimedDataHang rule (ndis)
description: The NdisTimedDataHang rule verifies that an NDIS miniport driver processes any pending send requests for NET\_BUFFER\_LIST structures within 22 seconds.
ms.assetid: CDFC9C23-B065-4916-BF1C-5429B6B57A23
ms.date: 05/21/2018
keywords: ["NdisTimedDataHang rule (ndis)"]
topic_type:
- apiref
api_name:
- NdisTimedDataHang
api_type:
- NA
ms.localizationpriority: medium
---

# NdisTimedDataHang rule (ndis)


The **NdisTimedDataHang** rule verifies that an NDIS miniport driver processes any pending send requests for [**NET\_BUFFER\_LIST**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/ns-ndis-_net_buffer_list) structures within 22 seconds.

The miniport driver must call the [**NdisMSendNetBufferListsComplete**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismsendnetbufferlistscomplete) function to complete the pending send requests for all [**NET\_BUFFER\_LIST**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/ns-ndis-_net_buffer_list) structures. If there are pending send requests, the NDIS miniport driver must continue to complete them. This rule is violated when there is at least one pending send request for a **NET\_BUFFER\_LIST** structure and no such send requests have been completed in the past 22 seconds.

You can use a kernel debugger to help identify the cause of the problem. Check RULE\_STATE for PendingNbl, which points to the oldest pending [**NET\_BUFFER\_LIST**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/ns-ndis-_net_buffer_list). Use the [**!ndiskd.nbl**](https://docs.microsoft.com/windows-hardware/drivers/debugger/-ndiskd-nbl) debugger extension. For information about using the debugger, see [Windows Debugging](https://docs.microsoft.com/windows-hardware/drivers/debugger/index).

**Driver model: NDIS**

|                                   |                                                                                                                                         |
|-----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Bug check(s) found with this rule | [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](https://docs.microsoft.com/windows-hardware/drivers/debugger/bug-check-0xc4--driver-verifier-detected-violation) (0x0x0009200F) |

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

[**MiniportSendNetBufferLists**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_send_net_buffer_lists)
[**NdisMSendNetBufferListsComplete**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismsendnetbufferlistscomplete)
 

 





