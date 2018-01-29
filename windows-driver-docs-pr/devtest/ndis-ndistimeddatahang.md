---
title: NdisTimedDataHang rule (ndis)
description: The NdisTimedDataHang rule verifies that an NDIS miniport driver processes any pending send requests for NET\_BUFFER\_LIST structures within 22 seconds.
ms.assetid: CDFC9C23-B065-4916-BF1C-5429B6B57A23
keywords: ["NdisTimedDataHang rule (ndis)"]
topic_type:
- apiref
api_name:
- NdisTimedDataHang
api_type:
- NA
---

# NdisTimedDataHang rule (ndis)


The **NdisTimedDataHang** rule verifies that an NDIS miniport driver processes any pending send requests for [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structures within 22 seconds.

The miniport driver must call the [**NdisMSendNetBufferListsComplete**](https://msdn.microsoft.com/library/windows/hardware/ff563668) function to complete the pending send requests for all [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structures. If there are pending send requests, the NDIS miniport driver must continue to complete them. This rule is violated when there is at least one pending send request for a **NET\_BUFFER\_LIST** structure and no such send requests have been completed in the past 22 seconds.

You can use a kernel debugger to help identify the cause of the problem. Check RULE\_STATE for PendingNbl, which points to the oldest pending [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388). Use the [**!ndiskd.nbl**](https://msdn.microsoft.com/library/windows/hardware/ff564156) debugger extension. For information about using the debugger, see [Windows Debugging](https://msdn.microsoft.com/library/windows/hardware/ff551063).

|              |      |
|--------------|------|
| Driver model | NDIS |

|                                   |                                                                                                                                         |
|-----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Bug check(s) found with this rule | [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](https://msdn.microsoft.com/library/windows/hardware/ff560187) (0x0x0009200F) |

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
<td align="left"><p>Run [Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff545448) and select the [NDIS/WIFI verification](https://msdn.microsoft.com/library/windows/hardware/dn312128) option.</p></td>
</tr>
</tbody>
</table>

 

Applies to
----------

[**MiniportSendNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff559440)
[**NdisMSendNetBufferListsComplete**](https://msdn.microsoft.com/library/windows/hardware/ff563668)
 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevtest\devtest%5D:%20NdisTimedDataHang%20rule%20%28ndis%29%20%20RELEASE:%20%281/17/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




