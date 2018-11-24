---
title: IRP_MN_QUERY_STOP_DEVICE
description: All PnP drivers must handle this IRP.
ms.date: 08/12/2017
ms.assetid: 22f58964-23a0-4307-a748-9c1620e30871
keywords:
 - IRP_MN_QUERY_STOP_DEVICE Kernel-Mode Driver Architecture
ms.localizationpriority: medium
---

# IRP\_MN\_QUERY\_STOP\_DEVICE


All PnP drivers must handle this IRP.

Major Code
----------

[**IRP\_MJ\_PNP**](irp-mj-pnp.md)
When Sent
---------

The PnP manager sends this IRP to query whether a device can be stopped to rebalance resources.

On Windows 98/Me, the PnP manager also sends this IRP when a device is being disabled.

The PnP manager sends this IRP at IRQL PASSIVE\_LEVEL in the context of a system thread.

## Input Parameters


None

## Output Parameters


None

## I/O Status Block


A driver sets **Irp-&gt;IoStatus.Status** to STATUS\_SUCCESS or to an appropriate error status. If a driver cannot stop the device, the driver sets **Irp-&gt;IoStatus.Status** to STATUS\_UNSUCCESSFUL.

A bus driver can set **Irp-&gt;IoStatus.Status** to STATUS\_RESOURCE\_REQUIREMENTS\_CHANGED to indicate success for the IRP but also to request that the PnP manager requery the resource requirements for the device before sending the stop IRP.

Operation
---------

This IRP is handled first by the driver at the top of the device stack and then passed down to each lower driver in the stack.

In response to this IRP, Windows 2000 and later drivers indicate whether it is safe to stop the device for resource rebalancing.

On Windows 98/Me, this IRP is sent not only during resource rebalancing, but also when a device is being disabled. Because a driver cannot distinguish these two situations, it should proceed as if the device were being disabled. If there are any open handles to the device, the driver should fail this IRP. If no handles are open, the driver should proceed as described in [Handling an IRP\_MN\_QUERY\_STOP\_DEVICE Request (Windows 98/Me)](https://msdn.microsoft.com/library/windows/hardware/ff546684).

See [Plug and Play](https://msdn.microsoft.com/library/windows/hardware/ff547125) for the general rules for handling [Plug and Play Minor IRPs](plug-and-play-minor-irps.md).

**Sending This IRP**

Reserved for system use. Drivers must not send this IRP.

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


[**IRP\_MN\_CANCEL\_STOP\_DEVICE**](irp-mn-cancel-stop-device.md)

[**IRP\_MN\_DEVICE\_USAGE\_NOTIFICATION**](irp-mn-device-usage-notification.md)

[**IRP\_MN\_START\_DEVICE**](irp-mn-start-device.md)

[**IRP\_MN\_STOP\_DEVICE**](irp-mn-stop-device.md)

 

 




