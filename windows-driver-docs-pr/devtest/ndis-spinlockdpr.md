---
title: SpinLockDpr Rule (NDIS)
description: The SpinLockDpr rule verifies the correct use of the NDIS spin lock interface.This rule specifies that calls to NdisDprAcquireSpinLock are made only when the spin lock is in the unlocked state.
ms.date: 05/21/2018
keywords: ["SpinLockDpr rule (ndis)"]
topic_type:
- apiref
ms.topic: reference
api_name:
- SpinLockDpr
api_type:
- NA
---

# SpinLockDpr rule (ndis)


The **SpinLockDpr** rule verifies the correct use of the NDIS spin lock interface.

This rule specifies that calls to [**NdisDprAcquireSpinLock**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisdpracquirespinlock) are made only when the spin lock is in the unlocked state. This rule also verifies that the spin lock is released before the miniport handler routine exits.

**Driver model: NDIS**

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
<td align="left"><p>Run <a href="/windows-hardware/drivers/devtest/static-driver-verifier" data-raw-source="[Static Driver Verifier](./static-driver-verifier.md)">Static Driver Verifier</a> and specify the <strong>SpinLockDpr</strong> rule.</p>
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

[**NdisAcquireSpinLock**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisacquirespinlock)
[**NdisAllocateSpinLock**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisallocatespinlock)
[**NdisDprAcquireSpinLock**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisdpracquirespinlock)
[**NdisDprReleaseSpinLock**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisdprreleasespinlock)
[**NdisReleaseSpinLock**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisreleasespinlock)
