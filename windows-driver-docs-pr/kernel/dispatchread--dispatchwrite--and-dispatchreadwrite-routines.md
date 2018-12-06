---
title: DispatchRead, DispatchWrite, and DispatchReadWrite Routines
description: DispatchRead, DispatchWrite, and DispatchReadWrite Routines
ms.assetid: 2982939a-4afb-4b21-9a96-0ac758f0fb6c
keywords: ["DispatchRead routine", "DispatchWrite routine", "DispatchReadWrite routine", "dispatch routines WDK kernel , DispatchReadWrite routine", "dispatch routines WDK kernel , DispatchWrite routine", "dispatch routines WDK kernel , DispatchRead routine", "read/write dispatch routines WDK kernel", "IRP_MJ_WRITE I/O function codes", "IRP_MJ_READ I/O function codes", "data transfers WDK kernel , read/write dispatch routines", "transferring data WDK kernel , read/write dispatch routines"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# DispatchRead, DispatchWrite, and DispatchReadWrite Routines





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

 

 




