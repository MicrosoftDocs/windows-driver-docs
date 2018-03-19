---
title: ParentObjectCheckLock rule (kmdf)
description: The ParentObjectCheckLock rule specifies that the driver should call WdfWaitLockCreate and WdfSpinLockCreate setting a parent object.
ms.assetid: 01B47113-F949-4B38-982A-D13AF0EE68E0
keywords: ["ParentObjectCheckLock rule (kmdf)"]
topic_type:
- apiref
api_name:
- ParentObjectCheckLock
api_type:
- NA
---

# ParentObjectCheckLock rule (kmdf)


The **ParentObjectCheckLock** rule specifies that the driver should call [**WdfWaitLockCreate**](https://msdn.microsoft.com/library/windows/hardware/ff551171) and [**WdfSpinLockCreate**](https://msdn.microsoft.com/library/windows/hardware/ff550042) setting a parent object.

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>ParentObjectCheckLock</strong> rule.</p>
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

[**WdfSpinLockCreate**](https://msdn.microsoft.com/library/windows/hardware/ff550042)
[**WdfWaitLockCreate**](https://msdn.microsoft.com/library/windows/hardware/ff551171)
 

 





