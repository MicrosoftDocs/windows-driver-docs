---
title: IrqlKeDispatchLte rule (wdm)
ms.date: 05/21/2018
description: "Learn more about: IrqlKeDispatchLte rule (wdm)"
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

-   [**KeAcquireSpinLock**](/windows-hardware/drivers/ddi/wdm/nf-wdm-keacquirespinlock)

-   [**KeCancelTimer**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kecanceltimer)

-   [**KeClearEvent**](/windows-hardware/drivers/ddi/wdm/nf-wdm-keclearevent)

-   [**KeFlushIoBuffers**](/windows-hardware/drivers/ddi/wdm/nf-wdm-keflushiobuffers)

-   [**KeInitializeDeviceQueue**](/windows-hardware/drivers/ddi/wdm/nf-wdm-keinitializedevicequeue)

-   [**KeInitializeTimer**](/windows-hardware/drivers/ddi/wdm/nf-wdm-keinitializetimer)

-   [**KeInitializeTimerEx**](/windows-hardware/drivers/ddi/wdm/nf-wdm-keinitializetimerex)

-   [**KePulseEvent**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-kepulseevent)

-   [**KeRaiseIrqlToDpcLevel**](/windows-hardware/drivers/ddi/wdm/nf-wdm-keraiseirqltodpclevel)

-   [**KeReadStateEvent**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kereadstateevent)

-   [**KeReadStateTimer**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kereadstatetimer)

-   [**KeReleaseMutex**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kereleasemutex)

-   [**KeRemoveEntryDeviceQueue**](/windows-hardware/drivers/ddi/wdm/nf-wdm-keremoveentrydevicequeue)

-   [**KeResetEvent**](/windows-hardware/drivers/ddi/wdm/nf-wdm-keresetevent)

-   [**KeSaveFloatingPointState**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kesavefloatingpointstate)

-   [**KeSetTimer**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kesettimer)

-   [**KeSetTimerEx**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kesettimerex)

**Driver model: WDM**

**Bug check(s) found with this rule**: [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](../debugger/bug-check-0xc4--driver-verifier-detected-violation.md) (0x00020011)


## How to test

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
<td align="left"><p>Run <a href="/windows-hardware/drivers/devtest/static-driver-verifier" data-raw-source="[Static Driver Verifier](./static-driver-verifier.md)">Static Driver Verifier</a> and specify the <strong>IrqlKeDispatchLte</strong> rule.</p>
Use the following steps to run an analysis of your code:
<ol>
<li><a href="/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers#preparing-your-source-code" data-raw-source="[Prepare your code (use role type declarations).](./using-static-driver-verifier-to-find-defects-in-drivers.md#preparing-your-source-code)">Prepare your code (use role type declarations).</a></li>
<li><a href="/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers#running-static-driver-verifier" data-raw-source="[Run Static Driver Verifier.](./using-static-driver-verifier-to-find-defects-in-drivers.md#running-static-driver-verifier)">Run Static Driver Verifier.</a></li>
<li><a href="/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers#viewing-and-analyzing-the-results" data-raw-source="[View and analyze the results.](./using-static-driver-verifier-to-find-defects-in-drivers.md#viewing-and-analyzing-the-results)">View and analyze the results.</a></li>
</ol>
<p>For more information, see <a href="/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers" data-raw-source="[Using Static Driver Verifier to Find Defects in Drivers](./using-static-driver-verifier-to-find-defects-in-drivers.md)">Using Static Driver Verifier to Find Defects in Drivers</a>.</p></td>
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
<td align="left"><p>Run <a href="/windows-hardware/drivers/devtest/driver-verifier" data-raw-source="[Driver Verifier](./driver-verifier.md)">Driver Verifier</a> and select the <a href="/windows-hardware/drivers/devtest/ddi-compliance-checking" data-raw-source="[DDI compliance checking](./ddi-compliance-checking.md)">DDI compliance checking</a> option.</p></td>
</tr>
</tbody>
</table>

 

## Applies to

[**KeAcquireSpinLock**](/windows-hardware/drivers/ddi/wdm/nf-wdm-keacquirespinlock)
[**KeCancelTimer**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kecanceltimer)
[**KeClearEvent**](/windows-hardware/drivers/ddi/wdm/nf-wdm-keclearevent)
[**KeInitializeDeviceQueue**](/windows-hardware/drivers/ddi/wdm/nf-wdm-keinitializedevicequeue)
[**KeInitializeSemaphore**](/windows-hardware/drivers/ddi/wdm/nf-wdm-keinitializesemaphore)
[**KeInitializeTimer**](/windows-hardware/drivers/ddi/wdm/nf-wdm-keinitializetimer)
[**KeInitializeTimerEx**](/windows-hardware/drivers/ddi/wdm/nf-wdm-keinitializetimerex)
[**KePulseEvent**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-kepulseevent)
[**KeReadStateEvent**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kereadstateevent)
[**KeReadStateTimer**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kereadstatetimer)
[**KeReleaseMutex**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kereleasemutex)
[**KeRemoveEntryDeviceQueue**](/windows-hardware/drivers/ddi/wdm/nf-wdm-keremoveentrydevicequeue)
[**KeResetEvent**](/windows-hardware/drivers/ddi/wdm/nf-wdm-keresetevent)
[**KeSaveFloatingPointState**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kesavefloatingpointstate)
[**KeSetTimer**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kesettimer)
[**KeSetTimerEx**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kesettimerex)
