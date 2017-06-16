---
title: Handling Transfers Asynchronously
author: windows-driver-content
description: Handling Transfers Asynchronously
ms.assetid: 84b231bd-54ff-4312-8e6c-cfc33e72b8cc
keywords: ["DispatchRead routine", "DispatchWrite routine", "DispatchReadWrite routine", "dispatch routines WDK kernel , DispatchReadWrite routine", "dispatch routines WDK kernel , DispatchWrite routine", "dispatch routines WDK kernel , DispatchRead routine", "read/write dispatch routines WDK kernel", "IRP_MJ_WRITE I/O function codes", "IRP_MJ_READ I/O function codes", "data transfers WDK kernel , read/write dispatch routines", "transferring data WDK kernel , read/write dispatch routines", "asynchronous transfers WDK kernel", "data transfers WDK kernel , asynchronous", "transferring data WDK kernel , asynchronous"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Handling Transfers Asynchronously


## <a href="" id="ddk-handling-transfers-asynchronously-kg"></a>


Except for highest-level drivers, all drivers handle [**IRP\_MJ\_READ**](https://msdn.microsoft.com/library/windows/hardware/ff550794) and [**IRP\_MJ\_WRITE**](https://msdn.microsoft.com/library/windows/hardware/ff550819) requests asynchronously. The *DispatchRead* and *DispatchWrite* routines in even a highest-level driver cannot wait for lower-level drivers to finish processing an asynchronous read or write request; they must pass such a request on to lower drivers and return STATUS\_PENDING.

Similarly, a lowest-level device driver's *DispatchReadWrite* routine must pass the transfer request on to other driver routines that process device I/O requests and then return STATUS\_PENDING.

A higher-level driver sometimes must set up partial-transfer IRPs and pass them on to lower drivers. The higher-level driver can complete the original read/write IRP only when its partial-transfer requests have been completed by the lower drivers.

For example, a SCSI class driver's *DispatchReadWrite* routine is required to split large transfer requests that exceed the underlying HBA's transfer capabilities into a set of partial-transfer requests. The class driver must set up the parameters in its partial-transfer IRPs so that the SCSI port/miniport drivers can satisfy each partial-transfer request in a single DMA operation.

Other device drivers that use DMA or PIO also might need to split up large transfer requests for themselves.

For more information about using DMA and PIO, see [Input/Output Techniques](i-o-programming-techniques.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Handling%20Transfers%20Asynchronously%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


