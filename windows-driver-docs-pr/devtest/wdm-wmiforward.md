---
title: WmiForward rule (wdm)
description: The WmiForward rule specifies that the driver must forward WMI minor IRPs when forwarding is required.
ms.assetid: c62f37d2-ebd5-4705-9590-d1bf17137802
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


The **WmiForward** rule specifies that the driver must forward [**WMI minor IRPs**](https://docs.microsoft.com/windows-hardware/drivers/kernel/wmi-minor-irps) when forwarding is required.

Specifically, when the driver calls [**WmiSystemControl**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wmilib/nf-wmilib-wmisystemcontrol) and the value of the *IrpDisposition* parameter is **IrpForward**, the driver must call [**IoCallDriver**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nf-wdm-iocalldriver) or [**PoCallDriver**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ntifs/nf-ntifs-pocalldriver) to forward the IRP before returning from the dispatch routine.

This rule does not apply to bus drivers.

A *WMI minor IRP* is an [**IRP\_MJ\_SYSTEM\_CONTROL**](https://docs.microsoft.com/windows-hardware/drivers/kernel/irp-mj-system-control) request with a WMI minor function code.

For more information about processing WMI minor IRPs, see [**WMI Requirements for WDM Drivers**](https://docs.microsoft.com/windows-hardware/drivers/kernel/wmi-requirements-for-wdm-drivers), [**Handling WMI Requests**](https://docs.microsoft.com/windows-hardware/drivers/kernel/handling-wmi-requests), [**Windows Management Instrumentation Routines**](https://docs.microsoft.com/windows-hardware/drivers/ddi/index), and [**WMI Library Support Routines**](https://docs.microsoft.com/windows-hardware/drivers/ddi/index).

**Driver model: WDM**

How to test
-----------

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
<td align="left"><p>Run <a href="https://docs.microsoft.com/windows-hardware/drivers/devtest/static-driver-verifier" data-raw-source="[Static Driver Verifier](https://docs.microsoft.com/windows-hardware/drivers/devtest/static-driver-verifier)">Static Driver Verifier</a> and specify the <strong>WmiForward</strong> rule.</p>
Use the following steps to run an analysis of your code:
<ol>
<li><a href="https://docs.microsoft.com/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers#preparing-your-source-code" data-raw-source="[Prepare your code (use role type declarations).](https://docs.microsoft.com/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers#preparing-your-source-code)">Prepare your code (use role type declarations).</a></li>
<li><a href="https://docs.microsoft.com/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers#running-static-driver-verifier" data-raw-source="[Run Static Driver Verifier.](https://docs.microsoft.com/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers#running-static-driver-verifier)">Run Static Driver Verifier.</a></li>
<li><a href="https://docs.microsoft.com/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers#viewing-and-analyzing-the-results" data-raw-source="[View and analyze the results.](https://docs.microsoft.com/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers#viewing-and-analyzing-the-results)">View and analyze the results.</a></li>
</ol>
<p>For more information, see <a href="https://docs.microsoft.com/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers" data-raw-source="[Using Static Driver Verifier to Find Defects in Drivers](https://docs.microsoft.com/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers)">Using Static Driver Verifier to Find Defects in Drivers</a>.</p></td>
</tr>
</tbody>
</table>

Applies to
----------

[**IoAcquireRemoveLock**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nf-wdm-ioacquireremovelock)
[**IoCallDriver**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nf-wdm-iocalldriver)
[**PoCallDriver**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ntifs/nf-ntifs-pocalldriver)
See also
--------

[**WMI Requirements for WDM Drivers**](https://docs.microsoft.com/windows-hardware/drivers/kernel/wmi-requirements-for-wdm-drivers)
[**Handling WMI Requests**](https://docs.microsoft.com/windows-hardware/drivers/kernel/handling-wmi-requests)
[**WMI Library Support Routines**](https://docs.microsoft.com/windows-hardware/drivers/ddi/index)
 

 





