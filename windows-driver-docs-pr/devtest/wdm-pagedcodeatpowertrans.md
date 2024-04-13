---
title: PagedCodeAtPowerTrans Rule (WDM)
description: The PagedCodeAtPowerTrans rule specifies that a driver should not call PAGED\_CODE while responding to a system IRP\_MJ\_POWER Irp (IRP\_MN\_SET\_POWER) and to a device IRP\_MJ\_POWER Irp (IRP\_MN\_SET\_POWER).
ms.date: 05/21/2018
keywords: ["PagedCodeAtPowerTrans rule (wdm)"]
topic_type:
- apiref
ms.topic: reference
api_name:
- PagedCodeAtPowerTrans
api_type:
- NA
---

# PagedCodeAtPowerTrans rule (wdm)


The **PagedCodeAtPowerTrans** rule specifies that a driver should not call [**PAGED_CODE**](../kernel/paged_code.md) while responding to a system IRP\_MJ\_POWER Irp (IRP\_MN\_SET\_POWER) and to a device IRP\_MJ\_POWER Irp (IRP\_MN\_SET\_POWER).

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
<td align="left"><p>Run <a href="/windows-hardware/drivers/devtest/static-driver-verifier" data-raw-source="[Static Driver Verifier](./static-driver-verifier.md)">Static Driver Verifier</a> and specify the <strong>PagedCodeAtPowerTrans</strong> rule.</p>
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

[**PAGED_CODE**](../kernel/paged_code.md)
