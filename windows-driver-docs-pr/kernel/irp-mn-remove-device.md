---
title: IRP_MN_REMOVE_DEVICE
author: windows-driver-content
description: All PnP drivers must handle this IRP.
ms.author: windowsdriverdev
ms.date: 08/12/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.assetid: 0d733cbd-2da8-48a5-afc6-e1e6b8f507a1
keywords:
 - IRP_MN_REMOVE_DEVICE Kernel-Mode Driver Architecture
---

# IRP\_MN\_REMOVE\_DEVICE


All PnP drivers must handle this IRP.

Major Code
----------

[**IRP\_MJ\_PNP**](irp-mj-pnp.md)
When Sent
---------

The PnP manager uses this IRP to direct drivers to remove a device's software representation (device objects, and so forth). The PnP manager sends this IRP when a device has been removed in an orderly fashion (for example, initiated by a user in the Unplug or Eject Hardware program), by surprise (a user pulls the device from its slot without prior warning), or when the user requests to update driver(s).

On Windows 2000 and later systems, the PnP manager also sends this IRP if one of the drivers in the device stack fails an [**IRP\_MN\_START\_DEVICE**](irp-mn-start-device.md) request for the device.

For an orderly device removal, the PnP manager sends an [**IRP\_MN\_QUERY\_REMOVE\_DEVICE**](irp-mn-query-remove-device.md) prior to the remove IRP. In this case, the device is in the remove-pending state when the remove IRP arrives. For a surprise device removal on Microsoft Windows 2000 or later, the PnP manager sends an [**IRP\_MN\_SURPRISE\_REMOVAL**](irp-mn-surprise-removal.md) prior to the remove IRP. In this case, the device is in the surprise-removed state when the remove IRP arrives. Drivers can also receive a remove IRP before a device is started. In this case, the device is in the non-started state when the IRP arrives.

The PnP manager sends this IRP at IRQL PASSIVE\_LEVEL in the context of a system thread.

## Input Parameters


None

## Output Parameters


None

## I/O Status Block


A driver must set **Irp-&gt;IoStatus.Status** to STATUS\_SUCCESS. Drivers must not fail this IRP.

Operation
---------

This IRP is handled first by the driver at the top of the device stack and then by each lower driver in the stack.

In response to this IRP, drivers perform such tasks as powering down the device, removing the device's software representation (device objects, and so forth), and releasing any resources for the device.

For more information about handling this IRP, see [Handling an IRP\_MN\_REMOVE\_DEVICE Request](https://msdn.microsoft.com/library/windows/hardware/ff546687). For general information about supporting device removal, see [Removing a Device](https://msdn.microsoft.com/library/windows/hardware/ff561046).

**Sending This IRP**

Reserved for system use. Drivers must not send this IRP.

If a bus driver detects that one (or more) of its child devices (child PDOs) has been physically removed from the computer, the bus driver calls [**IoInvalidateDeviceRelations**](https://msdn.microsoft.com/library/windows/hardware/ff549353) to report the change to the PnP manager. The PnP manager then sends remove IRPs for any devices that have disappeared.

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


[**IoInvalidateDeviceRelations**](https://msdn.microsoft.com/library/windows/hardware/ff549353)

[**IoRegisterPlugPlayNotification**](https://msdn.microsoft.com/library/windows/hardware/ff549526)

[**IRP\_MN\_CANCEL\_REMOVE\_DEVICE**](irp-mn-cancel-remove-device.md)

[**IRP\_MN\_QUERY\_REMOVE\_DEVICE**](irp-mn-query-remove-device.md)

[**IRP\_MN\_SURPRISE\_REMOVAL**](irp-mn-surprise-removal.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20IRP_MN_REMOVE_DEVICE%20%20RELEASE:%20%288/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


