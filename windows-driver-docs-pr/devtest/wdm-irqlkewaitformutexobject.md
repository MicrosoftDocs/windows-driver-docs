---
title: IrqlKeWaitForMutexObject rule (wdm)
ms.assetid: f2e7b733-1746-4db5-b4a9-becd211e40cf
ms.author: windowsdriverdev
ms.date: 05/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>IrqlKeWaitForMutexObject</strong> rule.</p>
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

[**KeWaitForSingleObject**](https://msdn.microsoft.com/library/windows/hardware/ff553350)
 

 





