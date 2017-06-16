---
title: DispatchRead, DispatchWrite, and DispatchReadWrite Routines
author: windows-driver-content
description: DispatchRead, DispatchWrite, and DispatchReadWrite Routines
ms.assetid: 2982939a-4afb-4b21-9a96-0ac758f0fb6c
keywords: ["DispatchRead routine", "DispatchWrite routine", "DispatchReadWrite routine", "dispatch routines WDK kernel , DispatchReadWrite routine", "dispatch routines WDK kernel , DispatchWrite routine", "dispatch routines WDK kernel , DispatchRead routine", "read/write dispatch routines WDK kernel", "IRP_MJ_WRITE I/O function codes", "IRP_MJ_READ I/O function codes", "data transfers WDK kernel , read/write dispatch routines", "transferring data WDK kernel , read/write dispatch routines"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# DispatchRead, DispatchWrite, and DispatchReadWrite Routines


## <a href="" id="ddk-dispatchread-dispatchwrite-and-dispatchreadwrite-routines-kg"></a>


A driver's [*DispatchRead*](https://msdn.microsoft.com/library/windows/hardware/ff543376) and [*DispatchWrite*](https://msdn.microsoft.com/library/windows/hardware/ff544034) routines handle IRPs with I/O function codes of [**IRP\_MJ\_READ**](https://msdn.microsoft.com/library/windows/hardware/ff550794) and [**IRP\_MJ\_WRITE**](https://msdn.microsoft.com/library/windows/hardware/ff550819), respectively. Alternatively, a combined [*DispatchReadWrite*](https://msdn.microsoft.com/library/windows/hardware/ff543381) routine can handle IRPs for both of these I/O function codes.

Every driver of a device from which data can be transferred to the system must have a *DispatchRead* routine. Every driver of a device to which data can be transferred from the system must have a *DispatchWrite* routine. Any driver that transfers data in both directions can have a combined *DispatchReadWrite* routine.

Lower-level drivers handle **IRP\_MJ\_READ** and **IRP\_MJ\_WRITE** requests asynchronously. Therefore, *DispatchRead* and/or *DispatchWrite* routines in highest-level drivers must pass these requests on for further processing, provided that the request has valid parameters in that driver's I/O stack location of the IRP.

Whether a driver sets up its device objects for buffered or direct I/O affects how it handles transfer requests. In particular, a driver that uses direct I/O to do DMA operations might need to split up large transfer requests into a sequence of smaller transfer operations in order to satisfy an **IRP\_MJ\_READ** or **IRP\_MJ\_WRITE** request. For more information, see [Input/Output Techniques](i-o-programming-techniques.md).

The following subsections discuss some of the design and implementation considerations for *DispatchReadWrite* routines in lowest-level device drivers that use buffered I/O and direct I/O, as well as in higher-level drivers layered above them:

[Handling Transfers Asynchronously](handling-transfers-asynchronously.md)

[DispatchReadWrite Using Buffered I/O](dispatchreadwrite-using-buffered-i-o.md)

[DispatchReadWrite Using Direct I/O](dispatchreadwrite-using-direct-i-o.md)

[DispatchReadWrite in Higher-Level Drivers](dispatchreadwrite-in-higher-level-drivers.md)

[Summary of Read/Write Dispatch Routines](summary-of-read-write-dispatch-routines.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20DispatchRead,%20DispatchWrite,%20and%20DispatchReadWrite%20Routines%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


