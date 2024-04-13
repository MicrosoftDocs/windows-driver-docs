---
title: InitFreeDeviceCreateType4 Rule (KMDF)
description: The InitFreeDeviceCreateType4 rule specifies that a driver must call WdfDeviceInitFree if the driver encounters an error while it calls WdfDeviceCreate and if the driver received the WDFDEVICE\_INIT structure from a call to WdfControlDeviceInitAllocate.
ms.date: 05/21/2018
keywords: ["InitFreeDeviceCreateType4 rule (kmdf)"]
topic_type:
- apiref
ms.topic: reference
api_name:
- InitFreeDeviceCreateType4
api_type:
- NA
---

# InitFreeDeviceCreateType4 rule (kmdf)


The **InitFreeDeviceCreateType4** rule specifies that a driver must call [**WdfDeviceInitFree**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceinitfree) if the driver encounters an error while it calls [**WdfDeviceCreate**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicecreate) and if the driver received the [**WDFDEVICE\_INIT**](../wdf/wdfdevice_init.md) structure from a call to [**WdfControlDeviceInitAllocate**](/windows-hardware/drivers/ddi/wdfcontrol/nf-wdfcontrol-wdfcontroldeviceinitallocate).

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
<td align="left"><p>Run <a href="/windows-hardware/drivers/devtest/static-driver-verifier" data-raw-source="[Static Driver Verifier](./static-driver-verifier.md)">Static Driver Verifier</a> and specify the <strong>InitFreeDeviceCreateType4</strong> rule.</p>
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

[**WdfControlDeviceInitAllocate**](/windows-hardware/drivers/ddi/wdfcontrol/nf-wdfcontrol-wdfcontroldeviceinitallocate)
[**WdfDeviceCreate**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicecreate)
[**WdfDeviceInitFree**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceinitfree)
## See also

[**InitFreeDeviceCallback**](kmdf-initfreedevicecallback.md)
[**InitFreeDeviceCreate**](kmdf-initfreedevicecreate.md)
[**InitFreeDeviceCreateType2**](kmdf-initfreedevicecreatetype2.md)
[**PdoInitFreeDeviceCreateType2**](kmdf-pdoinitfreedevicecreatetype2.md)
[**PdoInitFreeDeviceCallback**](kmdf-pdoinitfreedevicecallback.md)
[**PdoInitFreeDeviceCreate**](kmdf-pdoinitfreedevicecreate.md)
[**PdoInitFreeDeviceCreateType4**](kmdf-pdoinitfreedevicecreatetype4.md)
[**InitFreeNull**](kmdf-initfreenull.md)
