---
title: Handling Overlapped I/O Operations
author: windows-driver-content
description: Handling Overlapped I/O Operations
ms.assetid: d13a9fa2-9f68-4c35-af79-dd3f8cec2805
keywords: ["deferred procedure calls WDK kernel", "DPCs WDK kernel", "DpcForIsr", "CustomDpc", "overlapped I/O WDK kernel"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Handling Overlapped I/O Operations


## <a href="" id="ddk-handling-overlapped-i-o-operations-kg"></a>


The [*DpcForIsr*](https://msdn.microsoft.com/library/windows/hardware/ff544079) or [*CustomDpc*](https://msdn.microsoft.com/library/windows/hardware/ff542972) routine of a driver that overlaps operations on its device cannot rely on a one-to-one correspondence between requests input to the [*StartIo*](https://msdn.microsoft.com/library/windows/hardware/ff563858) routine and the ISR's calls to [**IoRequestDpc**](https://msdn.microsoft.com/library/windows/hardware/ff549657) or [**KeInsertQueueDpc**](https://msdn.microsoft.com/library/windows/hardware/ff552185). Such a driver's *DpcForIsr* or *CustomDpc* cannot necessarily use the input pointers to the IRP and ISR-supplied context, or the **CurrentIrp** pointer in the target device object, to complete only that IRP.

At any given moment, the same DPC object cannot be queued twice. If an ISR calls **IoRequestDpc** or **KeInsertQueueDpc** more than once before the corresponding *DpcForIsr* or *CustomDpc* executes, the DPC routine runs only once when the IRQL on a processor falls below DISPATCH\_LEVEL. On the other hand, if the ISR calls **IoRequestDpc** or **KeInsertQueueDpc** while the corresponding *DpcForIsr* or *CustomDpc* is running on another processor, the DPC routine can run on two processors concurrently.

Therefore, any driver that overlaps interrupt-driven I/O operations on its device must have the following:

-   A *DpcForIsr* or *CustomDpc* routine that can complete some driver-maintained count of outstanding requests each time it is called

-   An ISR that never overwrites the context information that it passes to a *DpcForIsr* or *CustomDpc* routine, until that routine has used the context information and completed the IRP to which the context information belongs

-   A *SynchCritSection* routine that accesses the ISR's context area on behalf of the *DpcForIsr* or *CustomDpc* routine

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Handling%20Overlapped%20I/O%20Operations%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


