---
title: MarkingInterlockedQueuedIrps rule (wdm)
description: The MarkingInterlockedQueuedIrps rule specifies that the driver correctly marks the IRP as pending before it queues it in an interlocked fashion for further processing.
ms.date: 05/21/2018
keywords: ["MarkingInterlockedQueuedIrps rule (wdm)"]
topic_type:
- apiref
api_name:
- MarkingInterlockedQueuedIrps
api_type:
- NA
ms.localizationpriority: medium
---

# MarkingInterlockedQueuedIrps rule (wdm)


The **MarkingInterlockedQueuedIrps** rule specifies that the driver correctly marks the IRP as pending before it queues it in an interlocked fashion for further processing.

This rule also specifies that the driver calls [**IoMarkIrpPending**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iomarkirppending) and correctly marks the IRP as pending before it calls any of the following functions to add the IRP to an interlocked queue:

-   [**ExInterlockedInsertHeadList**](/previous-versions/ff545397(v=vs.85))

-   [**ExInterlockedInsertTailList**](/previous-versions/ff545402(v=vs.85))

-   [**ExInterlockedPushEntryList**](/previous-versions/ff545418(v=vs.85))

Drivers should call [**IoMarkIrpPending**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iomarkirppending) before adding an IRP that requires more processing to an interlocked queue. Otherwise, an IRP could be dequeued, completed by another driver routine, and freed by the system before the call to **IoMarkIrpPending** occurs, thereby causing a crash.

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
<td align="left"><p>Run <a href="/windows-hardware/drivers/devtest/static-driver-verifier" data-raw-source="[Static Driver Verifier](./static-driver-verifier.md)">Static Driver Verifier</a> and specify the <strong>MarkingInterlockedQueuedIrps</strong> rule.</p>
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

[**ExInterlockedInsertHeadList**](/previous-versions/ff545397(v=vs.85))
[**ExInterlockedInsertTailList**](/previous-versions/ff545402(v=vs.85))
[**ExInterlockedPushEntryList**](/previous-versions/ff545418(v=vs.85))
[**IoMarkIrpPending**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iomarkirppending)
[**RemoveHeadList**](/windows-hardware/drivers/ddi/wdm/nf-wdm-removeheadlist)
## See also

[**MarkIrpPending**](wdm-markirppending.md)
[**Synchronizing IRP Cancellation**](../kernel/synchronizing-irp-cancellation.md)
