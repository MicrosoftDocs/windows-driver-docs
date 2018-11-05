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


The **NdisFilterTimedDataSend** rule verifies that an NDIS filter driver completes a send request by the [*FilterSendNetBufferLists*](https://msdn.microsoft.com/library/windows/hardware/ff549966) function before timing out.

You can use a kernel debugger to help identify the cause of the problem. Check RULE\_STATE for PendingNbl, which points to the oldest pending [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388). Use the [**!ndiskd.nbl**](https://msdn.microsoft.com/library/windows/hardware/ff564156) debugger extension. For information about using the debugger, see [Windows Debugging](https://msdn.microsoft.com/library/windows/hardware/ff551063).

|              |      |
|--------------|------|
| Driver model | NDIS |

|                                   |                                                                                                                                        |
|-----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| Bug check(s) found with this rule | [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](https://msdn.microsoft.com/library/windows/hardware/ff560187) ( 0x00092011) |

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
<td align="left"><p>Run <a href="https://msdn.microsoft.com/library/windows/hardware/ff545448" data-raw-source="[Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff545448)">Driver Verifier</a> and select the <a href="https://msdn.microsoft.com/library/windows/hardware/dn312128" data-raw-source="[NDIS/WIFI verification](https://msdn.microsoft.com/library/windows/hardware/dn312128)">NDIS/WIFI verification</a> option. This rule is also tested with the <a href="https://msdn.microsoft.com/library/windows/hardware/hh454208" data-raw-source="[DDI compliance checking](https://msdn.microsoft.com/library/windows/hardware/hh454208)">DDI compliance checking</a> option.</p></td>
</tr>
</tbody>
</table>

 

 

 





