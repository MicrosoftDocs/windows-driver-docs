---
title: IrqlKeWaitForMutexObject rule (wdm)
ms.assetid: f2e7b733-1746-4db5-b4a9-becd211e40cf
ms.date: 05/21/2018
description: 
keywords: ["IrqlKeWaitForMutexObject rule (wdm)"]
topic_type:
- apiref
api_name:
- IrqlKeWaitForMutexObject
api_type:
- NA
ms.localizationpriority: medium
---

# IrqlKeWaitForMutexObject rule (wdm)


The **IrqlKeWaitForMutexObject** rule specifies the driver to call the [**KeWaitForMutexObject**](https://msdn.microsoft.com/library/windows/hardware/ff553344) routine at the proper IRQL based on the value of the *Timeout* parameter:

-   If *Timeout* points to a zero value, the driver is executing at IRQL = DISPATCH\_LEVEL.

-   If *Timeout* is **NULL**, or points to any value other than zero, the driver is executing at IRQL &lt;= APC\_LEVEL.

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
<td align="left"><p>Run <a href="https://msdn.microsoft.com/library/windows/hardware/ff552808" data-raw-source="[Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808)">Static Driver Verifier</a> and specify the <strong>IrqlKeWaitForMutexObject</strong> rule.</p>
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

[**KeWaitForSingleObject**](https://msdn.microsoft.com/library/windows/hardware/ff553350)
 

 





