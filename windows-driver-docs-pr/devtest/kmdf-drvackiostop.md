---
title: DrvAckIoStop rule (kmdf)
description: The DrvAckIoStop rule verifies that the driver is aware of pending requests while its power-managed queue is getting powered-down and the driver acknowledges, completes, or cancels the pending requests accordingly.
ms.date: 05/21/2018
keywords: ["DrvAckIoStop rule (kmdf)"]
topic_type:
- apiref
api_name:
- DrvAckIoStop
api_type:
- NA
ms.localizationpriority: medium
---

# DrvAckIoStop rule (kmdf)


The **DrvAckIoStop** rule verifies that the driver is aware of pending requests while its power-managed queue is getting powered-down and the driver acknowledges, completes, or cancels the pending requests accordingly. In the case of self-managed I/O requests, the driver should also correctly handle these requests from its [*EvtDeviceSelfManagedIoSuspend*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_self_managed_io_suspend) function. A driver that fails to handle these requests during a power-down would cause [**Bug Check 0x9F: DRIVER\_POWER\_STATE\_FAILURE**](../debugger/bug-check-0x9f--driver-power-state-failure.md).

In some circumstances it might be appropriate to suppress this warning. If the driver does not hold on to the requests, or does not forward them to other drivers, and if the driver completes the requests directly in the queue's handlers, you can use the **\_\_analysis\_assume** function to suppress the warning. For more information, see [Using the \_analysis\_assume Function to Suppress False Defects](./using-the--analysis-assume-function-to-suppress-false-defects.md) and [**How to: Specify Additional Code Information by Using \_\_analysis\_assume**](/visualstudio/code-quality/how-to-specify-additional-code-information-by-using-analysis-assume).

**Driver model: KMDF**

**Bug check(s) found with this rule**: [**Bug Check 0x9F: DRIVER\_POWER\_STATE\_FAILURE**](../debugger/bug-check-0x9f--driver-power-state-failure.md)


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
<td align="left"><p>Run <a href="/windows-hardware/drivers/devtest/static-driver-verifier" data-raw-source="[Static Driver Verifier](./static-driver-verifier.md)">Static Driver Verifier</a> and specify the <strong>DrvAckIoStop</strong> rule.</p>
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

[**WdfDeviceInitSetPnpPowerEventCallbacks**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceinitsetpnppowereventcallbacks)
[**WdfFdoInitSetFilter**](/windows-hardware/drivers/ddi/wdffdo/nf-wdffdo-wdffdoinitsetfilter)
[**WdfIoQueueCreate**](/windows-hardware/drivers/ddi/wdfio/nf-wdfio-wdfioqueuecreate)
