---
title: MarkIrpPending rule (wdm)
description: The MarkIrpPending rule specifies that whenever a driver dispatch routine calls IoMarkIrpPending, the driver returns STATUS\_PENDING when the dispatch routine ends. See MarkIrpPending2 for a complimentary specification.
ms.assetid: cbf5484e-2806-4df6-bdfb-98acfe5d214c
ms.author: windowsdriverdev
ms.date: 05/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["MarkIrpPending rule (wdm)"]
topic_type:
- apiref
api_name:
- MarkIrpPending
api_type:
- NA
ms.localizationpriority: medium
---

# MarkIrpPending rule (wdm)


The **MarkIrpPending** rule specifies that whenever a driver dispatch routine calls [**IoMarkIrpPending**](https://msdn.microsoft.com/library/windows/hardware/ff549422), the driver returns STATUS\_PENDING when the dispatch routine ends. See [**MarkIrpPending2**](wdm-markirppending2.md) for a complimentary specification.

|              |     |
|--------------|-----|
| Driver model | WDM |

How to test
-----------

<table>
<colgroup>
<col width="100%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">At compile time</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>MarkIrpPending</strong> rule.</p>
Use the following steps to run an analysis of your code:
<ol>
<li>[Prepare your code (use role type declarations).](https://msdn.microsoft.com/library/windows/hardware/hh454281#preparing-your-source-code)</li>
<li>[Run Static Driver Verifier.](https://msdn.microsoft.com/library/windows/hardware/hh454281#running-static-driver-verifier)</li>
<li>[View and analyze the results.](https://msdn.microsoft.com/library/windows/hardware/hh454281#viewing-and-analyzing-the-results)</li>
</ol>
<p>For more information, see [Using Static Driver Verifier to Find Defects in Drivers](https://msdn.microsoft.com/library/windows/hardware/hh454281).</p></td>
</tr>
</tbody>
</table>

Applies to
----------

[**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336)
[**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343)
[**IoMarkIrpPending**](https://msdn.microsoft.com/library/windows/hardware/ff549422)
[**PoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff559654)
[**RemoveHeadList**](https://msdn.microsoft.com/library/windows/hardware/ff561032)
See also
--------

[**MarkingInterlockedQueuedIrps**](wdm-markinginterlockedqueuedirps.md)
[**Synchronizing IRP Cancellation**](https://msdn.microsoft.com/library/windows/hardware/ff564531)
 

 





