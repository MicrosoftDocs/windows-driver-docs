---
title: NdisTimedDataSend rule (ndis)
description: The NdisTimedDataSend rule verifies that when an NDIS driver calls MiniportSendNetBufferLists, the miniport driver completes the send request within 30 seconds.
ms.date: 05/21/2018
keywords: ["NdisTimedDataSend rule (ndis)"]
topic_type:
- apiref
api_name:
- NdisTimedDataSend
api_type:
- NA
ms.localizationpriority: medium
---

# NdisTimedDataSend rule (ndis)


The **NdisTimedDataSend** rule verifies that when an NDIS driver calls [*MiniportSendNetBufferLists*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_send_net_buffer_lists), the miniport driver completes the send request within 30 seconds.

You can use a kernel debugger to help identify the cause of the problem. Check RULE\_STATE for PendingNbl, which points to the pending buffer list that causes the timeout. Use the [**!ndiskd.nbl**](../debugger/-ndiskd-nbl.md) debugger extension to examine the [**NET\_BUFFER\_LIST**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_net_buffer_list). For information about using the debugger, see [Windows Debugging](../debugger/index.md).

**Driver model: NDIS**

**Bug check(s) found with this rule**: [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](../debugger/bug-check-0xc4--driver-verifier-detected-violation.md) (0x0009200D)


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
