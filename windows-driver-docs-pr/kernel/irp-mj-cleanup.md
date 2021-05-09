---
title: IRP_MJ_CLEANUP
description: Drivers that maintain process-specific context information must handle cleanup requests in DispatchCleanup routines.
ms.date: 08/12/2017
keywords:
 - IRP_MJ_CLEANUP Kernel-Mode Driver Architecture
ms.localizationpriority: medium
---

# IRP\_MJ\_CLEANUP


Drivers that maintain process-specific context information must handle cleanup requests in [*DispatchCleanup*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch) routines.

## When Sent

Receipt of this request indicates that the last handle for a file object that is associated with the target device object has been closed (but, due to outstanding I/O requests, might not have been released).

## Input Parameters


None

## Output Parameters


None

## Operation

This IRP is sent in the context of the process that closed the file object handle. Therefore, the driver should release process-specific resources, such as user memory, that the driver previously locked or mapped.

If the driver's device objects were set up as exclusive, so that only a single thread can use the device at a time, the driver must complete every IRP that is currently queued to the target device object and set STATUS\_CANCELLED in each IRP's I/O status block.

Otherwise, the driver must cancel and complete only the currently queued IRPs that are associated with the file object handle that is being released. (A pointer to the file object is located in the **FileObject** member of the driver's [**IO\_STACK\_LOCATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_stack_location) of the IRP.) After canceling these queued IRPs, the driver completes the cleanup IRP and sets STATUS\_SUCCESS in its I/O status block.

For more information about handling this request, see [DispatchCleanup Routines](./dispatchcleanup-routines.md).

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


[*DispatchCleanup*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch)

[**IO\_STACK\_LOCATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_stack_location)

[**IRP\_MJ\_CLOSE**](irp-mj-close.md)

 

