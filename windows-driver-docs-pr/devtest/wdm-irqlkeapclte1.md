---
title: IrqlKeApcLte1 rule (wdm)
ms.assetid: d88e3c0f-574b-41df-97ee-282a9f1eb6f4
ms.date: 05/21/2018
description: 
keywords: ["IrqlKeApcLte1 rule (wdm)"]
topic_type:
- apiref
api_name:
- IrqlKeApcLte1
api_type:
- NA
ms.localizationpriority: medium
---

# IrqlKeApcLte1 rule (wdm)


The **IrqlKeApcLte1** rule specifies that the driver calls the following kernel routines only when it is executing at IRQL &lt;= APC\_LEVEL:

-   [**KeAcquireGuardedMutex**](https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff551892(v=vs.85))

-   [**KeAcquireGuardedMutexUnsafe**](https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff551894(v=vs.85))

-   [**KeDelayExecutionThread**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nf-wdm-kedelayexecutionthread)

-   [**KeQueryActiveProcessors**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nf-wdm-kequeryactiveprocessors)

-   [**KeReleaseGuardedMutex**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nf-wdm-kereleaseguardedmutex)

-   [**KeReleaseGuardedMutexUnsafe**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nf-wdm-kereleaseguardedmutexunsafe)

-   [**KeTryToAcquireGuardedMutex**](https://msdn.microsoft.com/library/windows/hardware/ff553307)

|              |     |
|--------------|-----|
| Driver model | WDM |

|                                   |                                                                                                                                       |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Bug check(s) found with this rule | [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](https://docs.microsoft.com/windows-hardware/drivers/debugger/bug-check-0xc4--driver-verifier-detected-violation) (0x0002000F) |

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
<td align="left"><p>Run <a href="https://docs.microsoft.com/windows-hardware/drivers/devtest/static-driver-verifier" data-raw-source="[Static Driver Verifier](https://docs.microsoft.com/windows-hardware/drivers/devtest/static-driver-verifier)">Static Driver Verifier</a> and specify the <strong>IrqlKeApcLte1</strong> rule.</p>
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

[**KeAcquireGuardedMutex**](https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff551892(v=vs.85))
[**KeAcquireGuardedMutexUnsafe**](https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff551894(v=vs.85))
[**KeDelayExecutionThread**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nf-wdm-kedelayexecutionthread)
[**KeQueryActiveProcessors**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nf-wdm-kequeryactiveprocessors)
[**KeReleaseGuardedMutex**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nf-wdm-kereleaseguardedmutex)
[**KeReleaseGuardedMutexUnsafe**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nf-wdm-kereleaseguardedmutexunsafe)
[**KeTryToAcquireGuardedMutex**](https://msdn.microsoft.com/library/windows/hardware/ff553307)
 

 





