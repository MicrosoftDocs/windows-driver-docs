---
title: A Single DispatchCreateClose Routine
author: windows-driver-content
description: A Single DispatchCreateClose Routine
MS-HAID:
- 'DrvComps\_4114e826-2d0a-4210-af6d-7ecbcdaa2bc3.xml'
- 'kernel.a\_single\_dispatchcreateclose\_routine'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 6127d696-2409-49fc-9cbd-ba1b13c0c672
keywords: ["dispatch routines WDK kernel , DispatchCreateClose routine", "DispatchCreateClose routine", "IRP_MJ_CREATE I/O function code", "IRP_MJ_CLOSE I/O function code", "create dispatch routines WDK kernel", "close dispatch routines WDK kernel"]
---

# A Single DispatchCreateClose Routine


## <a href="" id="ddk-a-single-dispatchcreateclose-routine-kg"></a>


Many drivers, particularly lower-level drivers in a chain of layered drivers, merely need to establish their existence on receipt of a *create* request and merely need to acknowledge the receipt of a *close* request.

For example, a port driver for a device controller with one or more closely coupled class drivers that call [**IoGetDeviceObjectPointer**](https://msdn.microsoft.com/library/windows/hardware/ff549198) might have a minimal [*DispatchCreateClose*](https://msdn.microsoft.com/library/windows/hardware/ff543270) routine. The routine might do nothing more than complete the IRP as follows:

```
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20A%20Single%20DispatchCreateClose%20Routine%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


