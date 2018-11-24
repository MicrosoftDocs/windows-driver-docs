---
title: IrqlExApcLte2 rule (wdm)
description: The IrqlExApcLte2 rule specifies that the driver calls the following routines only at IRQL�  APC\_LEVEL.
ms.assetid: 5800ec58-2084-4092-9614-dd631458c7dd
ms.date: 05/21/2018
keywords: ["IrqlExApcLte2 rule (wdm)"]
topic_type:
- apiref
api_name:
- IrqlExApcLte2
api_type:
- NA
ms.localizationpriority: medium
---

# IrqlExApcLte2 rule (wdm)


The **IrqlExApcLte2** rule specifies that the driver calls the following routines only at IRQL &lt;= APC\_LEVEL.

-   [**CmRegisterCallback**](https://msdn.microsoft.com/library/windows/hardware/ff541918)

-   [**CmUnRegisterCallback**](https://msdn.microsoft.com/library/windows/hardware/ff541928)

-   [**ExAllocateFromPagedLookasideList**](https://msdn.microsoft.com/library/windows/hardware/ff544393)

-   [**ExAllocatePoolWithQuota**](https://msdn.microsoft.com/library/windows/hardware/ff544506)

-   [**ExAllocatePoolWithQuotaTag**](https://msdn.microsoft.com/library/windows/hardware/ff544513)

-   [**ExDeletePagedLookasideList**](https://msdn.microsoft.com/library/windows/hardware/ff544570)

-   [**ExFreeToPagedLookasideList**](https://msdn.microsoft.com/library/windows/hardware/ff544605)

-   [**ExInitializePagedLookasideList**](https://msdn.microsoft.com/library/windows/hardware/ff545309)

-   [**ExRegisterCallback**](https://msdn.microsoft.com/library/windows/hardware/ff545534)

-   [**ExSetTimerResolution**](https://msdn.microsoft.com/library/windows/hardware/ff545614)

-   [**ExUnregisterCallback**](https://msdn.microsoft.com/library/windows/hardware/ff545649)

-   [**ProbeForRead**](https://msdn.microsoft.com/library/windows/hardware/ff559876)

-   [**ProbeForWrite**](https://msdn.microsoft.com/library/windows/hardware/ff559879)

|              |     |
|--------------|-----|
| Driver model | WDM |

|                                   |                                                                                                                                                                                                                                        |
|-----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Bug check(s) found with this rule | [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](https://msdn.microsoft.com/library/windows/hardware/ff560187) (0x00020006), [**Bug Check 0xA: IRQL\_NOT\_LESS\_OR\_EQUAL**](https://msdn.microsoft.com/library/windows/hardware/ff560129) |

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
<td align="left"><p>Run <a href="https://msdn.microsoft.com/library/windows/hardware/ff552808" data-raw-source="[Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808)">Static Driver Verifier</a> and specify the <strong>IrqlExApcLte2</strong> rule.</p>
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
<td align="left"><p>Run <a href="https://msdn.microsoft.com/library/windows/hardware/ff545448" data-raw-source="[Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff545448)">Driver Verifier</a> and select the <a href="https://msdn.microsoft.com/library/windows/hardware/hh454208" data-raw-source="[DDI compliance checking](https://msdn.microsoft.com/library/windows/hardware/hh454208)">DDI compliance checking</a> option.</p></td>
</tr>
</tbody>
</table>

 

Applies to
----------

[**CmRegisterCallback**](https://msdn.microsoft.com/library/windows/hardware/ff541918)
[**CmRegisterCallbackEx**](https://msdn.microsoft.com/library/windows/hardware/ff541921)
[**CmUnRegisterCallback**](https://msdn.microsoft.com/library/windows/hardware/ff541928)
[**ExDeletePagedLookasideList**](https://msdn.microsoft.com/library/windows/hardware/ff544570)
[**ExInitializePagedLookasideList**](https://msdn.microsoft.com/library/windows/hardware/ff545309)
[**ExRegisterCallback**](https://msdn.microsoft.com/library/windows/hardware/ff545534)
[**ExSetTimerResolution**](https://msdn.microsoft.com/library/windows/hardware/ff545614)
[**ExUnregisterCallback**](https://msdn.microsoft.com/library/windows/hardware/ff545649)
[**ProbeForRead**](https://msdn.microsoft.com/library/windows/hardware/ff559876)
[**ProbeForWrite**](https://msdn.microsoft.com/library/windows/hardware/ff559879)
 

 





