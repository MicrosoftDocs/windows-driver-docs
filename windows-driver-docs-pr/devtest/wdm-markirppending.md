---
title: MarkIrpPending rule (wdm)
description: The MarkIrpPending rule specifies that whenever a driver dispatch routine calls IoMarkIrpPending, the driver returns STATUS\_PENDING when the dispatch routine ends. See MarkIrpPending2 for a complimentary specification.
ms.assetid: cbf5484e-2806-4df6-bdfb-98acfe5d214c
ms.date: 05/21/2018
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
<td align="left"><p>Run <a href="https://msdn.microsoft.com/library/windows/hardware/ff552808" data-raw-source="[Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808)">Static Driver Verifier</a> and specify the <strong>MarkIrpPending</strong> rule.</p>
Use the following steps to run an analysis of your code:
<ol>
<li><a href="https://msdn.microsoft.com/library/windows/hardware/hh454281#preparing-your-source-code" data-raw-source="[Prepare your code (use role type declarations).](https://msdn.microsoft.com/library/windows/hardware/hh454281#preparing-your-source-code)">Prepare your code (use role type declarations).</a></li>
<li><a href="https://msdn.microsoft.com/library/windows/hardware/hh454281#running-static-driver-verifier" data-raw-source="[Run Static Driver Verifier.](https://msdn.microsoft.com/library/windows/hardware/hh454281#running-static-driver-verifier)">Run Static Driver Verifier.</a></li>
<li><a href="https://msdn.microsoft.com/library/windows/hardware/hh454281#viewing-and-analyzing-the-results" data-raw-source="[View and analyze the results.](https://msdn.microsoft.com/library/windows/hardware/hh454281#viewing-and-analyzing-the-results)">View and analyze the results.</a></li>
</ol>
<p>For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/hh454281" data-raw-source="[Using Static Driver Verifier to Find Defects in Drivers](https://msdn.microsoft.com/library/windows/hardware/hh454281)">Using Static Driver Verifier to Find Defects in Drivers</a>.</p></td>
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
 

 





