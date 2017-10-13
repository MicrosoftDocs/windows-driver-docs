---
title: IRP_MN_QUERY_STOP_DEVICE
author: windows-driver-content
description: All PnP drivers must handle this IRP.
ms.author: windowsdriverdev
ms.date: 08/12/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.assetid: 22f58964-23a0-4307-a748-9c1620e30871
keywords:
 - IRP_MN_QUERY_STOP_DEVICE Kernel-Mode Driver Architecture
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20IRP_MN_QUERY_STOP_DEVICE%20%20RELEASE:%20%288/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


