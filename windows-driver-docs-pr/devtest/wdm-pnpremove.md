---
title: PnpRemove rule (wdm)
description: The PnpRemove rule specifies that the driver cannot complete IRP\_MN\_SURPRISE\_REMOVAL, IRP\_MN\_CANCEL\_REMOVE\_DEVICE, IRP\_MN\_CANCEL\_STOP\_DEVICE, or IRP\_MN\_REMOVE\_DEVICE requests with a failure.
ms.assetid: 2713F943-36A2-41B9-B9C0-86FC06B22443
ms.author: windowsdriverdev
ms.date: 5/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["PnpRemove rule (wdm)"]
topic_type:
- apiref
api_name:
- PnpRemove
api_type:
- NA
---

# PnpRemove rule (wdm)


The **PnpRemove** rule specifies that the driver cannot complete IRP\_MN\_SURPRISE\_REMOVAL, IRP\_MN\_CANCEL\_REMOVE\_DEVICE, IRP\_MN\_CANCEL\_STOP\_DEVICE, or IRP\_MN\_REMOVE\_DEVICE requests with a failure.

> [!NOTE]
> In Windows 8.1, you can test the **PnpRemove** rule using [Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff545448). The rule is not currently available for use with [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808).

 

|              |     |
|--------------|-----|
| Driver model | WDM |

|                                   |                                                                                                                                       |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Bug check(s) found with this rule | [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](https://msdn.microsoft.com/library/windows/hardware/ff560187) (0x00043006) |

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
<td align="left"><p>Run [Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff545448) and select the [DDI compliance checking](https://msdn.microsoft.com/library/windows/hardware/hh454208) option.</p></td>
</tr>
</tbody>
</table>

 

 

 





