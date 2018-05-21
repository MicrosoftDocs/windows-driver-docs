---
title: IoBuildSynchronousFsdRequestNoFree rule (wdm)
description: The IoBuildSynchronousFsdRequestNoFree rule specifies that a driver that calls IoBuildSynchronousFsdRequest must not call IoFreeIrp.
ms.assetid: 516D6B53-866D-477D-AB9C-6E44BB285BA8
ms.author: windowsdriverdev
ms.date: 5/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["IoBuildSynchronousFsdRequestNoFree rule (wdm)"]
topic_type:
- apiref
api_name:
- IoBuildSynchronousFsdRequestNoFree
api_type:
- NA
---

# IoBuildSynchronousFsdRequestNoFree rule (wdm)


The **IoBuildSynchronousFsdRequestNoFree** rule specifies that a driver that calls [**IoBuildSynchronousFsdRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548330) must not call [**IoFreeIrp**](https://msdn.microsoft.com/library/windows/hardware/ff549113).

The **IoBuildSynchronousFsdRequestNoFree** rule reports that [**IoFreeIrp**](https://msdn.microsoft.com/library/windows/hardware/ff549113) should not be called for this IRP.

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>IoBuildSynchronousFsdRequestNoFree</strong> rule.</p>
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

[**IoBuildSynchronousFsdRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548330)
[**IoFreeIrp**](https://msdn.microsoft.com/library/windows/hardware/ff549113)
 

 





