---
title: WdfInterruptLockRelease rule (kmdf)
description: The WdfInterruptLockRelease rule specifies that calls to WdfInterruptAcquireLock and WdfInterruptReleaseLock are used in a balanced way within a KMDF callback routine.
ms.assetid: 2cad3811-99c2-4909-bad6-54cab9f006e6
ms.author: windowsdriverdev
ms.date: 05/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["WdfInterruptLockRelease rule (kmdf)"]
topic_type:
- apiref
api_name:
- WdfInterruptLockRelease
api_type:
- NA
---

# WdfInterruptLockRelease rule (kmdf)


The **WdfInterruptLockRelease** rule specifies that calls to [**WdfInterruptAcquireLock**](https://msdn.microsoft.com/library/windows/hardware/ff547340) and [**WdfInterruptReleaseLock**](https://msdn.microsoft.com/library/windows/hardware/ff547376) are used in a balanced way within a KMDF callback routine. At the end of any KMDF callback routine, the driver should not hold the framework spin lock object that was obtained by a previous call to **WdfInterruptAcquireLock**.

|              |      |
|--------------|------|
| Driver model | KMDF |

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>WdfInterruptLockRelease</strong> rule.</p>
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

[**WdfInterruptAcquireLock**](https://msdn.microsoft.com/library/windows/hardware/ff547340)
[**WdfInterruptReleaseLock**](https://msdn.microsoft.com/library/windows/hardware/ff547376)
 

 





