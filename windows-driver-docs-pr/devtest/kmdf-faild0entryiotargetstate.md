---
title: FailD0EntryIoTargetState rule (kmdf)
description: The FailD0EntryIoTargetState rule specifies that an I/O target for a USB continuous reader started within the EvtDeviceD0Entry will get stopped appropriately from the same callback if the EvtDeviceD0Entry fails.
ms.date: 05/21/2018
keywords: ["FailD0EntryIoTargetState rule (kmdf)"]
topic_type:
- apiref
api_name:
- FailD0EntryIoTargetState
api_type:
- NA
ms.localizationpriority: medium
---

# FailD0EntryIoTargetState rule (kmdf)


The **FailD0EntryIoTargetState** rule specifies that an I/O target for a USB continuous reader started within the [*EvtDeviceD0Entry*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_d0_entry) will get stopped appropriately from the same callback if the *EvtDeviceD0Entry* fails.

When [*EvtDeviceD0Entry*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_d0_entry) callback function fails, the framework doesn’t execute the driver’s [*EvtDeviceD0Exit*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_d0_exit) callback function.

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
<td align="left"><p>Run <a href="/windows-hardware/drivers/devtest/static-driver-verifier" data-raw-source="[Static Driver Verifier](./static-driver-verifier.md)">Static Driver Verifier</a> and specify the <strong>FailD0EntryIoTargetState</strong> rule.</p>
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

[**WdfIoTargetStart**](/windows-hardware/drivers/ddi/wdfiotarget/nf-wdfiotarget-wdfiotargetstart)
[**WdfIoTargetStop**](/windows-hardware/drivers/ddi/wdfiotarget/nf-wdfiotarget-wdfiotargetstop)
[**WdfUsbTargetPipeConfigContinuousReader**](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetpipeconfigcontinuousreader)
[**WdfUsbTargetPipeGetIoTarget**](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetpipegetiotarget)
