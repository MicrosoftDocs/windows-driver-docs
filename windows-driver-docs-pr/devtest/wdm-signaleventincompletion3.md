---
title: SignalEventInCompletion3 rule (wdm)
description: The SignalEventInCompletion3 rule specifies that when processing a asynchronous IRP, the driver needs to call the KeSetEvent in the completion routine when the Irp- PendingReturned flag is set.
ms.date: 05/21/2018
keywords: ["SignalEventInCompletion3 rule (wdm)"]
topic_type:
- apiref
api_name:
- SignalEventInCompletion3
api_type:
- NA
ms.localizationpriority: medium
---

# SignalEventInCompletion3 rule (wdm)


The **SignalEventInCompletion3** rule specifies that when processing a asynchronous IRP, the driver needs to call the [**KeSetEvent**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kesetevent) in the completion routine when the **Irp-&gt;PendingReturned** flag is set.

In this case, the completion routine will not be called.

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
<td align="left"><p>Run <a href="/windows-hardware/drivers/devtest/static-driver-verifier" data-raw-source="[Static Driver Verifier](./static-driver-verifier.md)">Static Driver Verifier</a> and specify the <strong>SignalEventInCompletion3</strong> rule.</p>
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

[**IoSetCompletionRoutine**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iosetcompletionroutine)
[**IoSetCompletionRoutineEx**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iosetcompletionroutineex)
[**KeInitializeEvent**](/windows-hardware/drivers/ddi/wdm/nf-wdm-keinitializeevent)
