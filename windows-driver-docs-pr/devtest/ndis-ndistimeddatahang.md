---
title: NdisTimedDataHang rule (ndis)
description: The NdisTimedDataHang rule verifies that an NDIS miniport driver processes any pending send requests for NET\_BUFFER\_LIST structures within 22 seconds.
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


The **NdisTimedDataHang** rule verifies that an NDIS miniport driver processes any pending send requests for [**NET\_BUFFER\_LIST**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer_list) structures within 22 seconds.

The miniport driver must call the [**NdisMSendNetBufferListsComplete**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismsendnetbufferlistscomplete) function to complete the pending send requests for all [**NET\_BUFFER\_LIST**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer_list) structures. If there are pending send requests, the NDIS miniport driver must continue to complete them. This rule is violated when there is at least one pending send request for a **NET\_BUFFER\_LIST** structure and no such send requests have been completed in the past 22 seconds.

You can use a kernel debugger to help identify the cause of the problem. Check RULE\_STATE for PendingNbl, which points to the oldest pending [**NET\_BUFFER\_LIST**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer_list). Use the [**!ndiskd.nbl**](../debugger/-ndiskd-nbl.md) debugger extension. For information about using the debugger, see [Windows Debugging](../debugger/index.md).

**Driver model: NDIS**

**Bug check(s) found with this rule**: [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](../debugger/bug-check-0xc4--driver-verifier-detected-violation.md) (0x0x0009200F)


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

[**MiniportSendNetBufferLists**](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_send_net_buffer_lists)
[**NdisMSendNetBufferListsComplete**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismsendnetbufferlistscomplete)
