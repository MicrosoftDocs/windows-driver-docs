---
title: DeleteDevice rule (wdm)
description: The DeleteDevice rule specifies that drivers should not rely on the I/O Manager or PnP Manager to keep the DeviceObject alive after a call to IoDeleteDevice.
ms.date: 05/21/2018
keywords: ["DeleteDevice rule (wdm)"]
topic_type:
- apiref
api_name:
- DeleteDevice
api_type:
- NA
ms.localizationpriority: medium
---

# DeleteDevice rule (wdm)


The **DeleteDevice** rule specifies that drivers should not rely on the I/O Manager or PnP Manager to keep the DeviceObject alive after a call to [**IoDeleteDevice**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iodeletedevice).

Drivers should call [**IoDeleteDevice**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iodeletedevice) after the lower driver has returned. This is the recommended behavior. This rule applies to FDO and FIDO drivers.

When handling an [**IRP\_MN\_REMOVE\_DEVICE**](../kernel/irp-mn-remove-device.md) request, the driver should only call [**IoDeleteDevice**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iodeletedevice) after [**IoCallDriver**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocalldriver) or [**PoCallDriver**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-pocalldriver) have returned.

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
<td align="left"><p>Run <a href="/windows-hardware/drivers/devtest/static-driver-verifier" data-raw-source="[Static Driver Verifier](./static-driver-verifier.md)">Static Driver Verifier</a> and specify the <strong>DeleteDevice</strong> rule.</p>
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

[**IoCallDriver**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocalldriver)
[**IoDeleteDevice**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iodeletedevice)
[**PoCallDriver**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-pocalldriver)
