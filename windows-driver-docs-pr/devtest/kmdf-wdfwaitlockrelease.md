---
title: WdfWaitlockRelease rule (kmdf)
description: The WdfWaitlockRelease rule specifies that calls to WdfWaitLockAcquire and WdfWaitLockRelease are used in a balanced way within a KMDF event callback function.
ms.assetid: 4ac60469-b9a3-4777-865b-f03d5a4da8ed
keywords: ["WdfWaitlockRelease rule (kmdf)"]
topic_type:
- apiref
api_name:
- WdfWaitlockRelease
api_type:
- NA
---

# WdfWaitlockRelease rule (kmdf)


The **WdfWaitlockRelease** rule specifies that calls to [**WdfWaitLockAcquire**](https://msdn.microsoft.com/library/windows/hardware/ff551168) and [**WdfWaitLockRelease**](https://msdn.microsoft.com/library/windows/hardware/ff551173) are used in a balanced way within a KMDF event callback function. When the KMDF event callback function returns, the driver should not hold the framework spin lock object that was obtained by a previous call to **WdfWaitLockAcquire**.

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>WdfWaitlockRelease</strong> rule.</p>
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

[**WdfWaitLockAcquire**](https://msdn.microsoft.com/library/windows/hardware/ff551168)
[**WdfWaitLockRelease**](https://msdn.microsoft.com/library/windows/hardware/ff551173)
 

 





