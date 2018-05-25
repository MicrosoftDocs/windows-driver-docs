---
title: IrqlPsPassive rule (wdm)
ms.assetid: db84c945-7695-4691-8294-095bbc74ef8a
ms.author: windowsdriverdev
ms.date: 5/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
description: 
keywords: ["IrqlPsPassive rule (wdm)"]
topic_type:
- apiref
api_name:
- IrqlPsPassive
api_type:
- NA
---

# IrqlPsPassive rule (wdm)


The **IrqlPsPassive** rule specifies that the driver calls the following [**Process Structure routines**](https://msdn.microsoft.com/library/windows/hardware/ff559917) only when it is executing at IRQL = PASSIVE\_LEVEL:

-   [**PsCreateSystemThread**](https://msdn.microsoft.com/library/windows/hardware/ff559932)

-   [**PsGetVersion**](https://msdn.microsoft.com/library/windows/hardware/ff559941)

-   [**PsSetCreateProcessNotifyRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff559951)

-   [**PsSetCreateThreadNotifyRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff559954)

-   [**PsSetLoadImageNotifyRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff559957)

-   [**PsTerminateSystemThread**](https://msdn.microsoft.com/library/windows/hardware/ff559959)

|              |     |
|--------------|-----|
| Driver model | WDM |

|                                   |                                                                                                                                       |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Bug check(s) found with this rule | [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](https://msdn.microsoft.com/library/windows/hardware/ff560187) (0x0002001C) |

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>IrqlPsPassive</strong> rule.</p>
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

[**PsCreateSystemThread**](https://msdn.microsoft.com/library/windows/hardware/ff559932)
[**PsGetVersion**](https://msdn.microsoft.com/library/windows/hardware/ff559941)
[**PsSetCreateProcessNotifyRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff559951)
[**PsSetCreateThreadNotifyRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff559954)
[**PsSetLoadImageNotifyRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff559957)
[**PsTerminateSystemThread**](https://msdn.microsoft.com/library/windows/hardware/ff559959)
 

 





