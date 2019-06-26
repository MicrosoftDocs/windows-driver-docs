---
title: PnpRemove rule (wdm)
description: The PnpRemove rule specifies that the driver cannot complete IRP\_MN\_SURPRISE\_REMOVAL, IRP\_MN\_CANCEL\_REMOVE\_DEVICE, IRP\_MN\_CANCEL\_STOP\_DEVICE, or IRP\_MN\_REMOVE\_DEVICE requests with a failure.
ms.assetid: 2713F943-36A2-41B9-B9C0-86FC06B22443
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
> In Windows 8.1, you can test the **PnpRemove** rule using [Driver Verifier](https://docs.microsoft.com/windows-hardware/drivers/devtest/driver-verifier). The rule is not currently available for use with [Static Driver Verifier](https://docs.microsoft.com/windows-hardware/drivers/devtest/static-driver-verifier).

 

|              |     |
|--------------|-----|
| Driver model | WDM |

|                                   |                                                                                                                                       |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Bug check(s) found with this rule | [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](https://docs.microsoft.com/windows-hardware/drivers/debugger/bug-check-0xc4--driver-verifier-detected-violation) (0x00043006) |

How to test
-----------

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
<td align="left"><p>Run <a href="https://docs.microsoft.com/windows-hardware/drivers/devtest/driver-verifier" data-raw-source="[Driver Verifier](https://docs.microsoft.com/windows-hardware/drivers/devtest/driver-verifier)">Driver Verifier</a> and select the <a href="https://docs.microsoft.com/windows-hardware/drivers/devtest/ddi-compliance-checking" data-raw-source="[DDI compliance checking](https://docs.microsoft.com/windows-hardware/drivers/devtest/ddi-compliance-checking)">DDI compliance checking</a> option.</p></td>
</tr>
</tbody>
</table>

 

 

 





