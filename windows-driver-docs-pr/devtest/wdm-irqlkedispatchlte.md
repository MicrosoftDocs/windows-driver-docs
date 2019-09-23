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

-   [**KeAcquireSpinLock**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-keacquirespinlock)

-   [**KeCancelTimer**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-kecanceltimer)

-   [**KeClearEvent**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-keclearevent)

-   [**KeFlushIoBuffers**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-keflushiobuffers)

-   [**KeInitializeDeviceQueue**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-keinitializedevicequeue)

-   [**KeInitializeTimer**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-keinitializetimer)

-   [**KeInitializeTimerEx**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-keinitializetimerex)

-   [**KePulseEvent**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntddk/nf-ntddk-kepulseevent)

-   [**KeRaiseIrqlToDpcLevel**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-keraiseirqltodpclevel)

-   [**KeReadStateEvent**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-kereadstateevent)

-   [**KeReadStateTimer**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-kereadstatetimer)

-   [**KeReleaseMutex**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-kereleasemutex)

-   [**KeRemoveEntryDeviceQueue**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-keremoveentrydevicequeue)

-   [**KeResetEvent**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-keresetevent)

-   [**KeSaveFloatingPointState**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-kesavefloatingpointstate)

-   [**KeSetTimer**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-kesettimer)

-   [**KeSetTimerEx**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-kesettimerex)

|              |     |
|--------------|-----|
| Driver model | WDM |

|                                   |                                                                                                                                       |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Bug check(s) found with this rule | [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](https://docs.microsoft.com/windows-hardware/drivers/debugger/bug-check-0xc4--driver-verifier-detected-violation) (0x00020011) |

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
<td align="left"><p>Run <a href="https://docs.microsoft.com/windows-hardware/drivers/devtest/static-driver-verifier" data-raw-source="[Static Driver Verifier](https://docs.microsoft.com/windows-hardware/drivers/devtest/static-driver-verifier)">Static Driver Verifier</a> and specify the <strong>IrqlKeDispatchLte</strong> rule.</p>
Use the following steps to run an analysis of your code:
<ol>
<li><a href="https://docs.microsoft.com/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers#preparing-your-source-code" data-raw-source="[Prepare your code (use role type declarations).](https://docs.microsoft.com/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers#preparing-your-source-code)">Prepare your code (use role type declarations).</a></li>
<li><a href="https://docs.microsoft.com/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers#running-static-driver-verifier" data-raw-source="[Run Static Driver Verifier.](https://docs.microsoft.com/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers#running-static-driver-verifier)">Run Static Driver Verifier.</a></li>
<li><a href="https://docs.microsoft.com/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers#viewing-and-analyzing-the-results" data-raw-source="[View and analyze the results.](https://docs.microsoft.com/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers#viewing-and-analyzing-the-results)">View and analyze the results.</a></li>
</ol>
<p>For more information, see <a href="https://docs.microsoft.com/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers" data-raw-source="[Using Static Driver Verifier to Find Defects in Drivers](https://docs.microsoft.com/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers)">Using Static Driver Verifier to Find Defects in Drivers</a>.</p></td>
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
<td align="left"><p>Run <a href="https://docs.microsoft.com/windows-hardware/drivers/devtest/driver-verifier" data-raw-source="[Driver Verifier](https://docs.microsoft.com/windows-hardware/drivers/devtest/driver-verifier)">Driver Verifier</a> and select the <a href="https://docs.microsoft.com/windows-hardware/drivers/devtest/ddi-compliance-checking" data-raw-source="[DDI compliance checking](https://docs.microsoft.com/windows-hardware/drivers/devtest/ddi-compliance-checking)">DDI compliance checking</a> option.</p></td>
</tr>
</tbody>
</table>

 

Applies to
----------

[**KeAcquireSpinLock**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-keacquirespinlock)
[**KeCancelTimer**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-kecanceltimer)
[**KeClearEvent**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-keclearevent)
[**KeInitializeDeviceQueue**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-keinitializedevicequeue)
[**KeInitializeSemaphore**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-keinitializesemaphore)
[**KeInitializeTimer**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-keinitializetimer)
[**KeInitializeTimerEx**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-keinitializetimerex)
[**KePulseEvent**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntddk/nf-ntddk-kepulseevent)
[**KeReadStateEvent**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-kereadstateevent)
[**KeReadStateTimer**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-kereadstatetimer)
[**KeReleaseMutex**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-kereleasemutex)
[**KeRemoveEntryDeviceQueue**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-keremoveentrydevicequeue)
[**KeResetEvent**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-keresetevent)
[**KeSaveFloatingPointState**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-kesavefloatingpointstate)
[**KeSetTimer**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-kesettimer)
[**KeSetTimerEx**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-kesettimerex)
 

 





