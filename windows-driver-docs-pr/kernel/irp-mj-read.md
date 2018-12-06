---
title: IRP_MJ_READ
description: Every device driver that transfers data from its device to the system must handle read requests in a DispatchRead or DispatchReadWrite routine, as must any higher-level driver layered over such a device driver.
ms.date: 08/12/2017
ms.assetid: 5ae4c6c5-d8f2-4dc5-8cfd-ecb751fc88be
keywords:
 - IRP_MJ_READ Kernel-Mode Driver Architecture
ms.localizationpriority: medium
---

# IRP\_MJ\_READ


Every device driver that transfers data from its device to the system must handle read requests in a [*DispatchRead*](https://msdn.microsoft.com/library/windows/hardware/ff543376) or [*DispatchReadWrite*](https://msdn.microsoft.com/library/windows/hardware/ff543381) routine, as must any higher-level driver layered over such a device driver.

When Sent
---------

Any time following the successful completion of a create request.

Possibly, a user-mode application or Win32 component with a handle for the file object representing the target device object has requested a data transfer from the device. Possibly, a higher-level driver has created and set up the read IRP.

## Input Parameters


The driver's I/O stack location in the IRP indicates how many bytes to transfer at **Parameters.Read.Length**.

Some drivers use the value at **Parameters.Read.Key** to sort incoming read requests into a driver-determined order in the device queue or in a driver-managed internal queue of IRPs.

Certain types of drivers also use the value at **Parameters.Read.ByteOffset**, which indicates the starting offset for the transfer operation. For example, see the [**IRP\_MJ\_READ**](https://msdn.microsoft.com/library/windows/hardware/ff549327) topic in the Installable File System (IFS) documentation.

## Output Parameters


Depending on whether the underlying device driver sets up the target device object's **Flags** with DO\_BUFFERED\_IO or with DO\_DIRECT\_IO, data is transferred into one of the following:

-   The buffer at **Irp-&gt;AssociatedIrp.SystemBuffer** if the driver uses buffered I/O.

-   The buffer described by the MDL at **Irp-&gt;MdlAddress** if the underlying device driver uses direct I/O (DMA or PIO).

Operation
---------

On receipt of a read request, a higher-level driver sets up the I/O stack location in the IRP for the next-lower driver, or it creates and sets up additional IRPs for one or more lower drivers. It can set up its [*IoCompletion*](https://msdn.microsoft.com/library/windows/hardware/ff548354) routine, which is optional for the input IRP but required for driver-created IRPs, by calling [**IoSetCompletionRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff549679). Then, the driver passes the request on to the next-lower driver with [**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336).

On receipt of a read request, a device driver transfers data from its device to system memory. The device driver sets the **Information** field of the I/O status block to the number of bytes transferred when it completes the IRP.

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


[*DispatchRead*](https://msdn.microsoft.com/library/windows/hardware/ff543376)

[*DispatchReadWrite*](https://msdn.microsoft.com/library/windows/hardware/ff543381)

[**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336)

[**IoSetCompletionRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff549679)

 

 




