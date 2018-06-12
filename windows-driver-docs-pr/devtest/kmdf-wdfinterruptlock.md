---
title: WdfInterruptLock rule (kmdf)
description: The WdfInterruptLock rule specifies that calls to the WdfInterruptAcquireLock method is used in strict alternation with calls to WdfInterruptReleaseLock.
ms.assetid: bf105e83-dc63-44b1-ba9d-e4d81210fa1a
ms.author: windowsdriverdev
ms.date: 5/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["WdfInterruptLock rule (kmdf)"]
topic_type:
- apiref
api_name:
- WdfInterruptLock
api_type:
- NA
---

# WdfInterruptLock rule (kmdf)


The **WdfInterruptLock** rule specifies that calls to the [**WdfInterruptAcquireLock**](https://msdn.microsoft.com/library/windows/hardware/ff547340) method is used in strict alternation with calls to [**WdfInterruptReleaseLock**](https://msdn.microsoft.com/library/windows/hardware/ff547376). Moreover, at the end of any KMDF callback routine, the driver should not hold the framework spin lock object, obtained by a previous call to **WdfInterruptAcquireLock**.

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>WdfInterruptLock</strong> rule.</p>
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
 

 





