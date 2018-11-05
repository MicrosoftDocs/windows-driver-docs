---
title: WdfWaitlock rule (kmdf)
description: The WdfWaitlock rule specifies that calls to WdfWaitLockAcquire are used in strict alternation with WdfWaitlockRelease.
ms.assetid: 481c5a21-6c4d-41e3-a54a-3da07d287fda
ms.date: 05/21/2018
keywords: ["WdfWaitlock rule (kmdf)"]
topic_type:
- apiref
api_name:
- WdfWaitlock
api_type:
- NA
ms.localizationpriority: medium
---

# WdfWaitlock rule (kmdf)


The **WdfWaitlock** rule specifies that calls to [**WdfWaitLockAcquire**](https://msdn.microsoft.com/library/windows/hardware/ff551168) are used in strict alternation with [**WdfWaitlockRelease**](kmdf-wdfwaitlockrelease.md). When the KMDF event callback function returns, the driver should not hold the framework spin lock object that was obtained by a previous call to **WdfWaitLockAcquire**.

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
<td align="left"><p>Run <a href="https://msdn.microsoft.com/library/windows/hardware/ff552808" data-raw-source="[Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808)">Static Driver Verifier</a> and specify the <strong>WdfWaitlock</strong> rule.</p>
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

[**WdfWaitLockAcquire**](https://msdn.microsoft.com/library/windows/hardware/ff551168)
[**WdfWaitLockRelease**](https://msdn.microsoft.com/library/windows/hardware/ff551173)
 

 





