---
title: NdisFilterTimedPauseComplete rule (ndis)
description: The NdisFilterTimedPauseComplete verifies three things The FilterPause function will be completed in 10 seconds or less.The FilterPause function must not fail.The FilterPause function must not complete twice.
ms.assetid: 60B926CC-E2C4-42B8-8555-5E620DCDDAFC
keywords: ["NdisFilterTimedPauseComplete rule (ndis)"]
topic_type:
- apiref
api_name:
- NdisFilterTimedPauseComplete
api_type:
- NA
---

# NdisFilterTimedPauseComplete rule (ndis)


The **NdisFilterTimedPauseComplete** verifies three things:

-   The [*FilterPause*](https://msdn.microsoft.com/library/windows/hardware/ff549957) function will be completed in 10 seconds or less.

-   The [*FilterPause*](https://msdn.microsoft.com/library/windows/hardware/ff549957) function must not fail.

-   The [*FilterPause*](https://msdn.microsoft.com/library/windows/hardware/ff549957) function must not complete twice.

|              |      |
|--------------|------|
| Driver model | NDIS |

|                                   |                                                                                                                                        |
|-----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| Bug check(s) found with this rule | [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](https://msdn.microsoft.com/library/windows/hardware/ff560187) ( 0x00092010) |

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
<td align="left"><p>Run [Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff545448) and select the [NDIS/WIFI verification](https://msdn.microsoft.com/library/windows/hardware/dn312128) option. This rule is also tested with the [DDI compliance checking](https://msdn.microsoft.com/library/windows/hardware/hh454208) option.</p></td>
</tr>
</tbody>
</table>

 

 

 





