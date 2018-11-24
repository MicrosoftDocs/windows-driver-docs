---
title: IRP_MN_CANCEL_STOP_DEVICE
description: All PnP drivers must handle this IRP.
ms.date: 08/12/2017
ms.assetid: 7047c266-84b4-4260-ad75-d56c87c8c9ef
keywords:
 - IRP_MN_CANCEL_STOP_DEVICE Kernel-Mode Driver Architecture
ms.localizationpriority: medium
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

 

 




