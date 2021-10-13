---
title: IRP_MN_CANCEL_REMOVE_DEVICE
description: Learn about the 'IRP_MN_CANCEL_REMOVE_DEVICE' kernel-mode driver architecture. All PnP drivers must handle this IRP.
ms.date: 08/12/2017
keywords:
 - IRP_MN_CANCEL_REMOVE_DEVICE Kernel-Mode Driver Architecture
ms.localizationpriority: medium
---

# IRP\_MN\_CANCEL\_REMOVE\_DEVICE


All PnP drivers must handle this IRP.

## Value

0x03

## Major Code

[**IRP\_MJ\_PNP**](irp-mj-pnp.md)

## When Sent

The PnP manager sends this IRP to inform the drivers for a device that the device will not be removed.

The PnP manager sends this IRP at IRQL PASSIVE\_LEVEL in the context of a system thread.

## Input Parameters


None

## Output Parameters


None

## I/O Status Block


A driver must set **Irp-&gt;IoStatus.Status** to STATUS\_SUCCESS for this IRP. If a driver fails this IRP, the device is left in an inconsistent state.

## Operation

This IRP must be handled first by the parent bus driver for a device and then by each higher driver in the device stack.

In response to this IRP, drivers return the device to the state it was in prior to receiving the **IRP\_MN\_QUERY\_REMOVE\_DEVICE** request.

If the device is already started when the driver receives this IRP, the driver simply sets status to success and passes the IRP to the next driver (or completes the IRP if the driver is a bus driver). For such a cancel-remove IRP, a function or filter driver need not set a completion routine. The device may not be in the remove-pending state, because, for example, the driver failed the previous **IRP\_MN\_QUERY\_REMOVE\_DEVICE**.

The PnP manager calls any **EventCategoryTargetDeviceChange** notification callbacks with GUID\_TARGET\_DEVICE\_REMOVE\_CANCELLED after the **IRP\_MN\_CANCEL\_REMOVE\_DEVICE** request completes. Such callbacks were registered on the device by calling [**IoRegisterPlugPlayNotification**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioregisterplugplaynotification). The PnP manager also calls any user-mode components that registered for notification on the device by calling **RegisterDeviceNotification**.

If a file system is mounted on the device, it must undo any operations it did in response to the query-remove notification.

See [Plug and Play](./introduction-to-plug-and-play.md) for detailed information about handling remove IRPs and for the general rules for handling all [Plug and Play minor IRPs](plug-and-play-minor-irps.md).

**Sending This IRP**

Reserved for system use. Drivers must not send this IRP.

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


[**IoRegisterPlugPlayNotification**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioregisterplugplaynotification)

[**IRP\_MN\_QUERY\_REMOVE\_DEVICE**](irp-mn-query-remove-device.md)

 

