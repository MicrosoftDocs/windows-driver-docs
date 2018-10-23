---
title: IrqlExPassive rule (wdm)
description: The IrqlExPassive rule specifies that the driver calls the following executive support routines only at IRQL�  PASSIVE\_LEVEL ExCreateCallbackExIsProcessorFeaturePresentExRaiseAccessViolationExRaiseDatatypeMisalignmentExRaiseStatusExUuidCreateThe IrqlExPassive rule also specifies that the driver calls ExRaiseStatus at IRQL APC\_LEVEL.
ms.assetid: 92d73bd9-ce79-4be8-9ea2-a5aef2ea6edb
ms.date: 05/21/2018
keywords: ["IrqlExPassive rule (wdm)"]
topic_type:
- apiref
api_name:
- IrqlExPassive
api_type:
- NA
ms.localizationpriority: medium
---

# IrqlExPassive rule (wdm)


The **IrqlExPassive** rule specifies that the driver calls the following executive support routines only at IRQL = PASSIVE\_LEVEL:

-   [**ExCreateCallback**](https://msdn.microsoft.com/library/windows/hardware/ff544560)

-   [**ExIsProcessorFeaturePresent**](https://msdn.microsoft.com/library/windows/hardware/ff545442)

-   [**ExRaiseAccessViolation**](https://msdn.microsoft.com/library/windows/hardware/ff545509)

-   [**ExRaiseDatatypeMisalignment**](https://msdn.microsoft.com/library/windows/hardware/ff545524)

-   [**ExRaiseStatus**](https://msdn.microsoft.com/library/windows/hardware/ff545529)

-   [**ExUuidCreate**](https://msdn.microsoft.com/library/windows/hardware/ff545658)

The **IrqlExPassive** rule also specifies that the driver calls [**ExRaiseStatus**](https://msdn.microsoft.com/library/windows/hardware/ff545529) at IRQL &lt;= APC\_LEVEL.
|              |     |
|--------------|-----|
| Driver model | WDM |

|                                   |                                                                                                                                                                                                                                        |
|-----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Bug check(s) found with this rule | [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](https://msdn.microsoft.com/library/windows/hardware/ff560187) (0x00020008), [**Bug Check 0xA: IRQL\_NOT\_LESS\_OR\_EQUAL**](https://msdn.microsoft.com/library/windows/hardware/ff560129) |

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>IrqlExPassive</strong> rule.</p>
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

[**ExCreateCallback**](https://msdn.microsoft.com/library/windows/hardware/ff544560)
[**ExIsProcessorFeaturePresent**](https://msdn.microsoft.com/library/windows/hardware/ff545442)
[**ExRaiseAccessViolation**](https://msdn.microsoft.com/library/windows/hardware/ff545509)
[**ExRaiseDatatypeMisalignment**](https://msdn.microsoft.com/library/windows/hardware/ff545524)
[**ExRaiseStatus**](https://msdn.microsoft.com/library/windows/hardware/ff545529)
[**ExUuidCreate**](https://msdn.microsoft.com/library/windows/hardware/ff545658)
See also
--------

[**Managing Hardware Priorities**](https://msdn.microsoft.com/library/windows/hardware/ff554368)
[**Preventing Errors and Deadlocks While Using Spin Locks**](https://msdn.microsoft.com/library/windows/hardware/ff559854)
 

 





