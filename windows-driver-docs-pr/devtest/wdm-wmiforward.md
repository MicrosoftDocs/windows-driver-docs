---
title: WmiForward rule (wdm)
description: The WmiForward rule specifies that the driver must forward WMI minor IRPs when forwarding is required.
ms.date: 05/21/2018
keywords: ["WmiForward rule (wdm)"]
topic_type:
- apiref
api_name:
- WmiForward
api_type:
- NA
ms.localizationpriority: medium
---

# WmiForward rule (wdm)


The **WmiForward** rule specifies that the driver must forward [**WMI minor IRPs**](../kernel/wmi-minor-irps.md) when forwarding is required.

Specifically, when the driver calls [**WmiSystemControl**](/windows-hardware/drivers/ddi/wmilib/nf-wmilib-wmisystemcontrol) and the value of the *IrpDisposition* parameter is **IrpForward**, the driver must call [**IoCallDriver**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocalldriver) or [**PoCallDriver**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-pocalldriver) to forward the IRP before returning from the dispatch routine.

This rule does not apply to bus drivers.

A *WMI minor IRP* is an [**IRP\_MJ\_SYSTEM\_CONTROL**](../kernel/irp-mj-system-control.md) request with a WMI minor function code.

For more information about processing WMI minor IRPs, see [**WMI Requirements for WDM Drivers**](../kernel/wmi-requirements-for-wdm-drivers.md), [**Handling WMI Requests**](../kernel/handling-wmi-requests.md), [**Windows Management Instrumentation Routines**](/windows-hardware/drivers/ddi/index), and [**WMI Library Support Routines**](/windows-hardware/drivers/ddi/index).

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
<td align="left"><p>Run <a href="/windows-hardware/drivers/devtest/static-driver-verifier" data-raw-source="[Static Driver Verifier](./static-driver-verifier.md)">Static Driver Verifier</a> and specify the <strong>WmiForward</strong> rule.</p>
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

[**IoAcquireRemoveLock**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioacquireremovelock)
[**IoCallDriver**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocalldriver)
[**PoCallDriver**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-pocalldriver)
## See also

[**WMI Requirements for WDM Drivers**](../kernel/wmi-requirements-for-wdm-drivers.md)
[**Handling WMI Requests**](../kernel/handling-wmi-requests.md)
[**WMI Library Support Routines**](/windows-hardware/drivers/ddi/index)
