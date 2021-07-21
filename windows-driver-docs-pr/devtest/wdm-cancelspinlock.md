---
title: CancelSpinLock rule (wdm)
description: The CancelSpinLock rule specifies that the driver calls IoAcquireCancelSpinLock before calling IoReleaseCancelSpinLock and that the driver calls IoReleaseCancelSpinLock before any subsequent calls to IoAcquireCancelSpinLock.
ms.date: 05/21/2018
keywords: ["CancelSpinLock rule (wdm)"]
topic_type:
- apiref
api_name:
- CancelSpinLock
api_type:
- NA
ms.localizationpriority: medium
---

# CancelSpinLock rule (wdm)


The CancelSpinLock rule specifies that the driver calls [**IoAcquireCancelSpinLock**](/previous-versions/windows/hardware/drivers/ff548196(v=vs.85)) before calling [**IoReleaseCancelSpinLock**](/previous-versions/windows/hardware/drivers/ff549550(v=vs.85)) and that the driver calls **IoReleaseCancelSpinLock** before any subsequent calls to **IoAcquireCancelSpinLock**.

This rule also specifies that the driver must not hold any spin locks when the dispatch routine or cancel routine ends. Nested calls are permitted.

**Driver model: WDM**

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
<td align="left"><p>Run <a href="/windows-hardware/drivers/devtest/static-driver-verifier" data-raw-source="[Static Driver Verifier](./static-driver-verifier.md)">Static Driver Verifier</a> and specify the <strong>CancelSpinLock</strong> rule.</p>
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

[**IoAcquireCancelSpinLock**](/previous-versions/windows/hardware/drivers/ff548196(v=vs.85))
[**IoReleaseCancelSpinLock**](/previous-versions/windows/hardware/drivers/ff549550(v=vs.85))
[**RemoveHeadList**](/windows-hardware/drivers/ddi/wdm/nf-wdm-removeheadlist)
