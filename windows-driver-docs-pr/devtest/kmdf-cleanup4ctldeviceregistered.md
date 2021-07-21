---
title: Cleanup4CtlDeviceRegistered rule (kmdf)
description: The Cleanup4CtlDeviceRegistered rule specifies that if a Plug and Play (PnP) driver calls WdfDeviceCreate for the control device object, the driver must register one of the required event callback functions.
ms.date: 05/21/2018
keywords: ["Cleanup4CtlDeviceRegistered rule (kmdf)"]
topic_type:
- apiref
api_name:
- Cleanup4CtlDeviceRegistered
api_type:
- NA
ms.localizationpriority: medium
---

# Cleanup4CtlDeviceRegistered rule (kmdf)


The **Cleanup4CtlDeviceRegistered** rule specifies that if a Plug and Play (PnP) driver calls [**WdfDeviceCreate**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicecreate) for the control device object, the driver must register one of the required event callback functions.

The event callback function can be one of the following:

[*EvtCleanupCallback*](/windows-hardware/drivers/ddi/wdfobject/nc-wdfobject-evt_wdf_object_context_cleanup) or [*EvtDestroyCallback*](/windows-hardware/drivers/ddi/wdfobject/nc-wdfobject-evt_wdf_object_context_destroy) in the [**WDF\_OBJECT\_ATTRIBUTES**](/windows-hardware/drivers/ddi/wdfobject/ns-wdfobject-_wdf_object_attributes) structure for the control device
-or-
[*EvtDeviceSelfManagedIoCleanup*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_self_managed_io_cleanup) in the [**WDF\_PNPPOWER\_EVENT\_CALLBACKS**](/windows-hardware/drivers/ddi/wdfdevice/ns-wdfdevice-_wdf_pnppower_event_callbacks) structure

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
<td align="left"><p>Run <a href="/windows-hardware/drivers/devtest/static-driver-verifier" data-raw-source="[Static Driver Verifier](./static-driver-verifier.md)">Static Driver Verifier</a> and specify the <strong>Cleanup4CtlDeviceRegistered</strong> rule.</p>
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
