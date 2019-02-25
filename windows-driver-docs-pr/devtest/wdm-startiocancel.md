---
title: StartIoCancel rule (wdm)
description: The StartIoCancel rule specifies that the driver must not call IoSetStartIoAttributes with the NonCancelable parameter set to FALSE before calling IoSetCancelRoutine with a non-NULLCancel routine.
ms.assetid: 08fde0b1-4f4e-473a-9e07-3b39683a3a1b
ms.date: 05/21/2018
keywords: ["StartIoCancel rule (wdm)"]
topic_type:
- apiref
api_name:
- StartIoCancel
api_type:
- NA
ms.localizationpriority: medium
---

# StartIoCancel rule (wdm)


The **StartIoCancel** rule specifies that the driver must not call [**IoSetStartIoAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff550330) with the *NonCancelable* parameter set to **FALSE** before calling [**IoSetCancelRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff549674) with a non-**NULL**[**Cancel**](https://msdn.microsoft.com/library/windows/hardware/ff540742) routine.

Setting the *NonCancelable* parameter to **FALSE** before registering the [**Cancel**](https://msdn.microsoft.com/library/windows/hardware/ff540742) routine can result in a cancellation race condition.

Because a driver's [**Cancel**](https://msdn.microsoft.com/library/windows/hardware/ff540742) routine must include a call to [**IoReleaseCancelSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff549550) (to release the spin lock that the I/O Manager acquires before calling the **Cancel** routine), consider verifying your driver with both the **StartIoCancel** rule and the [**CancelSpinLock**](wdm-cancelspinlock.md) rule.

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
<td align="left"><p>Run <a href="https://msdn.microsoft.com/library/windows/hardware/ff552808" data-raw-source="[Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808)">Static Driver Verifier</a> and specify the <strong>StartIoCancel</strong> rule.</p>
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

[**IoSetCancelRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff549674)
[**IoSetStartIoAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff550330)
See also
--------

[**CancelSpinLock**](wdm-cancelspinlock.md)
 

 





