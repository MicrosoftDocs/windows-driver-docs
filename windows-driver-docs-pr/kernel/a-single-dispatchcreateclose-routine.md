---
title: A Single DispatchCreateClose Routine
description: A Single DispatchCreateClose Routine
ms.assetid: 6127d696-2409-49fc-9cbd-ba1b13c0c672
keywords: ["dispatch routines WDK kernel , DispatchCreateClose routine", "DispatchCreateClose routine", "IRP_MJ_CREATE I/O function code", "IRP_MJ_CLOSE I/O function code", "create dispatch routines WDK kernel", "close dispatch routines WDK kernel"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# A Single DispatchCreateClose Routine





Many drivers, particularly lower-level drivers in a chain of layered drivers, merely need to establish their existence on receipt of a *create* request and merely need to acknowledge the receipt of a *close* request.

For example, a port driver for a device controller with one or more closely coupled class drivers that call [**IoGetDeviceObjectPointer**](https://msdn.microsoft.com/library/windows/hardware/ff549198) might have a minimal [*DispatchCreateClose*](https://msdn.microsoft.com/library/windows/hardware/ff543270) routine. The routine might do nothing more than complete the IRP as follows:

```cpp
    :    : 
{ 
    Irp->IoStatus.Status = STATUS_SUCCESS; 
 Irp->IoStatus.Information = 0; 
    IoCompleteRequest(Irp, IO_NO_INCREMENT); 
 return STATUS_SUCCESS; 
}
```

This minimal *DispatchCreateClose* routine sets the **Information** member of the I/O status block to zero, indicating the file object is opened for a create request; **Information** has no meaning for a close request. The routine sets the **Status** member to STATUS\_SUCCESS and also returns this status value, indicating that the driver is ready to accept I/O requests.

This minimal *DispatchCreateClose* routine completes the create IRP without boosting the priority of the originator of the IRP (IO\_NO\_INCREMENT), because the originator is assumed to wait for an indeterminate but very small interval for the request to complete.

How much work a *DispatchCreateClose* routine does depends partly on the nature of the driver's device or the underlying device and partly on the design of the driver. If a driver performs very different operations for create and close requests, it should handle these requests in [separate DispatchCreate and DispatchClose routines](separate-dispatchcreate-and-dispatchclose-routines.md).

To handle a create request to open a file object representing a logical or physical device, a highest-level driver should do the following:

1.  Call [**IoGetCurrentIrpStackLocation**](https://msdn.microsoft.com/library/windows/hardware/ff549174) to get a pointer to its I/O stack location in the IRP.

2.  Check **FileObject**.**FileName** in the I/O stack location and complete the IRP with STATUS\_SUCCESS if the Unicode string at **FileName** has a zero length; otherwise, complete the IRP with STATUS\_INVALID\_PARAMETER.

Following the preceding steps ensures that no attempt to open a pseudofile on a device can cause problems later. For example, this prevents attempts to open a nonexistent \\\\device\\parallel0\\temp.dat.

 

 




