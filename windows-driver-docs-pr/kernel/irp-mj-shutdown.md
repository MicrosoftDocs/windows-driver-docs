---
title: IRP_MJ_SHUTDOWN
description: Drivers of mass-storage devices that have internal caches for data must handle this request in a DispatchShutdown routine.
ms.date: 08/12/2017
keywords:
 - IRP_MJ_SHUTDOWN Kernel-Mode Driver Architecture
ms.localizationpriority: medium
---

# IRP\_MJ\_SHUTDOWN


Drivers of mass-storage devices that have internal caches for data must handle this request in a [*DispatchShutdown*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch) routine. Drivers of mass-storage devices and intermediate drivers layered over them also must handle this request if an underlying driver maintains internal buffers for data.

## When Sent

Receipt of a shutdown request indicates that a file system driver is sending notice that the system is being shut down.

One or more file system drivers can send such a lower-level driver more than one shutdown request when a user logs off or when the system is being shut down for some other reason.

The PnP manager sends this IRP at IRQL<=APC_LEVEL in an arbitrary thread context.

## Input Parameters


None

## Output Parameters


None

## Operation

The driver must complete the transfer of any data currently cached in the device or held in the driver's internal buffers before completing the shutdown request.

A driver does not receive an **IRP\_MJ\_SHUTDOWN** request for a device object unless it registers to do so with either [**IoRegisterShutdownNotification**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioregistershutdownnotification) or [**IoRegisterLastChanceShutdownNotification**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioregisterlastchanceshutdownnotification).

## Requirements

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


[*DispatchShutdown*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch)

[**IoRegisterLastChanceShutdownNotification**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioregisterlastchanceshutdownnotification)

[**IoRegisterShutdownNotification**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioregistershutdownnotification)

 

