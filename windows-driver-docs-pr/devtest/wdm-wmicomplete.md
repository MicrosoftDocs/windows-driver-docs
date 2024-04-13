---
title: WmiComplete Rule (WDM)
description: The WmiComplete rule specifies that when processing a WMI minor IRP, the driver calls IoCompleteRequest before returning from the DispatchSystemControl routine.
ms.date: 05/21/2018
keywords: ["WmiComplete rule (wdm)"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WmiComplete
api_type:
- NA
---

# WmiComplete rule (wdm)


The **WmiComplete** rule specifies that when processing a [**WMI minor IRP**](../kernel/wmi-minor-irps.md), the driver calls [**IoCompleteRequest**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocompleterequest) before returning from the [**DispatchSystemControl**](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch) routine.

A *WMI minor IRP* is an [**IRP\_MJ\_SYSTEM\_CONTROL**](../kernel/irp-mj-system-control.md) request with a WMI minor function code.

For more information about processing WMI minor IRPs, see [**WMI Requirements for WDM Drivers**](../kernel/wmi-requirements-for-wdm-drivers.md), [**Handling WMI Requests**](../kernel/handling-wmi-requests.md), [**Windows Management Instrumentation Routines**](../kernel/windows-kernel-mode-wmi-library.md), and [**WMI Library Support Routines**](../kernel/windows-kernel-mode-wmi-library.md).

Drivers that are not registered as WMI data providers must forward the WMI request to the next lower driver. To verify this action, use the [**WmiForward**](wdm-wmiforward.md) rule.

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
<td align="left"><p>Run <a href="/windows-hardware/drivers/devtest/static-driver-verifier" data-raw-source="[Static Driver Verifier](./static-driver-verifier.md)">Static Driver Verifier</a> and specify the <strong>WmiComplete</strong> rule.</p>
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

[**IoCompleteRequest**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocompleterequest)
[**WmiSystemControl**](/windows-hardware/drivers/ddi/wmilib/nf-wmilib-wmisystemcontrol)
## See also

[**WmiForward**](wdm-wmiforward.md)
[**WMI Requirements for WDM Drivers**](../kernel/wmi-requirements-for-wdm-drivers.md)
[**Handling WMI Requests**](../kernel/handling-wmi-requests.md)
[**WMI Library Support Routines**](/windows-hardware/drivers/ddi/index)
