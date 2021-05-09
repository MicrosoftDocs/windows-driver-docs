---
title: PnpRemove rule (wdm)
description: The PnpRemove rule specifies that the driver cannot complete IRP\_MN\_SURPRISE\_REMOVAL, IRP\_MN\_CANCEL\_REMOVE\_DEVICE, IRP\_MN\_CANCEL\_STOP\_DEVICE, or IRP\_MN\_REMOVE\_DEVICE requests with a failure.
ms.date: 05/21/2018
keywords: ["PnpRemove rule (wdm)"]
topic_type:
- apiref
api_name:
- PnpRemove
api_type:
- NA
ms.localizationpriority: medium
---

# PnpRemove rule (wdm)


The **PnpRemove** rule specifies that the driver cannot complete IRP\_MN\_SURPRISE\_REMOVAL, IRP\_MN\_CANCEL\_REMOVE\_DEVICE, IRP\_MN\_CANCEL\_STOP\_DEVICE, or IRP\_MN\_REMOVE\_DEVICE requests with a failure.

> [!NOTE]
> In Windows 8.1, you can test the **PnpRemove** rule using [Driver Verifier](./driver-verifier.md). The rule is not currently available for use with [Static Driver Verifier](./static-driver-verifier.md).

 

**Driver model: WDM**

**Bug check(s) found with this rule**: [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](../debugger/bug-check-0xc4--driver-verifier-detected-violation.md) (0x00043006)


## How to test

<table>
<colgroup>
<col width="100%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">At run time</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Run <a href="/windows-hardware/drivers/devtest/driver-verifier" data-raw-source="[Driver Verifier](./driver-verifier.md)">Driver Verifier</a> and select the <a href="/windows-hardware/drivers/devtest/ddi-compliance-checking" data-raw-source="[DDI compliance checking](./ddi-compliance-checking.md)">DDI compliance checking</a> option.</p></td>
</tr>
</tbody>
</table>

 

