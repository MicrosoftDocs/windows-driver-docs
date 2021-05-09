---
title: ExclusiveResourceAccess rule (wdm)
description: The ExclusiveResourceAccess rule specifies that the driver calls ExAcquireResourceExclusiveLite before calling ExReleaseResourceLite or ExReleaseResourceForThreadLite and specifies that the driver calls ExReleaseResourceLite or ExReleaseResourceForThreadLite before any subsequent calls to ExAcquireResourceExclusiveLite.
ms.date: 05/21/2018
keywords: ["ExclusiveResourceAccess rule (wdm)"]
topic_type:
- apiref
api_name:
- ExclusiveResourceAccess
api_type:
- NA
ms.localizationpriority: medium
---

# ExclusiveResourceAccess rule (wdm)


The **ExclusiveResourceAccess** rule specifies that the driver calls [**ExAcquireResourceExclusiveLite**](/previous-versions/ff544351(v=vs.85)) before calling [**ExReleaseResourceLite**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exreleaseresourcelite) or [**ExReleaseResourceForThreadLite**](/previous-versions/ff545585(v=vs.85)) and specifies that the driver calls **ExReleaseResourceLite** or **ExReleaseResourceForThreadLite** before any subsequent calls to **ExAcquireResourceExclusiveLite**.

Nested calls are permitted if they are acquiring and releasing different resources. Nested calls to acquire or release the same resources violate this rule.

This rule also states that when the routine ends, the driver must not have exclusive access to the resource. Static Driver Verifier monitors the end of the **DriverEntry**, **AddDevice**, **StartIo**, **StartDevice**, **DpcForIsr**, **Cancel**, **Dispatch**, **RemoveDevice**, and **Unload** routines.

**Driver model: WDM**

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left">Bug check(s) found with this rule</td>
<td align="left"></td>
</tr>
</tbody>
</table>

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
<td align="left"><p>Run <a href="/windows-hardware/drivers/devtest/static-driver-verifier" data-raw-source="[Static Driver Verifier](./static-driver-verifier.md)">Static Driver Verifier</a> and specify the <strong>ExclusiveResourceAccess</strong> rule.</p>
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

## Applies to

[**ExAcquireResourceExclusiveLite**](/previous-versions/ff544351(v=vs.85))
[**ExReleaseResourceForThreadLite**](/previous-versions/ff545585(v=vs.85))
[**ExReleaseResourceLite**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exreleaseresourcelite)
## See also

[**Preventing Errors and Deadlocks While Using Spin Locks**](../kernel/preventing-errors-and-deadlocks-while-using-spin-locks.md)
