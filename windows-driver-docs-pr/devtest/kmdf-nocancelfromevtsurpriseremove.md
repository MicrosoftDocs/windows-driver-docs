---
title: NoCancelFromEvtSurpriseRemove rule (kmdf)
description: The NoCancelFromEvtSurpriseRemove rule specifies that WDF Drivers shouldn’t cancel requests from the EvtDeviceSurpriseRemoval callback function, instead self-managed I/O callback functions should be used.
ms.date: 05/21/2018
keywords: ["NoCancelFromEvtSurpriseRemove rule (kmdf)"]
topic_type:
- apiref
api_name:
- NoCancelFromEvtSurpriseRemove
api_type:
- NA
ms.localizationpriority: medium
---

# NoCancelFromEvtSurpriseRemove rule (kmdf)


The **NoCancelFromEvtSurpriseRemove** rule specifies that WDF Drivers shouldn’t cancel requests from the [*EvtDeviceSurpriseRemoval*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_surprise_removal) callback function, instead self-managed I/O callback functions should be used. *EvtDeviceSurpriseRemoval* callback function isn’t synchronized with the power-down path.

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
<td align="left"><p>Run <a href="/windows-hardware/drivers/devtest/static-driver-verifier" data-raw-source="[Static Driver Verifier](./static-driver-verifier.md)">Static Driver Verifier</a> and specify the <strong>NoCancelFromEvtSurpriseRemove</strong> rule.</p>
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

[**WdfIoQueueDrain**](/windows-hardware/drivers/ddi/wdfio/nf-wdfio-wdfioqueuedrain)
[**WdfIoQueueDrainSynchronously**](/windows-hardware/drivers/ddi/wdfio/nf-wdfio-wdfioqueuedrainsynchronously)
[**WdfIoQueuePurge**](/windows-hardware/drivers/ddi/wdfio/nf-wdfio-wdfioqueuepurge)
[**WdfIoQueuePurgeSynchronously**](/windows-hardware/drivers/ddi/wdfio/nf-wdfio-wdfioqueuepurgesynchronously)
[**WdfIoQueueStop**](/windows-hardware/drivers/ddi/wdfio/nf-wdfio-wdfioqueuestop)
[**WdfIoQueueStopAndPurge**](/windows-hardware/drivers/ddi/wdfio/nf-wdfio-wdfioqueuestopandpurge)
[**WdfIoQueueStopAndPurgeSynchronously**](/windows-hardware/drivers/ddi/wdfio/nf-wdfio-wdfioqueuestopandpurgesynchronously)
[**WdfIoQueueStopSynchronously**](/windows-hardware/drivers/ddi/wdfio/nf-wdfio-wdfioqueuestopsynchronously)
[**WdfRequestComplete**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestcomplete)
[**WdfRequestCompleteWithInformation**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestcompletewithinformation)
[**WdfRequestCompleteWithPriorityBoost**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestcompletewithpriorityboost)
