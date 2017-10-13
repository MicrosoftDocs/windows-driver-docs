---
title: IRP_MN_CANCEL_STOP_DEVICE
author: windows-driver-content
description: All PnP drivers must handle this IRP.
ms.author: windowsdriverdev
ms.date: 08/12/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.assetid: 7047c266-84b4-4260-ad75-d56c87c8c9ef
keywords:
 - IRP_MN_CANCEL_STOP_DEVICE Kernel-Mode Driver Architecture
---

# IRP\_MN\_CANCEL\_STOP\_DEVICE


All PnP drivers must handle this IRP.

Major Code
----------

[**IRP\_MJ\_PNP**](irp-mj-pnp.md)
When Sent
---------

The PnP manager sends this IRP, at some point after an [**IRP\_MN\_QUERY\_STOP\_DEVICE**](irp-mn-query-stop-device.md), to inform the drivers for a device that the device will not be disabled (Windows 98/Me only) or stopped for resource reconfiguration.

The PnP manager sends this IRP at IRQL PASSIVE\_LEVEL in the context of a system thread.

## Input Parameters


None

## Output Parameters


None

## I/O Status Block


A driver must set **Irp-&gt;IoStatus.Status** to STATUS\_SUCCESS for this IRP. If a driver fails this IRP, the device is left in an inconsistent state.

Operation
---------

This IRP must be handled first by the parent bus driver for a device and then by each higher driver in the device stack.

In response to this IRP, drivers return the device to the started state. Drivers start any IRPs that were held while the device was in the stop-pending state.

If the device is already in an active state when the driver receives this IRP, a function or filter driver simply sets status to success and passes the IRP to the next driver. The parent bus driver completes the IRP. For such a cancel-stop IRP, a function or filter driver need not set a completion routine.

See [Plug and Play](https://msdn.microsoft.com/library/windows/hardware/ff547125) for detailed information about handling stop IRPs and for the general rules for handling all [Plug and Play minor IRPs](plug-and-play-minor-irps.md).

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


[**IRP\_MN\_QUERY\_STOP\_DEVICE**](irp-mn-query-stop-device.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20IRP_MN_CANCEL_STOP_DEVICE%20%20RELEASE:%20%288/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


