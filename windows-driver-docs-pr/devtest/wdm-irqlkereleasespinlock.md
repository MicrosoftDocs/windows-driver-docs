---
title: IrqlKeReleaseSpinLock rule (wdm)
description: The IrqlKeReleaseSpinLock rule specifies that the driver calls KeReleaseSpinLock only when it is executing at IRQL�  DISPATCH\_LEVEL.
ms.assetid: 4abc4010-c653-44ab-9eaa-621d0ed2f354
ms.author: windowsdriverdev
ms.date: 5/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["IrqlKeReleaseSpinLock rule (wdm)"]
topic_type:
- apiref
api_name:
- IrqlKeReleaseSpinLock
api_type:
- NA
---

# IrqlKeReleaseSpinLock rule (wdm)


The **IrqlKeReleaseSpinLock** rule specifies that the driver calls [**KeReleaseSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff553145) only when it is executing at IRQL = DISPATCH\_LEVEL.

This rule also specifies that the value of the *NewIrql* parameter in the call to **KeReleaseSpinLock** is equal to the IRQL at which the driver was executing before the call to [**KeAcquireSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff551917). (This value is also the value of the *OldIrql* parameter that is supplied by **KeAcquireSpinLock**.)

|              |     |
|--------------|-----|
| Driver model | WDM |

|                                   |                                                                                                                                       |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Bug check(s) found with this rule | [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](https://msdn.microsoft.com/library/windows/hardware/ff560187) (0x00020015) |

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>IrqlKeReleaseSpinLock</strong> rule.</p>
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

[**KeReleaseSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff553145)
 

 





