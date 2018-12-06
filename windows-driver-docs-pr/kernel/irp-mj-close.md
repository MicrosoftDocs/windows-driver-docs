---
title: IRP_MJ_CLOSE
description: Every driver must handle close requests in a DispatchClose routine, with the possible exception of a driver whose device cannot be disabled or removed from the machine without bringing down the system.
ms.date: 08/12/2017
ms.assetid: 109819a8-3787-448d-a766-5d53dbcf55f4
keywords:
 - IRP_MJ_CLOSE Kernel-Mode Driver Architecture
ms.localizationpriority: medium
---

# IRP\_MJ\_CLOSE


Every driver must handle close requests in a [*DispatchClose*](separate-dispatchcreate-and-dispatchclose-routines.md) routine, with the possible exception of a driver whose device cannot be disabled or removed from the machine without bringing down the system. A disk driver whose device holds the system page file is an example of such a driver. Note that the driver of such a device also cannot be unloaded dynamically.

When Sent
---------

Receipt of this request indicates that the last handle of the file object that is associated with the target device object has been closed and released. All outstanding I/O requests have been completed or canceled.

## Input Parameters


None

## Output Parameters


None

Operation
---------

Many device and intermediate drivers merely set STATUS\_SUCCESS in the I/O status block of the IRP and complete the close request. However, what a given driver does on receipt of a close request depends on the driver's design. In general, a driver should undo whatever actions it takes on receipt of the [**IRP\_MJ\_CREATE**](irp-mj-create.md) request. Device drivers whose device objects are exclusive, such as a serial driver, also can reset the hardware on receipt of a close request.

The **IRP\_MJ\_CLOSE** request is not necessarily sent in the context of the process that closed the file object handle. If the driver must release process-specific resources, such as user memory, that the driver previously locked or mapped, it must do so in response to an [**IRP\_MJ\_CLEANUP**](irp-mj-cleanup.md) request.

The **IRP\_MJ\_CLOSE** request will always be sent at PASSIVE\_LEVEL.

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

[*DispatchClose*](separate-dispatchcreate-and-dispatchclose-routines.md)

[**IRP\_MJ\_CLEANUP**](irp-mj-cleanup.md)

[**IRP\_MJ\_CREATE**](irp-mj-create.md)

 

 




