---
title: UsbDeviceCreateTarget rule (kmdf)
description: The UsbDeviceCreateTarget rule specifies that multiple WDFUSBDEVICE objects are not created while WDFUSBDEVICE object(s) that are currently in the device context are leaked.
ms.date: 05/21/2018
keywords: ["UsbDeviceCreateTarget rule (kmdf)"]
topic_type:
- apiref
api_name:
- UsbDeviceCreateTarget
api_type:
- NA
ms.localizationpriority: medium
---

# UsbDeviceCreateTarget rule (kmdf)


The **UsbDeviceCreateTarget** rule specifies that multiple WDFUSBDEVICE objects are not created while WDFUSBDEVICE object(s) that are currently in the device context are leaked.

For example, the [*EvtDevicePrepareHardware*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_prepare_hardware) event callback function can be called multiple times when the system is trying to manage resources and needs to allocate a different chunk of memory for the driver. In this situation, the [*EvtDeviceReleaseHardware*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_release_hardware) event callback function is called to unmap memory resources after the framework has initially called *EvtDevicePrepareHardware*. The *EvtDevicePrepareHardware* is then called again to map resources so that the driver can access memory that is assigned to the device. This rule checks that the driver first verifies that the target WDFUSBDEVICE is **NULL** and does not simply create a new device and replace the previous handle.

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
<td align="left"><p>Run <a href="/windows-hardware/drivers/devtest/static-driver-verifier" data-raw-source="[Static Driver Verifier](./static-driver-verifier.md)">Static Driver Verifier</a> and specify the <strong>UsbDeviceCreateTarget</strong> rule.</p>
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

[**WdfUsbTargetDeviceCreate**](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdevicecreate)
[**WdfUsbTargetDeviceCreateWithParameters**](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdevicecreatewithparameters)
