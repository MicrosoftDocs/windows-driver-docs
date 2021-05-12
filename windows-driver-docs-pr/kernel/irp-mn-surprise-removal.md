---
title: IRP_MN_SURPRISE_REMOVAL
description: All PnP drivers must handle this IRP.
ms.date: 08/12/2017
keywords:
 - IRP_MN_SURPRISE_REMOVAL Kernel-Mode Driver Architecture
ms.localizationpriority: medium
---

# IRP\_MN\_SURPRISE\_REMOVAL


All PnP drivers must handle this IRP.

## Value

0x17

## Major Code

[**IRP\_MJ\_PNP**](irp-mj-pnp.md)

## When Sent

The PnP manager sends this IRP to notify the drivers for a device that the device is no longer available for I/O operations. This IRP is sent on Windows 2000 and later systems only.

The PnP manager sends this IRP before notifying user-mode applications or other kernel-mode components. After this IRP completes, the PnP manager notifies registered applications and drivers that the device has been removed.

The device can be in any PnP state when the PnP manager sends this IRP.

On Windows 98/Windows Me, the PnP manager does not send this IRP.

The PnP manager sends this IRP at IRQL = PASSIVE\_LEVEL in the context of a system thread.

## Input Parameters


None

## Output Parameters


None

## I/O Status Block


A driver must set **Irp-&gt;IoStatus.Status** to STATUS\_SUCCESS. A driver must not fail this IRP.

## Operation

This IRP is handled first by the driver at the top of the device stack and then passed down to each lower driver in the stack.

For more information about this IRP, see [Handling an IRP\_MN\_SURPRISE\_REMOVAL Request](./handling-an-irp-mn-surprise-removal-request.md). For additional information about supporting device removal, see [Removing a Device](./removing-a-device-in-a-function-driver.md).

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


[**IRP\_MN\_REMOVE\_DEVICE**](irp-mn-remove-device.md)

