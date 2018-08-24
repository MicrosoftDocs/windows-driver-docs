---
title: IrqlExApcLte1 rule (wdm)
description: The IrqlExApcLte1 rule specifies that the driver calls ExAcquireFastMutex and ExTryToAcquireFastMutex only at IRQL�  APC\_LEVEL.
ms.assetid: c86aa593-03b5-4a65-9cef-3b64fcc3d5fd
ms.author: windowsdriverdev
ms.date: 05/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["IrqlExApcLte1 rule (wdm)"]
topic_type:
- apiref
api_name:
- IrqlExApcLte1
api_type:
- NA
ms.localizationpriority: medium
---

# IrqlExApcLte1 rule (wdm)


The **IrqlExApcLte1** rule specifies that the driver calls [**ExAcquireFastMutex**](https://msdn.microsoft.com/library/windows/hardware/ff544337) and [**ExTryToAcquireFastMutex**](https://msdn.microsoft.com/library/windows/hardware/ff545647) only at IRQL &lt;= APC\_LEVEL.

|              |     |
|--------------|-----|
| Driver model | WDM |

|                                   |                                                                                                                                                                                                                                        |
|-----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Bug check(s) found with this rule | [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](https://msdn.microsoft.com/library/windows/hardware/ff560187) (0x00020005), [**Bug Check 0xA: IRQL\_NOT\_LESS\_OR\_EQUAL**](https://msdn.microsoft.com/library/windows/hardware/ff560129) |

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>IrqlExApcLte1</strong> rule.</p>
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

<table>
<colgroup>
<col width="100%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">At run time</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Run [Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff545448) and select the [DDI compliance checking](https://msdn.microsoft.com/library/windows/hardware/hh454208) option.</p></td>
</tr>
</tbody>
</table>

 

Applies to
----------

[**ExAcquireFastMutex**](https://msdn.microsoft.com/library/windows/hardware/ff544337)
[**ExTryToAcquireFastMutex**](https://msdn.microsoft.com/library/windows/hardware/ff545647)
See also
--------

[**Managing Hardware Priorities**](https://msdn.microsoft.com/library/windows/hardware/ff554368)
[**Preventing Errors and Deadlocks While Using Spin Locks**](https://msdn.microsoft.com/library/windows/hardware/ff559854)
 

 





