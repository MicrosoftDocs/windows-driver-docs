---
title: WdfInterruptLockRelease rule (kmdf)
description: The WdfInterruptLockRelease rule specifies that calls to WdfInterruptAcquireLock and WdfInterruptReleaseLock are used in a balanced way within a KMDF callback routine.
ms.date: 05/21/2018
keywords: ["WdfInterruptLockRelease rule (kmdf)"]
topic_type:
- apiref
api_name:
- WdfInterruptLockRelease
api_type:
- NA
ms.localizationpriority: medium
---

# WdfInterruptLockRelease rule (kmdf)


The **WdfInterruptLockRelease** rule specifies that calls to [**WdfInterruptAcquireLock**](/previous-versions/ff547340(v=vs.85)) and [**WdfInterruptReleaseLock**](/previous-versions/ff547376(v=vs.85)) are used in a balanced way within a KMDF callback routine. At the end of any KMDF callback routine, the driver should not hold the framework spin lock object that was obtained by a previous call to **WdfInterruptAcquireLock**.

**Driver model: KMDF**

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
<td align="left"><p>Run <a href="/windows-hardware/drivers/devtest/static-driver-verifier" data-raw-source="[Static Driver Verifier](./static-driver-verifier.md)">Static Driver Verifier</a> and specify the <strong>WdfInterruptLockRelease</strong> rule.</p>
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

[**WdfInterruptAcquireLock**](/previous-versions/ff547340(v=vs.85))
[**WdfInterruptReleaseLock**](/previous-versions/ff547376(v=vs.85))
