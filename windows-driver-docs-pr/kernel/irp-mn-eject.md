---
title: IRP_MN_EJECT
description: Bus drivers typically handle this request for their child devices (child PDOs) that support device ejection. Function and filter drivers do not receive this request.
ms.date: 08/12/2017
keywords:
 - IRP_MN_EJECT Kernel-Mode Driver Architecture
ms.localizationpriority: medium
---

# IRP\_MN\_EJECT


Bus drivers typically handle this request for their child devices (child PDOs) that support device ejection. Function and filter drivers do not receive this request.

## Value

0x11

## Major Code

[**IRP\_MJ\_PNP**](irp-mj-pnp.md)

## When Sent

The PnP manager sends this IRP to direct the appropriate driver or drivers to eject the device from its slot.

The PnP manager sends this IRP at IRQL PASSIVE\_LEVEL in an arbitrary thread context.

## Input Parameters


None

## Output Parameters


None

## I/O Status Block


A bus driver sets **Irp-&gt;IoStatus.Status** to STATUS\_SUCCESS or to an appropriate error status.

On success, a bus driver sets **Irp-&gt;IoStatus.Information** to zero.

If a bus driver does not handle this IRP, it leaves **Irp-&gt;IoStatus.Status** as is and completes the IRP.

## Operation

For the device to be ejected, the device must be in the D3 device power state (off) and must be unlocked (if the device supports locking).

Any driver that returns success for this IRP must wait until the device has been ejected before completing the IRP.

See [Plug and Play](./introduction-to-plug-and-play.md) for the general rules for handling [Plug and Play minor IRPs](plug-and-play-minor-irps.md).

**Sending This IRP**

Reserved for system use. Drivers must not send this IRP.

Instead, see the reference page for the [**IoRequestDeviceEject**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iorequestdeviceeject) routine.

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


[**IoRequestDeviceEject**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iorequestdeviceeject)

 

