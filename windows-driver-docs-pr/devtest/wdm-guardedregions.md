---
title: GuardedRegions rule (wdm)
description: The GuardedRegions rule verifies that calls to KeEnterGuardedRegion and KeLeaveGuardedRegion are used in strict alternation.
ms.assetid: CF98BF68-905C-48D2-AE72-08DD5559AA0D
ms.author: windowsdriverdev
ms.date: 05/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["GuardedRegions rule (wdm)"]
topic_type:
- apiref
api_name:
- GuardedRegions
api_type:
- NA
---

# GuardedRegions rule (wdm)


The **GuardedRegions** rule verifies that calls to [**KeEnterGuardedRegion**](https://msdn.microsoft.com/library/windows/hardware/ff552028) and [**KeLeaveGuardedRegion**](https://msdn.microsoft.com/library/windows/hardware/ff552967) are used in strict alternation.

Each call to [**KeEnterGuardedRegion**](https://msdn.microsoft.com/library/windows/hardware/ff552028) must have a matching call to [**KeLeaveGuardedRegion**](https://msdn.microsoft.com/library/windows/hardware/ff552967).

|              |     |
|--------------|-----|
| Driver model | WDM |

|                                   |                                                                                                                                       |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Bug check(s) found with this rule | [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](https://msdn.microsoft.com/library/windows/hardware/ff560187) (0x0004000E) |

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>GuardedRegions</strong> rule.</p>
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
<td align="left"><p>Run [Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff545448) and select the [DDI compliance checking](https://msdn.microsoft.com/library/windows/hardware/hh454208) option.</p></td>
</tr>
</tbody>
</table>

 

Applies to
----------

[**KeEnterGuardedRegion**](https://msdn.microsoft.com/library/windows/hardware/ff552028)
[**KeLeaveGuardedRegion**](https://msdn.microsoft.com/library/windows/hardware/ff552967)
See also
--------

[Critical Regions and Guarded Regions](https://msdn.microsoft.com/library/windows/hardware/ff542925)
 

 





