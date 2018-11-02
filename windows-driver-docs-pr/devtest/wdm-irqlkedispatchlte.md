---
title: IrqlKeDispatchLte rule (wdm)
ms.assetid: 425a20ea-c9e3-45f4-a517-6bad9ab0de98
ms.date: 05/21/2018
description: 
keywords: ["IrqlKeDispatchLte rule (wdm)"]
topic_type:
- apiref
api_name:
- IrqlKeDispatchLte
api_type:
- NA
ms.localizationpriority: medium
---

# IrqlKeDispatchLte rule (wdm)


The **IrqlKeDispatchLte** rule specifies that the driver calls the following kernel routines only when it is executing at IRQL &lt;= DISPATCH\_LEVEL:

-   [**KeAcquireSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff551917)

-   [**KeCancelTimer**](https://msdn.microsoft.com/library/windows/hardware/ff551970)

-   [**KeClearEvent**](https://msdn.microsoft.com/library/windows/hardware/ff551980)

-   [**KeFlushIoBuffers**](https://msdn.microsoft.com/library/windows/hardware/ff552041)

-   [**KeInitializeDeviceQueue**](https://msdn.microsoft.com/library/windows/hardware/ff552126)

-   [**KeInitializeTimer**](https://msdn.microsoft.com/library/windows/hardware/ff552168)

-   [**KeInitializeTimerEx**](https://msdn.microsoft.com/library/windows/hardware/ff552173)

-   [**KePulseEvent**](https://msdn.microsoft.com/library/windows/hardware/ff552979)

-   [**KeRaiseIrqlToDpcLevel**](https://msdn.microsoft.com/library/windows/hardware/ff553084)

-   [**KeReadStateEvent**](https://msdn.microsoft.com/library/windows/hardware/ff553089)

-   [**KeReadStateTimer**](https://msdn.microsoft.com/library/windows/hardware/ff553099)

-   [**KeReleaseMutex**](https://msdn.microsoft.com/library/windows/hardware/ff553140)

-   [**KeRemoveEntryDeviceQueue**](https://msdn.microsoft.com/library/windows/hardware/ff553163)

-   [**KeResetEvent**](https://msdn.microsoft.com/library/windows/hardware/ff553176)

-   [**KeSaveFloatingPointState**](https://msdn.microsoft.com/library/windows/hardware/ff553243)

-   [**KeSetTimer**](https://msdn.microsoft.com/library/windows/hardware/ff553286)

-   [**KeSetTimerEx**](https://msdn.microsoft.com/library/windows/hardware/ff553292)

|              |     |
|--------------|-----|
| Driver model | WDM |

|                                   |                                                                                                                                       |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Bug check(s) found with this rule | [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](https://msdn.microsoft.com/library/windows/hardware/ff560187) (0x00020011) |

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
<td align="left"><p>Run <a href="https://msdn.microsoft.com/library/windows/hardware/ff552808" data-raw-source="[Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808)">Static Driver Verifier</a> and specify the <strong>IrqlKeDispatchLte</strong> rule.</p>
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

[**KeAcquireSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff551917)
[**KeCancelTimer**](https://msdn.microsoft.com/library/windows/hardware/ff551970)
[**KeClearEvent**](https://msdn.microsoft.com/library/windows/hardware/ff551980)
[**KeInitializeDeviceQueue**](https://msdn.microsoft.com/library/windows/hardware/ff552126)
[**KeInitializeSemaphore**](https://msdn.microsoft.com/library/windows/hardware/ff552150)
[**KeInitializeTimer**](https://msdn.microsoft.com/library/windows/hardware/ff552168)
[**KeInitializeTimerEx**](https://msdn.microsoft.com/library/windows/hardware/ff552173)
[**KePulseEvent**](https://msdn.microsoft.com/library/windows/hardware/ff552979)
[**KeReadStateEvent**](https://msdn.microsoft.com/library/windows/hardware/ff553089)
[**KeReadStateTimer**](https://msdn.microsoft.com/library/windows/hardware/ff553099)
[**KeReleaseMutex**](https://msdn.microsoft.com/library/windows/hardware/ff553140)
[**KeRemoveEntryDeviceQueue**](https://msdn.microsoft.com/library/windows/hardware/ff553163)
[**KeResetEvent**](https://msdn.microsoft.com/library/windows/hardware/ff553176)
[**KeSaveFloatingPointState**](https://msdn.microsoft.com/library/windows/hardware/ff553243)
[**KeSetTimer**](https://msdn.microsoft.com/library/windows/hardware/ff553286)
[**KeSetTimerEx**](https://msdn.microsoft.com/library/windows/hardware/ff553292)
 

 





