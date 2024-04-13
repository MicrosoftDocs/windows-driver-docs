---
title: IRP_MJ_WRITE
description: Every device driver that transfers data from the system to its device must handle write requests in a DispatchWrite or DispatchReadWrite routine, as must any higher-level driver layered over such a device driver.
ms.date: 08/12/2017
ms.topic: reference
keywords:
 - IRP_MJ_WRITE Kernel-Mode Driver Architecture
---

# IRP\_MJ\_WRITE


Every device driver that transfers data from the system to its device must handle write requests in a [*DispatchWrite*](./dispatchread--dispatchwrite--and-dispatchreadwrite-routines.md) or [*DispatchReadWrite*](./dispatchread--dispatchwrite--and-dispatchreadwrite-routines.md) routine, as must any higher-level driver layered over such a device driver.

## When Sent

Any time following the successful completion of a create request.

Possibly, a user-mode application or Win32 component with a handle for the file object representing the target device object has requested a data transfer to the device. Possibly, a higher-level driver has created and set up the write IRP.

## Input Parameters


The driver's I/O stack location in the IRP indicates how many bytes to transfer at **Parameters.Write.Length**.

Some drivers use the value at **Parameters.Write.Key** to sort incoming write requests into a driver-determined order in the device queue or in a driver-managed internal queue of IRPs.

Certain types of drivers also use the value at **Parameters.Write.ByteOffset**, which indicates the starting offset for the transfer operation. For example, see the [**IRP\_MJ\_WRITE**](../ifs/irp-mj-write.md) topic in the Installable File System (IFS) documentation.

Depending on whether the underlying device driver sets up the target device object's **Flags** with DO\_BUFFERED\_IO or with DO\_DIRECT\_IO, data is transferred from one of the following:

-   The buffer at **Irp-&gt;AssociatedIrp.SystemBuffer**, if the driver uses buffered I/O

-   The buffer described by the MDL at **Irp-&gt;MdlAddress**, if the underlying device driver uses direct I/O (DMA or PIO)

## Output Parameters


None

## Operation

On receipt of a write request, a higher-level driver sets up the I/O stack location in the IRP for the next-lower driver, or it creates and sets up additional IRPs for one or more lower drivers. It can set up its [*IoCompletion*](/windows-hardware/drivers/ddi/wdm/nc-wdm-io_completion_routine) routine, which is optional for the input IRP but required for driver-created IRPs, by calling [**IoSetCompletionRoutine**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iosetcompletionroutine). Then, the driver passes the request on to the next-lower driver with [**IoCallDriver**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocalldriver).

On receipt of a write request, a device driver transfers data from system memory to its device. The device driver sets the **Information** field of the I/O status block to the number of bytes transferred when it completes the IRP.

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


[*DispatchReadWrite*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch)

[*DispatchWrite*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch)

[**IoCallDriver**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocalldriver)

[*IoCompletion*](/windows-hardware/drivers/ddi/wdm/nc-wdm-io_completion_routine)

[**IoSetCompletionRoutine**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iosetcompletionroutine)

 

