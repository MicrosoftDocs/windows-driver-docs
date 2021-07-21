---
title: ForwardedAtBadIrqlFsdSync rule
description: The ForwardedAtBadIrqlFsdSync rule specifies that the driver call IoCallDriver and PoCallDriver at IRQL DISPATCH\_LEVEL, unless the IRP major function code being forwarded is one of the following IRP\_MJ\_POWERIRP\_MJ\_READIRP\_MJ\_WRITEIRP\_MJ\_DEVICE\_CONTROLIRP\_MJ\_INTERNAL\_DEVICE\_CONTROL.
ms.date: 05/21/2018
keywords: ["ForwardedAtBadIrqlFsdSync rule"]
topic_type:
- apiref
api_name:
- ForwardedAtBadIrqlFsdSync
api_type:
- NA
ms.localizationpriority: medium
---

# ForwardedAtBadIrqlFsdSync rule


The **ForwardedAtBadIrqlFsdSync** rule specifies that the driver call [**IoCallDriver**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocalldriver) and [**PoCallDriver**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-pocalldriver) at IRQL&lt;DISPATCH\_LEVEL, unless the IRP major function code being forwarded is one of the following:

-   [**IRP\_MJ\_POWER**](../kernel/irp-mj-power.md)
-   [**IRP\_MJ\_READ**](../kernel/irp-mj-read.md)
-   [**IRP\_MJ\_WRITE**](../kernel/irp-mj-write.md)
-   [**IRP\_MJ\_DEVICE\_CONTROL**](../kernel/irp-mj-device-control.md)
-   [**IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL**](../kernel/irp-mj-internal-device-control.md)

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
<td align="left"><p>Run <a href="/windows-hardware/drivers/devtest/static-driver-verifier" data-raw-source="[Static Driver Verifier](./static-driver-verifier.md)">Static Driver Verifier</a> and specify the <strong>ForwardedAtBadIrqlFsdSync</strong> rule.</p>
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

[**IoBuildSynchronousFsdRequest**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iobuildsynchronousfsdrequest)
[**IoCallDriver**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocalldriver)
[**PoCallDriver**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-pocalldriver)
