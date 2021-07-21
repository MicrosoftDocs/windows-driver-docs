---
title: PnpSameDeviceObject rule (wdm)
description: The PnpSameDeviceObject rule specifies that the driver calls IoAttachDeviceToDeviceStack with a pointer to a valid target device object.
ms.date: 05/21/2018
keywords: ["PnpSameDeviceObject rule (wdm)"]
topic_type:
- apiref
api_name:
- PnpSameDeviceObject
api_type:
- NA
ms.localizationpriority: medium
---

# PnpSameDeviceObject rule (wdm)


The **PnpSameDeviceObject** rule specifies that the driver calls [**IoAttachDeviceToDeviceStack**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioattachdevicetodevicestack) with a pointer to a valid target device object.

If the pointed-to device object is not standard, the driver violates this rule. This rule ensures that the driver correctly attaches to the device stack.

This rule does not verify the validity of the pointer to the source object.

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
<td align="left"><p>Run <a href="/windows-hardware/drivers/devtest/static-driver-verifier" data-raw-source="[Static Driver Verifier](./static-driver-verifier.md)">Static Driver Verifier</a> and specify the <strong>PnpSameDeviceObject</strong> rule.</p>
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

[**IoAttachDeviceToDeviceStack**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioattachdevicetodevicestack)
