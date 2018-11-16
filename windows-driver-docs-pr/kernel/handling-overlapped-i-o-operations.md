---
title: Handling Overlapped I/O Operations
description: Handling Overlapped I/O Operations
ms.assetid: d13a9fa2-9f68-4c35-af79-dd3f8cec2805
keywords: ["deferred procedure calls WDK kernel", "DPCs WDK kernel", "DpcForIsr", "CustomDpc", "overlapped I/O WDK kernel"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Handling Overlapped I/O Operations





The [*DpcForIsr*](https://msdn.microsoft.com/library/windows/hardware/ff544079) or [*CustomDpc*](https://msdn.microsoft.com/library/windows/hardware/ff542972) routine of a driver that overlaps operations on its device cannot rely on a one-to-one correspondence between requests input to the [*StartIo*](https://msdn.microsoft.com/library/windows/hardware/ff563858) routine and the ISR's calls to [**IoRequestDpc**](https://msdn.microsoft.com/library/windows/hardware/ff549657) or [**KeInsertQueueDpc**](https://msdn.microsoft.com/library/windows/hardware/ff552185). Such a driver's *DpcForIsr* or *CustomDpc* cannot necessarily use the input pointers to the IRP and ISR-supplied context, or the **CurrentIrp** pointer in the target device object, to complete only that IRP.

At any given moment, the same DPC object cannot be queued twice. If an ISR calls **IoRequestDpc** or **KeInsertQueueDpc** more than once before the corresponding *DpcForIsr* or *CustomDpc* executes, the DPC routine runs only once when the IRQL on a processor falls below DISPATCH\_LEVEL. On the other hand, if the ISR calls **IoRequestDpc** or **KeInsertQueueDpc** while the corresponding *DpcForIsr* or *CustomDpc* is running on another processor, the DPC routine can run on two processors concurrently.

Therefore, any driver that overlaps interrupt-driven I/O operations on its device must have the following:

-   A *DpcForIsr* or *CustomDpc* routine that can complete some driver-maintained count of outstanding requests each time it is called

-   An ISR that never overwrites the context information that it passes to a *DpcForIsr* or *CustomDpc* routine, until that routine has used the context information and completed the IRP to which the context information belongs

-   A *SynchCritSection* routine that accesses the ISR's context area on behalf of the *DpcForIsr* or *CustomDpc* routine

 

 




