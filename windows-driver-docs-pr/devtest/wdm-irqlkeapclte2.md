---
title: IrqlKeApcLte2 rule (wdm)
ms.assetid: 585d741d-543f-421b-be48-28f48d68fc4d
description: 
keywords: ["IrqlKeApcLte2 rule (wdm)"]
topic_type:
- apiref
api_name:
- IrqlKeApcLte2
api_type:
- NA
---

# IrqlKeApcLte2 rule (wdm)


The **IrqlKeApcLte2** rule specifies that the driver calls the following kernel routines only when it is executing at IRQL &lt;= APC\_LEVEL:

-   [**KeAreAllApcsDisabled**](https://msdn.microsoft.com/library/windows/hardware/ff551935)

-   [**KeAreApcsDisabled**](https://msdn.microsoft.com/library/windows/hardware/ff551938)

-   [**KeDeregisterNmiCallback**](https://msdn.microsoft.com/library/windows/hardware/ff552008)

-   [**KeEnterCriticalRegion**](https://msdn.microsoft.com/library/windows/hardware/ff552021)

-   [**KeEnterGuardedRegion**](https://msdn.microsoft.com/library/windows/hardware/ff552028)

-   [**KeLeaveCriticalRegion**](https://msdn.microsoft.com/library/windows/hardware/ff552964)

-   [**KeLeaveGuardedRegion**](https://msdn.microsoft.com/library/windows/hardware/ff552967)

-   [**KeRegisterNmiCallback**](https://msdn.microsoft.com/library/windows/hardware/ff553116)

|              |     |
|--------------|-----|
| Driver model | WDM |

|                                   |                                                                                                                                       |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Bug check(s) found with this rule | [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](https://msdn.microsoft.com/library/windows/hardware/ff560187) (0x00020010) |

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>IrqlKeApcLte2</strong> rule.</p>
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

[**KeDeregisterNmiCallback**](https://msdn.microsoft.com/library/windows/hardware/ff552008)
[**KeEnterCriticalRegion**](https://msdn.microsoft.com/library/windows/hardware/ff552021)
[**KeEnterGuardedRegion**](https://msdn.microsoft.com/library/windows/hardware/ff552028)
[**KeLeaveCriticalRegion**](https://msdn.microsoft.com/library/windows/hardware/ff552964)
[**KeLeaveGuardedRegion**](https://msdn.microsoft.com/library/windows/hardware/ff552967)
[**KeRegisterNmiCallback**](https://msdn.microsoft.com/library/windows/hardware/ff553116)
 

 





