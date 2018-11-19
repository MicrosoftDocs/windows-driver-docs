---
title: IRP_MJ_POWER
description: All drivers must be prepared to service IRP_MJ_POWER requests in a DispatchPower routine.
ms.date: 08/12/2017
ms.assetid: ca53ceef-2755-49d3-aab9-0d12a0e51e75
keywords:
 - IRP_MJ_POWER Kernel-Mode Driver Architecture
ms.localizationpriority: medium
---

# IRP\_MJ\_POWER


All drivers must be prepared to service **IRP\_MJ\_POWER** requests in a [*DispatchPower*](https://msdn.microsoft.com/library/windows/hardware/ff543354) routine.

When Sent
---------

The power manager or a driver can send **IRP\_MJ\_POWER** requests at any time the operating system is running.

## Input Parameters


Depends on the value at **MinorFunction** in the current I/O stack location of the IRP. Every **IRP\_MJ\_POWER** request specifies a minor function code that identifies the requested power action.

## Output Parameters


Depends on the value at **MinorFunction** in the current I/O stack location of the IRP.

Operation
---------

In addition to the usual rules that govern the processing of IRPs, **IRP\_MJ\_POWER** IRPs have the following special requirement: A driver that receives a power IRP must not change the major and minor function codes in any I/O stack locations in the IRP that have been set by the power manager or by higher-level drivers. The power manager relies on these function codes remaining unchanged until the IRP is completed. Violations of this rule can cause problems that are difficult to debug. For example, the operating system might stop responding, or "hang."

See [Power Management Minor IRPs](power-management-minor-irps.md) for detailed information about **IRP\_MJ\_POWER** requests.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Header</p></td>
<td>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</td>
</tr>
</tbody>
</table>

## See also


[*DispatchPower*](https://msdn.microsoft.com/library/windows/hardware/ff543354)

 

 




