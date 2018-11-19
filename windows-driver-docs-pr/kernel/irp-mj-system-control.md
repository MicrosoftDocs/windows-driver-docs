---
title: IRP_MJ_SYSTEM_CONTROL
description: All drivers must provide a DispatchSystemControl routine that handles IRP_MJ_SYSTEM_CONTROL requests, which are sent by the kernel-mode component of Windows Management Instrumentation (WMI).
ms.date: 08/12/2017
ms.assetid: 1b4dfc87-3f74-4e33-9dbb-72d4f72480fc
keywords:
 - IRP_MJ_SYSTEM_CONTROL Kernel-Mode Driver Architecture
ms.localizationpriority: medium
---

# IRP\_MJ\_SYSTEM\_CONTROL


All drivers must provide a [*DispatchSystemControl*](https://msdn.microsoft.com/library/windows/hardware/ff543412) routine that handles **IRP\_MJ\_SYSTEM\_CONTROL** requests, which are sent by the kernel-mode component of [Windows Management Instrumentation](https://msdn.microsoft.com/library/windows/hardware/ff547139) (WMI).

When Sent
---------

The WMI kernel-mode component can send an **IRP\_MJ\_SYSTEM\_CONTROL** request any time following a driver's successful registration as a supplier of WMI data. WMI IRPs typically are sent when a user-mode data consumer has requested WMI data.

## Input Parameters


Depends on the value at **MinorFunction** in the current I/O stack location of the IRP. Every **IRP\_MJ\_SYSTEM\_CONTROL** request specifies a minor function code that identifies the requested WMI action.

## Output Parameters


Depends on the value at **MinorFunction** in the current I/O stack location of the IRP.

Operation
---------

All drivers must support **IRP\_MJ\_SYSTEM\_CONTROL** requests by supplying a [*DispatchSystemControl*](https://msdn.microsoft.com/library/windows/hardware/ff543412) routine.

Drivers that support [Windows Management Instrumentation](https://msdn.microsoft.com/library/windows/hardware/ff547139) (WMI) must handle **IRP\_MJ\_SYSTEM\_CONTROL** requests by processing the minor function codes associated with this major function code. For information about the WMI minor function codes, see [WMI Minor IRPs](wmi-minor-irps.md).

Drivers that do not support WMI by [registering as a WMI data provider](https://msdn.microsoft.com/library/windows/hardware/ff560870) must pass **IRP\_MJ\_SYSTEM\_CONTROL** requests to the next lower driver.

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


[*DispatchSystemControl*](https://msdn.microsoft.com/library/windows/hardware/ff543412)

 

 




