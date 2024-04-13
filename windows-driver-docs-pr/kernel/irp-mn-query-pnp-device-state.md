---
title: IRP_MN_QUERY_PNP_DEVICE_STATE
description: Function, filter, and bus drivers can handle this request.
ms.date: 08/12/2017
ms.topic: reference
keywords:
 - IRP_MN_QUERY_PNP_DEVICE_STATE Kernel-Mode Driver Architecture
---

# IRP\_MN\_QUERY\_PNP\_DEVICE\_STATE


Function, filter, and bus drivers can handle this request.

## Value47

0x14

## Major Code

[**IRP\_MJ\_PNP**](irp-mj-pnp.md)

## When Sent

The PnP manager sends this IRP after the drivers for a device return success from the [**IRP\_MN\_START\_DEVICE**](irp-mn-start-device.md) request sent when a device is first started. This IRP is not sent on a start after a stop for resource rebalancing. The PnP manager also sends this IRP when a driver for the device calls [**IoInvalidateDeviceState**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioinvalidatedevicestate).

The PnP manager sends this IRP at IRQL PASSIVE\_LEVEL in the context of an arbitrary thread.

## Input Parameters


None

## Output Parameters


Returned in I/O status block.

## I/O Status Block


A driver sets **Irp-&gt;IoStatus.Status** to STATUS\_SUCCESS or to an appropriate error status such as STATUS\_UNSUCCESSFUL.

On success, a driver sets **Irp-&gt;IoStatus.Information** to a [**PNP\_DEVICE\_STATE**](./handling-an-irp-mn-surprise-removal-request.md#about-pnp_device_state) bitmask.


If a function or filter driver does not handle this IRP, it calls [**IoSkipCurrentIrpStackLocation**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioskipcurrentirpstacklocation), does not set an [*IoCompletion*](/windows-hardware/drivers/ddi/wdm/nc-wdm-io_completion_routine) routine, and passes the IRP down to the next driver. Such a driver must not modify **Irp-&gt;IoStatus** and must not complete the IRP.

If a bus driver does not handle this IRP, it leaves **Irp-&gt;IoStatus.Status** as is and completes the IRP.

## Operation

This IRP is handled first by the driver at the top of the device stack and then by each next lower driver in the stack.

A driver handles this IRP if it has information about the PnP state of a device. A driver can set or clear the flags in the PNP\_DEVICE\_STATE bitmask. If another driver has set a PNP\_DEVICE\_STATE in **Irp-&gt;IoStatus.Information**, a driver must take care to modify the flags in that bitmask rather than overwrite the whole structure.

See [Plug and Play](./introduction-to-plug-and-play.md) for the general rules for handling [Plug and Play minor IRPs](plug-and-play-minor-irps.md).

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


[**IoInvalidateDeviceState**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioinvalidatedevicestate)

[**PNP\_DEVICE\_STATE**](./handling-an-irp-mn-surprise-removal-request.md#about-pnp_device_state)
