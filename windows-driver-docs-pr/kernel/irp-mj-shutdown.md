---
title: IRP_MJ_SHUTDOWN
description: Drivers of mass-storage devices that have internal caches for data must handle this request in a DispatchShutdown routine.
ms.date: 08/12/2017
ms.assetid: af0b01b5-5f81-42da-aa4b-433bd422a51f
keywords:
 - IRP_MJ_SHUTDOWN Kernel-Mode Driver Architecture
ms.localizationpriority: medium
---

# IRP\_MJ\_SHUTDOWN


Drivers of mass-storage devices that have internal caches for data must handle this request in a [*DispatchShutdown*](https://msdn.microsoft.com/library/windows/hardware/ff543405) routine. Drivers of mass-storage devices and intermediate drivers layered over them also must handle this request if an underlying driver maintains internal buffers for data.

When Sent
---------

Receipt of a shutdown request indicates that a file system driver is sending notice that the system is being shut down.

One or more file system drivers can send such a lower-level driver more than one shutdown request when a user logs off or when the system is being shut down for some other reason.

## Input Parameters


None

## Output Parameters


None

Operation
---------

The driver must complete the transfer of any data currently cached in the device or held in the driver's internal buffers before completing the shutdown request.

A driver does not receive an **IRP\_MJ\_SHUTDOWN** request for a device object unless it registers to do so with either [**IoRegisterShutdownNotification**](https://msdn.microsoft.com/library/windows/hardware/ff549541) or [**IoRegisterLastChanceShutdownNotification**](https://msdn.microsoft.com/library/windows/hardware/ff549518).

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


[*DispatchShutdown*](https://msdn.microsoft.com/library/windows/hardware/ff543405)

[**IoRegisterLastChanceShutdownNotification**](https://msdn.microsoft.com/library/windows/hardware/ff549518)

[**IoRegisterShutdownNotification**](https://msdn.microsoft.com/library/windows/hardware/ff549541)

 

 




