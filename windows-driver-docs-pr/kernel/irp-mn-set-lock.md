---
title: IRP_MN_SET_LOCK
description: Bus drivers must handle this IRP for their child devices (child PDOs) that support device locking. Function and filter drivers do not handle this request.
ms.date: 08/12/2017
ms.assetid: d4e09527-f817-4eb5-b0f5-7584de8888b1
keywords:
 - IRP_MN_SET_LOCK Kernel-Mode Driver Architecture
ms.localizationpriority: medium
---

# IRP\_MN\_SET\_LOCK


Bus drivers must handle this IRP for their child devices (child PDOs) that support device locking. Function and filter drivers do not handle this request.

Major Code
----------

[**IRP\_MJ\_PNP**](irp-mj-pnp.md)
When Sent
---------

The PnP manager sends this IRP to direct driver(s) to lock the device and prevent device eject, or to unlock the device.

The PnP manager sends this IRP at IRQL PASSIVE\_LEVEL in an arbitrary thread context.

## Input Parameters


The **Parameters.SetLock.Lock** member of the [**IO\_STACK\_LOCATION**](https://msdn.microsoft.com/library/windows/hardware/ff550659) structure is a BOOLEAN value specifying whether to lock (TRUE) or unlock (FALSE) the device.

## Output Parameters


None

## I/O Status Block


A bus driver sets **Irp-&gt;IoStatus.Status** to STATUS\_SUCCESS or to an appropriate error status.

On success, a driver sets **Irp-&gt;IoStatus.Information** to zero.

If a bus driver does not handle this IRP, it leaves **Irp-&gt;IoStatus.Status** as is and completes the IRP.

Function and filter drivers do not handle this IRP. Such drivers call [**IoSkipCurrentIrpStackLocation**](https://msdn.microsoft.com/library/windows/hardware/ff550355) and pass the IRP down to the next driver. Function and filter drivers do not set an [*IoCompletion*](https://msdn.microsoft.com/library/windows/hardware/ff548354) routine, do not modify **Irp-&gt;IoStatus**, and must not complete the IRP.

Operation
---------

If a driver returns success for this IRP, it ensures that the device has been locked or unlocked before completing the IRP.

See [Plug and Play](https://msdn.microsoft.com/library/windows/hardware/ff547125) for the general rules for handling [Plug and Play minor IRPs](plug-and-play-minor-irps.md).

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

 

 




