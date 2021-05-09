---
title: MarkingQueuedIrps rule (wdm)
description: The MarkingQueuedIrps rule specifies that the driver calls IoMarkIrpPending for an IRP that requires further processing only while holding a spin lock. This rule applies only when the driver adds the IRP to a driver-managed queue.
ms.date: 05/21/2018
keywords: ["MarkingQueuedIrps rule (wdm)"]
topic_type:
- apiref
api_name:
- MarkingQueuedIrps
api_type:
- NA
ms.localizationpriority: medium
---

# MarkingQueuedIrps rule (wdm)


The **MarkingQueuedIrps** rule specifies that the driver calls [**IoMarkIrpPending**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iomarkirppending) for an IRP that requires further processing only while holding a spin lock. This rule applies only when the driver adds the IRP to a driver-managed queue.

Specifically, the driver violates this rule only when *all* of the following events occur.

-   The driver calls [**KeAcquireSpinLock**](/windows-hardware/drivers/ddi/wdm/nf-wdm-keacquirespinlock) or [**KeAcquireInStackQueuedSpinLock**](/previous-versions/windows/hardware/drivers/ff551899(v=vs.85)) to acquire a spin lock.

-   The driver calls one of the following routines to add an IRP to a driver-managed queue:
    -   [**InsertHeadList**](/windows-hardware/drivers/ddi/wdm/nf-wdm-insertheadlist)
    -   [**InsertTailList**](/windows-hardware/drivers/ddi/wdm/nf-wdm-inserttaillist)
    -   [**KeInsertDeviceQueue**](/windows-hardware/drivers/ddi/wdm/nf-wdm-keinsertdevicequeue)
    -   [**KeInsertQueueDpc**](/windows-hardware/drivers/ddi/wdm/nf-wdm-keinsertqueuedpc)
    -   [**KeInsertByKeyDeviceQueue**](/windows-hardware/drivers/ddi/wdm/nf-wdm-keinsertbykeydevicequeue)
-   The driver calls [**KeReleaseSpinLock**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kereleasespinlock) or [**KeReleaseInStackQueuedSpinLock**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kereleaseinstackqueuedspinlock) to release the spin lock before it calls **IoMarkIrpPending**.

-   The driver returns a status of STATUS\_PENDING for the IRP.

Drivers should call **IoMarkIrpPending** for a queued IRP only while holding a spin lock. Otherwise, an IRP could be dequeued, completed by another driver routine, and freed by the system before the call to **IoMarkIrpPending** occurs, thereby causing a crash.

For more information, see [**Synchronizing IRP Cancellation**](../kernel/synchronizing-irp-cancellation.md).

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
<td align="left"><p>Run <a href="/windows-hardware/drivers/devtest/static-driver-verifier" data-raw-source="[Static Driver Verifier](./static-driver-verifier.md)">Static Driver Verifier</a> and specify the <strong>MarkingQueuedIrps</strong> rule.</p>
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

[**InsertHeadList**](/windows-hardware/drivers/ddi/wdm/nf-wdm-insertheadlist)
[**IoCallDriver**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocalldriver)
[**IoMarkIrpPending**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iomarkirppending)
[**KeAcquireInStackQueuedSpinLock**](/previous-versions/windows/hardware/drivers/ff551899(v=vs.85))
[**KeAcquireSpinLock**](/windows-hardware/drivers/ddi/wdm/nf-wdm-keacquirespinlock)
[**KeInsertByKeyDeviceQueue**](/windows-hardware/drivers/ddi/wdm/nf-wdm-keinsertbykeydevicequeue)
[**KeInsertDeviceQueue**](/windows-hardware/drivers/ddi/wdm/nf-wdm-keinsertdevicequeue)
[**KeInsertQueueDpc**](/windows-hardware/drivers/ddi/wdm/nf-wdm-keinsertqueuedpc)
[**KeReleaseInStackQueuedSpinLock**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kereleaseinstackqueuedspinlock)
[**KeReleaseSpinLock**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kereleasespinlock)
[**PoCallDriver**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-pocalldriver)
[**RemoveHeadList**](/windows-hardware/drivers/ddi/wdm/nf-wdm-removeheadlist)
