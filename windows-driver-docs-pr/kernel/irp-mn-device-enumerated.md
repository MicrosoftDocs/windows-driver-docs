---
title: IRP_MN_DEVICE_ENUMERATED
description: The PnP manager uses this I/O request packet (IRP) to notify bus drivers that a device object exists and that it has been fully enumerated by the plug and play manager.
ms.date: 08/12/2017
keywords:
 - IRP_MN_DEVICE_ENUMERATED Kernel-Mode Driver Architecture
ms.localizationpriority: medium
---

# IRP\_MN\_DEVICE\_ENUMERATED


The PnP manager uses this I/O request packet (IRP) to notify bus drivers that a device object exists and that it has been fully enumerated by the plug and play manager.

## Value

0x19

## Major Code

[**IRP\_MJ\_PNP**](irp-mj-pnp.md)

## When Sent

The PnP manager sends this IRP just before user mode is notified with GUID\_DEVICE\_ENUMERATED. This IRP allows drivers to provide a preprocess routine for IRP\_MN\_DEVICE\_ENUMERATED, such as filling in additional device properties. This IRP primarily allows drivers to set device properties for the physical device object (PDO) by using [**IoSetDevicePropertyData**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iosetdevicepropertydata).

## Input Parameters


None

## Output Parameters


None

## I/O Status Block


A driver that handles this IRP sets [Irp-&gt;IoStatus.Status](./i-o-status-blocks.md) to STATUS\_SUCCESS or an appropriate error status.

## Operation

The **IRP\_MN\_DEVICE\_ENUMERATED** IRP is sent to the bus driver's PDO to indicate that the bus driver PDO exists.

## Sending the IRP


Reserved for system use. Drivers must not send this IRP.

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Version</p></td>
<td><p>Available in Windows 7 and later versions of Windows.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Wdm.h</td>
</tr>
</tbody>
</table>

## See also


[Plug and Play Minor IRPs](plug-and-play-minor-irps.md)

 

