---
title: IrqlKeApcLte1 rule (wdm)
ms.assetid: d88e3c0f-574b-41df-97ee-282a9f1eb6f4
ms.author: windowsdriverdev
ms.date: 05/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
description: 
keywords: ["IrqlKeApcLte1 rule (wdm)"]
topic_type:
- apiref
api_name:
- IrqlKeApcLte1
api_type:
- NA
---

# IrqlKeApcLte1 rule (wdm)


The **IrqlKeApcLte1** rule specifies that the driver calls the following kernel routines only when it is executing at IRQL &lt;= APC\_LEVEL:

-   [**KeAcquireGuardedMutex**](https://msdn.microsoft.com/library/windows/hardware/ff551892)

-   [**KeAcquireGuardedMutexUnsafe**](https://msdn.microsoft.com/library/windows/hardware/ff551894)

-   [**KeDelayExecutionThread**](https://msdn.microsoft.com/library/windows/hardware/ff551986)

-   [**KeQueryActiveProcessors**](https://msdn.microsoft.com/library/windows/hardware/ff553001)

-   [**KeReleaseGuardedMutex**](https://msdn.microsoft.com/library/windows/hardware/ff553124)

-   [**KeReleaseGuardedMutexUnsafe**](https://msdn.microsoft.com/library/windows/hardware/ff553125)

-   [**KeTryToAcquireGuardedMutex**](https://msdn.microsoft.com/library/windows/hardware/ff553307)

|              |     |
|--------------|-----|
| Driver model | WDM |

|                                   |                                                                                                                                       |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Bug check(s) found with this rule | [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](https://msdn.microsoft.com/library/windows/hardware/ff560187) (0x0002000F) |

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>IrqlKeApcLte1</strong> rule.</p>
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

[**KeAcquireGuardedMutex**](https://msdn.microsoft.com/library/windows/hardware/ff551892)
[**KeAcquireGuardedMutexUnsafe**](https://msdn.microsoft.com/library/windows/hardware/ff551894)
[**KeDelayExecutionThread**](https://msdn.microsoft.com/library/windows/hardware/ff551986)
[**KeQueryActiveProcessors**](https://msdn.microsoft.com/library/windows/hardware/ff553001)
[**KeReleaseGuardedMutex**](https://msdn.microsoft.com/library/windows/hardware/ff553124)
[**KeReleaseGuardedMutexUnsafe**](https://msdn.microsoft.com/library/windows/hardware/ff553125)
[**KeTryToAcquireGuardedMutex**](https://msdn.microsoft.com/library/windows/hardware/ff553307)
 

 





