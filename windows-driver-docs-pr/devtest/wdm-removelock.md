---
title: RemoveLock rule (wdm)
description: The RemoveLock rule specifies that calls to IoAcquireRemoveLock and IoReleaseRemoveLock are used correctly. Moreover, at the end of the IRP\_MJ\_PNP or IRP\_MJ\_POWER routine, the driver should not hold the RemoveLock.
ms.assetid: 8FEBE04B-7823-46FC-B493-D98778114748
keywords: ["RemoveLock rule (wdm)"]
topic_type:
- apiref
api_name:
- RemoveLock
api_type:
- NA
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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>RemoveLock</strong> rule.</p>
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

[**IoAcquireRemoveLock**](https://msdn.microsoft.com/library/windows/hardware/ff548204)
[**IoReleaseRemoveLock**](https://msdn.microsoft.com/library/windows/hardware/ff549560)
[**IoReleaseRemoveLockAndWait**](https://msdn.microsoft.com/library/windows/hardware/ff549567)
[**RemoveHeadList**](https://msdn.microsoft.com/library/windows/hardware/ff561032)
See also
--------

[Using Remove Locks](https://msdn.microsoft.com/library/windows/hardware/ff565504)
 

 





