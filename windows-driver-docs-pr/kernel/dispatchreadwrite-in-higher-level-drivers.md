---
title: DispatchReadWrite in Higher-Level Drivers
author: windows-driver-content
description: DispatchReadWrite in Higher-Level Drivers
MS-HAID:
- 'DrvComps\_d1d8c4df-319f-4c55-966a-a02d331cc12b.xml'
- 'kernel.dispatchreadwrite\_in\_higher\_level\_drivers'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: d8406115-c62e-4362-8d2c-77d0414c4104
keywords: ["DispatchReadWrite routine", "dispatch routines WDK kernel , DispatchReadWrite routine", "read/write dispatch routines WDK kernel", "IRP_MJ_WRITE I/O function codes", "IRP_MJ_READ I/O function codes", "data transfers WDK kernel , read/write dispatch routines", "transferring data WDK kernel , read/write dispatch routines"]
---

# DispatchReadWrite in Higher-Level Drivers


## <a href="" id="ddk-dispatchreadwrite-in-higher-level-drivers-kg"></a>


Except for file system drivers, a higher-level driver usually does not have any internal driver queues for IRPs. Such a driver's [*DispatchReadWrite*](https://msdn.microsoft.com/library/windows/hardware/ff543381) routine can pass IRPs with valid parameters on to lower drivers, possibly after setting up its [*IoCompletion*](https://msdn.microsoft.com/library/windows/hardware/ff548354) routine, as described in [Passing IRPs down the Driver Stack](passing-irps-down-the-driver-stack.md).

However, a SCSI class driver's *DispatchReadWrite* routine is responsible for splitting up large transfer requests, if necessary, before it sends an IRP with the major function code [**IRP\_MJ\_READ**](https://msdn.microsoft.com/library/windows/hardware/ff550794) or [**IRP\_MJ\_WRITE**](https://msdn.microsoft.com/library/windows/hardware/ff550819) to the SCSI port/miniport driver pair. For more information, see [Storage Class Driver's SplitTransferRequest Routine](https://msdn.microsoft.com/library/windows/hardware/ff566965).

If a higher-level driver allocates one or more IRPs, which it sets up for the next-lower driver in its *DispatchReadWrite* routine, to request some number of partial transfers, the *DispatchReadWrite* routine must call [**IoSetCompletionRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff549679) with each driver-allocated IRP. The driver must register its *IoCompletion* routine to track how much data is transferred in each partial-transfer operation so that the *IoCompletion* routine can release all driver-allocated IRPs and, eventually, complete the original request.

If the underlying driver controls a removable-media device, any IRPs allocated by the higher-level driver must have a thread context. To set up a thread context, the allocating driver must set the **Irp-&gt;Tail.Overlay**.Thread in each newly allocated IRP from the same value in the incoming transfer IRP. For more information, see [Supporting Removable Media](supporting-removable-media.md).

If the underlying device driver returns an IRP for a partial transfer with an error, the *IoCompletion* routine can either retry the partial-transfer request or complete the original IRP with its I/O status block set with the returned error, after freeing any IRPs and memory the higher-level driver has allocated.

If a higher-level driver's *DispatchReadWrite* routine allocates memory for partial-transfer operations and its allocation will be accessed by the driver's *IoCompletion* routine (or by the underlying device driver), the *DispatchReadWrite* routine must allocate that memory from nonpaged pool.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20DispatchReadWrite%20in%20Higher-Level%20Drivers%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


