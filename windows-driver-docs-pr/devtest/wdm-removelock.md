---
title: RemoveLock rule (wdm)
description: The RemoveLock rule specifies that calls to IoAcquireRemoveLock and IoReleaseRemoveLock are used correctly. Moreover, at the end of the IRP\_MJ\_PNP or IRP\_MJ\_POWER routine, the driver should not hold the RemoveLock.
ms.assetid: 8FEBE04B-7823-46FC-B493-D98778114748
ms.date: 05/21/2018
keywords: ["RemoveLock rule (wdm)"]
topic_type:
- apiref
api_name:
- RemoveLock
api_type:
- NA
ms.localizationpriority: medium
---

# RemoveLock rule (wdm)


The **RemoveLock** rule specifies that calls to [**IoAcquireRemoveLock**](https://msdn.microsoft.com/library/windows/hardware/ff548204) and [**IoReleaseRemoveLock**](https://msdn.microsoft.com/library/windows/hardware/ff549560) are used correctly. Moreover, at the end of the IRP\_MJ\_PNP or IRP\_MJ\_POWER routine, the driver should not hold the **RemoveLock**.

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
<td align="left"><p>Run <a href="https://msdn.microsoft.com/library/windows/hardware/ff552808" data-raw-source="[Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808)">Static Driver Verifier</a> and specify the <strong>RemoveLock</strong> rule.</p>
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

[**IoAcquireRemoveLock**](https://msdn.microsoft.com/library/windows/hardware/ff548204)
[**IoReleaseRemoveLock**](https://msdn.microsoft.com/library/windows/hardware/ff549560)
[**IoReleaseRemoveLockAndWait**](https://msdn.microsoft.com/library/windows/hardware/ff549567)
[**RemoveHeadList**](https://msdn.microsoft.com/library/windows/hardware/ff561032)
See also
--------

[Using Remove Locks](https://msdn.microsoft.com/library/windows/hardware/ff565504)
 

 





